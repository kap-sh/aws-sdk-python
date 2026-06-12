"""Generated from Smithy shape ``com.amazonaws.wafv2#ActionCondition``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.action_value


class ActionCondition(TypedDict):
    action: "aws_sdk_wafv2.types.action_value.ActionValue"
    """<p>The action setting that a log record must contain in order to meet the condition. This is the action that WAF applied to the web request. </p> <p>For rule groups, this is either the configured rule action setting, or if you've applied a rule action override to the rule, it's the override action. The value <code>EXCLUDED_AS_COUNT</code> matches on excluded rules and also on rules that have a rule action override of Count. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionCondition) -> dict:
    out: dict = {}
    import aws_sdk_wafv2.types.action_value

    out["Action"] = aws_sdk_wafv2.types.action_value.serialize_aws_json_1_1(
        value["action"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ActionCondition:
    out: ActionCondition = {}  # type: ignore[typeddict-item]
    if "Action" in data:
        import aws_sdk_wafv2.types.action_value

        out["action"] = aws_sdk_wafv2.types.action_value.deserialize_aws_json_1_1(
            data["Action"]
        )
    else:
        raise DeserializationError("ActionCondition.action required")
    return out
