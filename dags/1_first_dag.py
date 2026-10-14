from airflow.sdk import dag, task

@dag(
        dag_id='first_dag'
)
def first_dag():
    @task.python
    def first_task():
        print('this is first task')
    
    @task.python
    def second_task():
        print('this is second task')
    @task.python
    def third_task():
        print('this is third task complete!')
    #call tasks
    first = first_task()
    second = second_task()
    third = third_task()

    #define task dependencies
    first >> second >> third

#Instantiate the DAG
first_dag()