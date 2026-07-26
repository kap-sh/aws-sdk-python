"""Generated from Smithy shape ``com.amazonaws.s3control#JobFailure``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.job_failure_code
    import capo_s3_control.types.job_failure_reason


class JobFailure(TypedDict, closed=True):
    failure_code: NotRequired["capo_s3_control.types.job_failure_code.JobFailureCode"]
    """<p>The failure code, if any, for the specified job.</p>"""
    failure_reason: NotRequired[
        "capo_s3_control.types.job_failure_reason.JobFailureReason"
    ]
    """<p>The failure reason, if any, for the specified job.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: JobFailure, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "failure_code" in value:
        SubElement(el, "FailureCode").text = str(value["failure_code"])
    if "failure_reason" in value:
        SubElement(el, "FailureReason").text = str(value["failure_reason"])


def deserialize_xml(el: Element) -> JobFailure:
    out: JobFailure = {}  # type: ignore[typeddict-item]
    child_failure_code = el.find("FailureCode")
    if child_failure_code is not None:
        out["failure_code"] = str(child_failure_code.text or "")
    child_failure_reason = el.find("FailureReason")
    if child_failure_reason is not None:
        out["failure_reason"] = str(child_failure_reason.text or "")
    return out
