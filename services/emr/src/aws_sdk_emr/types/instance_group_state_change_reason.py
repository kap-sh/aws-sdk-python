"""Generated from Smithy shape ``com.amazonaws.emr#InstanceGroupStateChangeReason``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr.types.instance_group_state_change_reason_code
    import aws_sdk_emr.types.string


class InstanceGroupStateChangeReason(TypedDict, closed=True):
    code: NotRequired[
        "aws_sdk_emr.types.instance_group_state_change_reason_code.InstanceGroupStateChangeReasonCode"
    ]
    """<p>The programmable code for the state change reason.</p>"""
    message: NotRequired["aws_sdk_emr.types.string.String"]
    """<p>The status change reason description.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceGroupStateChangeReason) -> dict:
    out: dict = {}
    if "code" in value:
        import aws_sdk_emr.types.instance_group_state_change_reason_code

        out["Code"] = (
            aws_sdk_emr.types.instance_group_state_change_reason_code.serialize_aws_json_1_1(
                value["code"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceGroupStateChangeReason:
    out: InstanceGroupStateChangeReason = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        import aws_sdk_emr.types.instance_group_state_change_reason_code

        out["code"] = (
            aws_sdk_emr.types.instance_group_state_change_reason_code.deserialize_aws_json_1_1(
                data["Code"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    return out
