"""Generated from Smithy shape ``com.amazonaws.shield#ResponseAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_shield.types.block_action
    import aws_sdk_shield.types.count_action


class ResponseAction(TypedDict, closed=True):
    block: NotRequired["aws_sdk_shield.types.block_action.BlockAction"]
    """<p>Specifies that Shield Advanced should configure its WAF rules with the WAF <code>Block</code> action. </p> <p>You must specify exactly one action, either <code>Block</code> or <code>Count</code>.</p>"""
    count: NotRequired["aws_sdk_shield.types.count_action.CountAction"]
    """<p>Specifies that Shield Advanced should configure its WAF rules with the WAF <code>Count</code> action. </p> <p>You must specify exactly one action, either <code>Block</code> or <code>Count</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResponseAction) -> dict:
    out: dict = {}
    if "block" in value:
        import aws_sdk_shield.types.block_action

        out["Block"] = aws_sdk_shield.types.block_action.serialize_aws_json_1_1(
            value["block"]
        )
    if "count" in value:
        import aws_sdk_shield.types.count_action

        out["Count"] = aws_sdk_shield.types.count_action.serialize_aws_json_1_1(
            value["count"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResponseAction:
    out: ResponseAction = {}  # type: ignore[typeddict-item]
    if "Block" in data:
        import aws_sdk_shield.types.block_action

        out["block"] = aws_sdk_shield.types.block_action.deserialize_aws_json_1_1(
            data["Block"]
        )
    if "Count" in data:
        import aws_sdk_shield.types.count_action

        out["count"] = aws_sdk_shield.types.count_action.deserialize_aws_json_1_1(
            data["Count"]
        )
    return out
