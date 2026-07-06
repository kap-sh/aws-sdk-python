"""Generated from Smithy shape ``com.amazonaws.panorama#DescribeDeviceJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_panorama.types.job_id


class DescribeDeviceJobRequest(TypedDict, closed=True):
    job_id: "aws_sdk_panorama.types.job_id.JobId"
    """<p>The job's ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDeviceJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeDeviceJobRequest:
    out: DescribeDeviceJobRequest = {}  # type: ignore[typeddict-item]
    return out
