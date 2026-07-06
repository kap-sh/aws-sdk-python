"""Generated from Smithy shape ``com.amazonaws.wafregional#WafOverrideAction``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_waf_regional.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.waf_override_action_type


class WafOverrideAction(TypedDict, closed=True):
    type: "aws_sdk_waf_regional.types.waf_override_action_type.WafOverrideActionType"
    """<p> <code>COUNT</code> overrides the action specified by the individual rule within a <code>RuleGroup</code> . If set to <code>NONE</code>, the rule's action will take place.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WafOverrideAction) -> dict:
    out: dict = {}
    import aws_sdk_waf_regional.types.waf_override_action_type

    out["Type"] = (
        aws_sdk_waf_regional.types.waf_override_action_type.serialize_aws_json_1_1(
            value["type"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> WafOverrideAction:
    out: WafOverrideAction = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_waf_regional.types.waf_override_action_type

        out["type"] = (
            aws_sdk_waf_regional.types.waf_override_action_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("WafOverrideAction.type required")
    return out
