"""Generated from Smithy shape ``com.amazonaws.comprehend#DeleteFlywheelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import capo_comprehend.types.comprehend_flywheel_arn


class DeleteFlywheelRequest(TypedDict, closed=True):
    flywheel_arn: "capo_comprehend.types.comprehend_flywheel_arn.ComprehendFlywheelArn"
    """<p>The Amazon Resource Number (ARN) of the flywheel to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteFlywheelRequest) -> dict:
    out: dict = {}
    out["FlywheelArn"] = value["flywheel_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteFlywheelRequest:
    out: DeleteFlywheelRequest = {}  # type: ignore[typeddict-item]
    if "FlywheelArn" in data:
        out["flywheel_arn"] = data["FlywheelArn"]
    else:
        raise DeserializationError("DeleteFlywheelRequest.flywheel_arn required")
    return out
