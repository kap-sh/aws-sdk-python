"""Generated from Smithy shape ``com.amazonaws.snowball#DescribeJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_snowball.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_snowball.types.job_id


class DescribeJobRequest(TypedDict, closed=True):
    job_id: "aws_sdk_snowball.types.job_id.JobId"
    """<p>The automatically generated ID for a job, for example <code>JID123e4567-e89b-12d3-a456-426655440000</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeJobRequest) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeJobRequest:
    out: DescribeJobRequest = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    else:
        raise DeserializationError("DescribeJobRequest.job_id required")
    return out
