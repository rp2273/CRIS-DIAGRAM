import json
import pandas as pd
import matplotlib.pyplot as plt


with open('HHT.json', 'r') as file:
    data = json.load(file)

projects = []
data_received = []
data_consumed = []

for project, details in data.items():
    projects.append(details['projectName'])
    received_data = ', '.join([v for k, v in details['dataReceived'].items() if v])
    consumed_data = ', '.join([v for k, v in details['dataConsumed'].items() if v])
    data_received.append(received_data)
    data_consumed.append(consumed_data)

df = pd.DataFrame({
    'Project': projects,
    'Data Received': data_received,
    'Data Consumed': data_consumed
})

df['Data Received Count'] = df['Data Received'].apply(lambda x: len(x.split(', ')) if x else 0)
df['Data Consumed Count'] = df['Data Consumed'].apply(lambda x: len(x.split(', ')) if x else 0)

plt.ion()

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(df['Project'], df['Data Received Count'], label='Data Received Count', alpha=0.7, color='b')
ax.bar(df['Project'], df['Data Consumed Count'], label='Data Consumed Count', alpha=0.7, color='r', bottom=df['Data Received Count'])
ax.set_xlabel('Project')
ax.set_ylabel('Count')
ax.set_title('Bar Plot: Data Received and Consumed Count per Project')
ax.legend()
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show(block=False)

plt.figure(figsize=(8, 8))
plt.pie(df['Data Received Count'], labels=df['Project'], autopct='%1.1f%%', startangle=140)
plt.title('Pie Chart: Data Received Distribution')
plt.show(block=False)

plt.figure(figsize=(8, 8))
plt.pie(df['Data Consumed Count'], labels=df['Project'], autopct='%1.1f%%', startangle=140)
plt.title('Pie Chart: Data Consumed Distribution')
plt.show(block=False)

plt.figure(figsize=(10, 6))
plt.plot(df['Project'], df['Data Received Count'], marker='o', label='Data Received Count', color='b')
plt.plot(df['Project'], df['Data Consumed Count'], marker='o', label='Data Consumed Count', color='r')
plt.xlabel('Project')
plt.ylabel('Count')
plt.title('Line Plot: Data Received and Consumed Count per Project')
plt.legend()
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show(block=False)

input("Press Enter to close the plots...")