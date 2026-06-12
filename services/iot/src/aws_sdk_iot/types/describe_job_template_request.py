"""Generated from Smithy shape ``com.amazonaws.iot#DescribeJobTemplateRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.job_template_id


class DescribeJobTemplateRequest(TypedDict):
    job_template_id: "aws_sdk_iot.types.job_template_id.JobTemplateId"
    """<p>The unique identifier of the job template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeJobTemplateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeJobTemplateRequest:
    out: DescribeJobTemplateRequest = {}  # type: ignore[typeddict-item]
    return out
