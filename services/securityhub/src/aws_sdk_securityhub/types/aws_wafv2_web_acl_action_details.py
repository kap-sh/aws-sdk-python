"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsWafv2WebAclActionDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_wafv2_action_allow_details
    import aws_sdk_securityhub.types.aws_wafv2_action_block_details


class AwsWafv2WebAclActionDetails(TypedDict):
    allow: NotRequired[
        "aws_sdk_securityhub.types.aws_wafv2_action_allow_details.AwsWafv2ActionAllowDetails"
    ]
    """<p> Specifies that WAF should allow requests by default. </p>"""
    block: NotRequired[
        "aws_sdk_securityhub.types.aws_wafv2_action_block_details.AwsWafv2ActionBlockDetails"
    ]
    """<p> Specifies that WAF should block requests by default. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsWafv2WebAclActionDetails) -> dict:
    out: dict = {}
    if "allow" in value:
        import aws_sdk_securityhub.types.aws_wafv2_action_allow_details

        out["Allow"] = (
            aws_sdk_securityhub.types.aws_wafv2_action_allow_details.serialize_json(
                value["allow"]
            )
        )
    if "block" in value:
        import aws_sdk_securityhub.types.aws_wafv2_action_block_details

        out["Block"] = (
            aws_sdk_securityhub.types.aws_wafv2_action_block_details.serialize_json(
                value["block"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsWafv2WebAclActionDetails:
    out: AwsWafv2WebAclActionDetails = {}  # type: ignore[typeddict-item]
    if "Allow" in data:
        import aws_sdk_securityhub.types.aws_wafv2_action_allow_details

        out["allow"] = (
            aws_sdk_securityhub.types.aws_wafv2_action_allow_details.deserialize_json(
                data["Allow"]
            )
        )
    if "Block" in data:
        import aws_sdk_securityhub.types.aws_wafv2_action_block_details

        out["block"] = (
            aws_sdk_securityhub.types.aws_wafv2_action_block_details.deserialize_json(
                data["Block"]
            )
        )
    return out
