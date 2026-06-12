"""Generated from Smithy shape ``com.amazonaws.snowball#DescribeReturnShippingLabelRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_snowball.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_snowball.types.job_id


class DescribeReturnShippingLabelRequest(TypedDict):
    job_id: "aws_sdk_snowball.types.job_id.JobId"
    """<p>The automatically generated ID for a job, for example <code>JID123e4567-e89b-12d3-a456-426655440000</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeReturnShippingLabelRequest) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeReturnShippingLabelRequest:
    out: DescribeReturnShippingLabelRequest = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    else:
        raise DeserializationError("DescribeReturnShippingLabelRequest.job_id required")
    return out
