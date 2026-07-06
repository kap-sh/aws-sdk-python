"""Generated from Smithy shape ``com.amazonaws.databrew#DescribeJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_databrew.types.job_name


class DescribeJobRequest(TypedDict, closed=True):
    name: "aws_sdk_databrew.types.job_name.JobName"
    """<p>The name of the job to be described.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeJobRequest:
    out: DescribeJobRequest = {}  # type: ignore[typeddict-item]
    return out
