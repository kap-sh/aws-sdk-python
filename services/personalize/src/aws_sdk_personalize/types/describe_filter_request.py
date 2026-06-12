"""Generated from Smithy shape ``com.amazonaws.personalize#DescribeFilterRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn


class DescribeFilterRequest(TypedDict):
    filter_arn: "aws_sdk_personalize.types.arn.Arn"
    """<p>The ARN of the filter to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFilterRequest) -> dict:
    out: dict = {}
    out["filterArn"] = value["filter_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFilterRequest:
    out: DescribeFilterRequest = {}  # type: ignore[typeddict-item]
    if "filterArn" in data:
        out["filter_arn"] = data["filterArn"]
    else:
        raise DeserializationError("DescribeFilterRequest.filter_arn required")
    return out
