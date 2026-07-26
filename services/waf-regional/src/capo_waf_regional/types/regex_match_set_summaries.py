"""Generated from Smithy shape ``com.amazonaws.wafregional#RegexMatchSetSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_waf_regional.types.regex_match_set_summary

RegexMatchSetSummaries: TypeAlias = list[
    "capo_waf_regional.types.regex_match_set_summary.RegexMatchSetSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegexMatchSetSummaries) -> list:
    import capo_waf_regional.types.regex_match_set_summary

    out: list = []
    for item in value:
        out.append(
            capo_waf_regional.types.regex_match_set_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RegexMatchSetSummaries:
    import capo_waf_regional.types.regex_match_set_summary

    out: RegexMatchSetSummaries = []
    for item in data:
        out.append(
            capo_waf_regional.types.regex_match_set_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
