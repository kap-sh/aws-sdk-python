"""Generated from Smithy shape ``com.amazonaws.emr#InstanceStateChangeReason``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.instance_state_change_reason_code
    import capo_emr.types.string


class InstanceStateChangeReason(TypedDict, closed=True):
    code: NotRequired[
        "capo_emr.types.instance_state_change_reason_code.InstanceStateChangeReasonCode"
    ]
    """<p>The programmable code for the state change reason.</p>"""
    message: NotRequired["capo_emr.types.string.String"]
    """<p>The status change reason description.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceStateChangeReason) -> dict:
    out: dict = {}
    if "code" in value:
        import capo_emr.types.instance_state_change_reason_code

        out["Code"] = (
            capo_emr.types.instance_state_change_reason_code.serialize_aws_json_1_1(
                value["code"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceStateChangeReason:
    out: InstanceStateChangeReason = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        import capo_emr.types.instance_state_change_reason_code

        out["code"] = (
            capo_emr.types.instance_state_change_reason_code.deserialize_aws_json_1_1(
                data["Code"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    return out
