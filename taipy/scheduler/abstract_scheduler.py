from abc import abstractmethod
from typing import Callable, Iterable, List, Optional

from taipy.job.job import Job
from taipy.task.task import Task


class AbstractScheduler:
    """Creates and schedules Jobs.

    Attributes:
        data_manager: DataManager is an element that retrieves and deals with Data Node.

    """

    @abstractmethod
    def submit(self, pipeline, callbacks: Optional[Iterable[Callable]]) -> List[Job]:
        return NotImplemented

    @abstractmethod
    def submit_task(self, task: Task, callbacks: Optional[Iterable[Callable]] = None) -> Job:
        return NotImplemented

    @abstractmethod
    def is_running(self) -> bool:
        return NotImplemented

    @abstractmethod
    def start(self):
        return NotImplemented

    @abstractmethod
    def stop(self):
        return NotImplemented
