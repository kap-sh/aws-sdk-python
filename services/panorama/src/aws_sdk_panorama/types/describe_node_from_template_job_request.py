"""Generated from Smithy shape ``com.amazonaws.panorama#DescribeNodeFromTemplateJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_panorama.types.job_id


class DescribeNodeFromTemplateJobRequest(TypedDict):
    job_id: "aws_sdk_panorama.types.job_id.JobId"
    """<p>The job's ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeNodeFromTemplateJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeNodeFromTemplateJobRequest:
    out: DescribeNodeFromTemplateJobRequest = {}  # type: ignore[typeddict-item]
    return out
