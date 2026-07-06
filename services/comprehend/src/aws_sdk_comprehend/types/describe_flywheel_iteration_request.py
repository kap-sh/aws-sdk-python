"""Generated from Smithy shape ``com.amazonaws.comprehend#DescribeFlywheelIterationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.comprehend_flywheel_arn
    import aws_sdk_comprehend.types.flywheel_iteration_id


class DescribeFlywheelIterationRequest(TypedDict, closed=True):
    flywheel_arn: (
        "aws_sdk_comprehend.types.comprehend_flywheel_arn.ComprehendFlywheelArn"
    )
    """<p></p>"""
    flywheel_iteration_id: (
        "aws_sdk_comprehend.types.flywheel_iteration_id.FlywheelIterationId"
    )
    """<p></p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFlywheelIterationRequest) -> dict:
    out: dict = {}
    out["FlywheelArn"] = value["flywheel_arn"]
    out["FlywheelIterationId"] = value["flywheel_iteration_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFlywheelIterationRequest:
    out: DescribeFlywheelIterationRequest = {}  # type: ignore[typeddict-item]
    if "FlywheelArn" in data:
        out["flywheel_arn"] = data["FlywheelArn"]
    else:
        raise DeserializationError(
            "DescribeFlywheelIterationRequest.flywheel_arn required"
        )
    if "FlywheelIterationId" in data:
        out["flywheel_iteration_id"] = data["FlywheelIterationId"]
    else:
        raise DeserializationError(
            "DescribeFlywheelIterationRequest.flywheel_iteration_id required"
        )
    return out
