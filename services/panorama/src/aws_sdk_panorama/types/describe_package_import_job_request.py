"""Generated from Smithy shape ``com.amazonaws.panorama#DescribePackageImportJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_panorama.types.job_id


class DescribePackageImportJobRequest(TypedDict):
    job_id: "aws_sdk_panorama.types.job_id.JobId"
    """<p>The job's ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribePackageImportJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribePackageImportJobRequest:
    out: DescribePackageImportJobRequest = {}  # type: ignore[typeddict-item]
    return out
