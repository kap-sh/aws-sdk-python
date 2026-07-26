"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsWafv2WebAclActionDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_wafv2_action_allow_details
    import capo_securityhub.types.aws_wafv2_action_block_details


class AwsWafv2WebAclActionDetails(TypedDict, closed=True):
    allow: NotRequired[
        "capo_securityhub.types.aws_wafv2_action_allow_details.AwsWafv2ActionAllowDetails"
    ]
    """<p> Specifies that WAF should allow requests by default. </p>"""
    block: NotRequired[
        "capo_securityhub.types.aws_wafv2_action_block_details.AwsWafv2ActionBlockDetails"
    ]
    """<p> Specifies that WAF should block requests by default. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsWafv2WebAclActionDetails) -> dict:
    out: dict = {}
    if "allow" in value:
        import capo_securityhub.types.aws_wafv2_action_allow_details

        out["Allow"] = (
            capo_securityhub.types.aws_wafv2_action_allow_details.serialize_json(
                value["allow"]
            )
        )
    if "block" in value:
        import capo_securityhub.types.aws_wafv2_action_block_details

        out["Block"] = (
            capo_securityhub.types.aws_wafv2_action_block_details.serialize_json(
                value["block"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsWafv2WebAclActionDetails:
    out: AwsWafv2WebAclActionDetails = {}  # type: ignore[typeddict-item]
    if "Allow" in data:
        import capo_securityhub.types.aws_wafv2_action_allow_details

        out["allow"] = (
            capo_securityhub.types.aws_wafv2_action_allow_details.deserialize_json(
                data["Allow"]
            )
        )
    if "Block" in data:
        import capo_securityhub.types.aws_wafv2_action_block_details

        out["block"] = (
            capo_securityhub.types.aws_wafv2_action_block_details.deserialize_json(
                data["Block"]
            )
        )
    return out
