"""Generated from Smithy shape ``com.amazonaws.wafv2#DefaultAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.allow_action
    import capo_wafv2.types.block_action


class DefaultAction(TypedDict, closed=True):
    block: NotRequired["capo_wafv2.types.block_action.BlockAction"]
    """<p>Specifies that WAF should block requests by default. </p>"""
    allow: NotRequired["capo_wafv2.types.allow_action.AllowAction"]
    """<p>Specifies that WAF should allow requests by default.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DefaultAction) -> dict:
    out: dict = {}
    if "block" in value:
        import capo_wafv2.types.block_action

        out["Block"] = capo_wafv2.types.block_action.serialize_aws_json_1_1(
            value["block"]
        )
    if "allow" in value:
        import capo_wafv2.types.allow_action

        out["Allow"] = capo_wafv2.types.allow_action.serialize_aws_json_1_1(
            value["allow"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DefaultAction:
    out: DefaultAction = {}  # type: ignore[typeddict-item]
    if "Block" in data:
        import capo_wafv2.types.block_action

        out["block"] = capo_wafv2.types.block_action.deserialize_aws_json_1_1(
            data["Block"]
        )
    if "Allow" in data:
        import capo_wafv2.types.allow_action

        out["allow"] = capo_wafv2.types.allow_action.deserialize_aws_json_1_1(
            data["Allow"]
        )
    return out
