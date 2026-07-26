"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsWafv2RulesActionDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_wafv2_action_allow_details
    import capo_securityhub.types.aws_wafv2_action_block_details
    import capo_securityhub.types.aws_wafv2_rules_action_captcha_details
    import capo_securityhub.types.aws_wafv2_rules_action_count_details


class AwsWafv2RulesActionDetails(TypedDict, closed=True):
    allow: NotRequired[
        "capo_securityhub.types.aws_wafv2_action_allow_details.AwsWafv2ActionAllowDetails"
    ]
    """<p> Instructs WAF to allow the web request. </p>"""
    block: NotRequired[
        "capo_securityhub.types.aws_wafv2_action_block_details.AwsWafv2ActionBlockDetails"
    ]
    """<p> Instructs WAF to block the web request. </p>"""
    captcha: NotRequired[
        "capo_securityhub.types.aws_wafv2_rules_action_captcha_details.AwsWafv2RulesActionCaptchaDetails"
    ]
    """<p> Instructs WAF to run a CAPTCHA check against the web request. </p>"""
    count: NotRequired[
        "capo_securityhub.types.aws_wafv2_rules_action_count_details.AwsWafv2RulesActionCountDetails"
    ]
    """<p> Instructs WAF to count the web request and then continue evaluating the request using the remaining rules in the web ACL. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsWafv2RulesActionDetails) -> dict:
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
    if "captcha" in value:
        import capo_securityhub.types.aws_wafv2_rules_action_captcha_details

        out["Captcha"] = (
            capo_securityhub.types.aws_wafv2_rules_action_captcha_details.serialize_json(
                value["captcha"]
            )
        )
    if "count" in value:
        import capo_securityhub.types.aws_wafv2_rules_action_count_details

        out["Count"] = (
            capo_securityhub.types.aws_wafv2_rules_action_count_details.serialize_json(
                value["count"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsWafv2RulesActionDetails:
    out: AwsWafv2RulesActionDetails = {}  # type: ignore[typeddict-item]
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
    if "Captcha" in data:
        import capo_securityhub.types.aws_wafv2_rules_action_captcha_details

        out["captcha"] = (
            capo_securityhub.types.aws_wafv2_rules_action_captcha_details.deserialize_json(
                data["Captcha"]
            )
        )
    if "Count" in data:
        import capo_securityhub.types.aws_wafv2_rules_action_count_details

        out["count"] = (
            capo_securityhub.types.aws_wafv2_rules_action_count_details.deserialize_json(
                data["Count"]
            )
        )
    return out
