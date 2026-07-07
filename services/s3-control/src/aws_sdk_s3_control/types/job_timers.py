"""Generated from Smithy shape ``com.amazonaws.s3control#JobTimers``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.job_time_in_state_seconds


class JobTimers(TypedDict, closed=True):
    elapsed_time_in_active_seconds: NotRequired[
        "aws_sdk_s3_control.types.job_time_in_state_seconds.JobTimeInStateSeconds"
    ]
    """<p>Indicates the elapsed time in seconds the job has been in the Active job state.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: JobTimers, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "elapsed_time_in_active_seconds" in value:
        SubElement(el, "ElapsedTimeInActiveSeconds").text = str(
            value["elapsed_time_in_active_seconds"]
        )


def deserialize_xml(el: Element) -> JobTimers:
    out: JobTimers = {}  # type: ignore[typeddict-item]
    child_elapsed_time_in_active_seconds = el.find("ElapsedTimeInActiveSeconds")
    if child_elapsed_time_in_active_seconds is not None:
        out["elapsed_time_in_active_seconds"] = int(
            child_elapsed_time_in_active_seconds.text or ""
        )
    return out
