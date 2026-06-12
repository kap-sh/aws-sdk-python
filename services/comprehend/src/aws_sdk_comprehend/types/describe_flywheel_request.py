"""Generated from Smithy shape ``com.amazonaws.comprehend#DescribeFlywheelRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.comprehend_flywheel_arn


class DescribeFlywheelRequest(TypedDict):
    flywheel_arn: (
        "aws_sdk_comprehend.types.comprehend_flywheel_arn.ComprehendFlywheelArn"
    )
    """<p>The Amazon Resource Number (ARN) of the flywheel.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFlywheelRequest) -> dict:
    out: dict = {}
    out["FlywheelArn"] = value["flywheel_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFlywheelRequest:
    out: DescribeFlywheelRequest = {}  # type: ignore[typeddict-item]
    if "FlywheelArn" in data:
        out["flywheel_arn"] = data["FlywheelArn"]
    else:
        raise DeserializationError("DescribeFlywheelRequest.flywheel_arn required")
    return out
