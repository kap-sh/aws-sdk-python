"""Generated from Smithy shape ``com.amazonaws.comprehend#StartFlywheelIterationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.comprehend_flywheel_arn
    import aws_sdk_comprehend.types.flywheel_iteration_id


class StartFlywheelIterationResponse(TypedDict, closed=True):
    flywheel_arn: NotRequired[
        "aws_sdk_comprehend.types.comprehend_flywheel_arn.ComprehendFlywheelArn"
    ]
    """<p></p>"""
    flywheel_iteration_id: NotRequired[
        "aws_sdk_comprehend.types.flywheel_iteration_id.FlywheelIterationId"
    ]
    """<p></p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartFlywheelIterationResponse) -> dict:
    out: dict = {}
    if "flywheel_arn" in value:
        out["FlywheelArn"] = value["flywheel_arn"]
    if "flywheel_iteration_id" in value:
        out["FlywheelIterationId"] = value["flywheel_iteration_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartFlywheelIterationResponse:
    out: StartFlywheelIterationResponse = {}  # type: ignore[typeddict-item]
    if "FlywheelArn" in data:
        out["flywheel_arn"] = data["FlywheelArn"]
    if "FlywheelIterationId" in data:
        out["flywheel_iteration_id"] = data["FlywheelIterationId"]
    return out
