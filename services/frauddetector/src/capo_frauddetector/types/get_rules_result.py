"""Generated from Smithy shape ``com.amazonaws.frauddetector#GetRulesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.rule_detail_list
    import capo_frauddetector.types.string


class GetRulesResult(TypedDict, closed=True):
    rule_details: NotRequired[
        "capo_frauddetector.types.rule_detail_list.RuleDetailList"
    ]
    """<p>The details of the requested rule.</p>"""
    next_token: NotRequired["capo_frauddetector.types.string.string"]
    """<p>The next page token to be used in subsequent requests.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRulesResult) -> dict:
    out: dict = {}
    if "rule_details" in value:
        import capo_frauddetector.types.rule_detail_list

        out["ruleDetails"] = (
            capo_frauddetector.types.rule_detail_list.serialize_aws_json_1_1(
                value["rule_details"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRulesResult:
    out: GetRulesResult = {}  # type: ignore[typeddict-item]
    if "ruleDetails" in data:
        import capo_frauddetector.types.rule_detail_list

        out["rule_details"] = (
            capo_frauddetector.types.rule_detail_list.deserialize_aws_json_1_1(
                data["ruleDetails"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
