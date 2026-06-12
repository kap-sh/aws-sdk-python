"""Generated from Smithy shape ``com.amazonaws.s3control#CreateJobResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.job_id


class CreateJobResult(TypedDict):
    job_id: NotRequired["aws_sdk_s3_control.types.job_id.JobId"]
    """<p>The ID for this job. Amazon S3 generates this ID automatically and returns it after a successful <code>Create Job</code> request.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: CreateJobResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "job_id" in value:
        SubElement(el, "JobId").text = str(value["job_id"])


def deserialize_xml(el: Element) -> CreateJobResult:
    out: CreateJobResult = {}  # type: ignore[typeddict-item]
    child_job_id = el.find("JobId")
    if child_job_id is not None:
        out["job_id"] = str(child_job_id.text or "")
    return out
