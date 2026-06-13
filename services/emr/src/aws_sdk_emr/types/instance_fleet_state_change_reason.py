"""Generated from Smithy shape ``com.amazonaws.emr#InstanceFleetStateChangeReason``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.instance_fleet_state_change_reason_code
    import aws_sdk_emr.types.string


class InstanceFleetStateChangeReason(TypedDict):
    code: NotRequired[
        "aws_sdk_emr.types.instance_fleet_state_change_reason_code.InstanceFleetStateChangeReasonCode"
    ]
    """<p>A code corresponding to the reason the state change occurred.</p>"""
    message: NotRequired["aws_sdk_emr.types.string.String"]
    """<p>An explanatory message.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceFleetStateChangeReason) -> dict:
    out: dict = {}
    if "code" in value:
        import aws_sdk_emr.types.instance_fleet_state_change_reason_code

        out["Code"] = (
            aws_sdk_emr.types.instance_fleet_state_change_reason_code.serialize_aws_json_1_1(
                value["code"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceFleetStateChangeReason:
    out: InstanceFleetStateChangeReason = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        import aws_sdk_emr.types.instance_fleet_state_change_reason_code

        out["code"] = (
            aws_sdk_emr.types.instance_fleet_state_change_reason_code.deserialize_aws_json_1_1(
                data["Code"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    return out
