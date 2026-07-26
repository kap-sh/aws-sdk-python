"""Generated from Smithy shape ``com.amazonaws.s3control#JobProgressSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.job_number_of_tasks_failed
    import capo_s3_control.types.job_number_of_tasks_succeeded
    import capo_s3_control.types.job_timers
    import capo_s3_control.types.job_total_number_of_tasks


class JobProgressSummary(TypedDict, closed=True):
    total_number_of_tasks: NotRequired[
        "capo_s3_control.types.job_total_number_of_tasks.JobTotalNumberOfTasks"
    ]
    """<p></p>"""
    number_of_tasks_succeeded: NotRequired[
        "capo_s3_control.types.job_number_of_tasks_succeeded.JobNumberOfTasksSucceeded"
    ]
    """<p></p>"""
    number_of_tasks_failed: NotRequired[
        "capo_s3_control.types.job_number_of_tasks_failed.JobNumberOfTasksFailed"
    ]
    """<p></p>"""
    timers: NotRequired["capo_s3_control.types.job_timers.JobTimers"]
    """<p>The JobTimers attribute of a job's progress summary.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: JobProgressSummary, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "total_number_of_tasks" in value:
        SubElement(el, "TotalNumberOfTasks").text = str(value["total_number_of_tasks"])
    if "number_of_tasks_succeeded" in value:
        SubElement(el, "NumberOfTasksSucceeded").text = str(
            value["number_of_tasks_succeeded"]
        )
    if "number_of_tasks_failed" in value:
        SubElement(el, "NumberOfTasksFailed").text = str(
            value["number_of_tasks_failed"]
        )
    if "timers" in value:
        import capo_s3_control.types.job_timers

        capo_s3_control.types.job_timers.serialize_xml(value["timers"], el, "Timers")


def deserialize_xml(el: Element) -> JobProgressSummary:
    out: JobProgressSummary = {}  # type: ignore[typeddict-item]
    child_total_number_of_tasks = el.find("TotalNumberOfTasks")
    if child_total_number_of_tasks is not None:
        out["total_number_of_tasks"] = int(child_total_number_of_tasks.text or "")
    child_number_of_tasks_succeeded = el.find("NumberOfTasksSucceeded")
    if child_number_of_tasks_succeeded is not None:
        out["number_of_tasks_succeeded"] = int(
            child_number_of_tasks_succeeded.text or ""
        )
    child_number_of_tasks_failed = el.find("NumberOfTasksFailed")
    if child_number_of_tasks_failed is not None:
        out["number_of_tasks_failed"] = int(child_number_of_tasks_failed.text or "")
    child_timers = el.find("Timers")
    if child_timers is not None:
        import capo_s3_control.types.job_timers

        out["timers"] = capo_s3_control.types.job_timers.deserialize_xml(child_timers)
    return out
