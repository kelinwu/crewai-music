from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task



@CrewBase
class Hit2Crew():
	"""Hit crew"""

	@agent
	def songwriter(self) -> Agent:
		return Agent(
			config=self.agents_config['songwriter'],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True
		)

	@agent
	def producer(self) -> Agent:
		return Agent(
			config=self.agents_config['producer'],
			verbose=True
		)

	@task
	def songwriting(self) -> Task:
		return Task(
			config=self.tasks_config['songwriting'],
		)

	@task
	def producing(self) -> Task:
		return Task(
			config=self.tasks_config['producing'],
			output_file='song.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Hit crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)