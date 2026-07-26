"""Generated from Smithy shape ``com.amazonaws.wafv2#RuleAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.allow_action
    import capo_wafv2.types.block_action
    import capo_wafv2.types.captcha_action
    import capo_wafv2.types.challenge_action
    import capo_wafv2.types.count_action


class RuleAction(TypedDict, closed=True):
    block: NotRequired["capo_wafv2.types.block_action.BlockAction"]
    """<p>Instructs WAF to block the web request.</p>"""
    allow: NotRequired["capo_wafv2.types.allow_action.AllowAction"]
    """<p>Instructs WAF to allow the web request.</p>"""
    count: NotRequired["capo_wafv2.types.count_action.CountAction"]
    """<p>Instructs WAF to count the web request and then continue evaluating the request using the remaining rules in the web ACL.</p>"""
    captcha: NotRequired["capo_wafv2.types.captcha_action.CaptchaAction"]
    """<p>Instructs WAF to run a <code>CAPTCHA</code> check against the web request.</p>"""
    challenge: NotRequired["capo_wafv2.types.challenge_action.ChallengeAction"]
    """<p>Instructs WAF to run a <code>Challenge</code> check against the web request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleAction) -> dict:
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
    if "count" in value:
        import capo_wafv2.types.count_action

        out["Count"] = capo_wafv2.types.count_action.serialize_aws_json_1_1(
            value["count"]
        )
    if "captcha" in value:
        import capo_wafv2.types.captcha_action

        out["Captcha"] = capo_wafv2.types.captcha_action.serialize_aws_json_1_1(
            value["captcha"]
        )
    if "challenge" in value:
        import capo_wafv2.types.challenge_action

        out["Challenge"] = capo_wafv2.types.challenge_action.serialize_aws_json_1_1(
            value["challenge"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RuleAction:
    out: RuleAction = {}  # type: ignore[typeddict-item]
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
    if "Count" in data:
        import capo_wafv2.types.count_action

        out["count"] = capo_wafv2.types.count_action.deserialize_aws_json_1_1(
            data["Count"]
        )
    if "Captcha" in data:
        import capo_wafv2.types.captcha_action

        out["captcha"] = capo_wafv2.types.captcha_action.deserialize_aws_json_1_1(
            data["Captcha"]
        )
    if "Challenge" in data:
        import capo_wafv2.types.challenge_action

        out["challenge"] = capo_wafv2.types.challenge_action.deserialize_aws_json_1_1(
            data["Challenge"]
        )
    return out
