"""Generated from Smithy shape ``com.amazonaws.s3control#DescribeJobResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.job_descriptor


class DescribeJobResult(TypedDict, closed=True):
    job: NotRequired["aws_sdk_s3_control.types.job_descriptor.JobDescriptor"]
    """<p>Contains the configuration parameters and status for the job specified in the <code>Describe Job</code> request.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: DescribeJobResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "job" in value:
        import aws_sdk_s3_control.types.job_descriptor

        aws_sdk_s3_control.types.job_descriptor.serialize_xml(value["job"], el, "Job")


def deserialize_xml(el: Element) -> DescribeJobResult:
    out: DescribeJobResult = {}  # type: ignore[typeddict-item]
    child_job = el.find("Job")
    if child_job is not None:
        import aws_sdk_s3_control.types.job_descriptor

        out["job"] = aws_sdk_s3_control.types.job_descriptor.deserialize_xml(child_job)
    return out
