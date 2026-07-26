"""Generated from Smithy shape ``com.amazonaws.wafregional#RegexPatternSetSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_waf_regional.types.regex_pattern_set_summary

RegexPatternSetSummaries: TypeAlias = list[
    "capo_waf_regional.types.regex_pattern_set_summary.RegexPatternSetSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegexPatternSetSummaries) -> list:
    import capo_waf_regional.types.regex_pattern_set_summary

    out: list = []
    for item in value:
        out.append(
            capo_waf_regional.types.regex_pattern_set_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RegexPatternSetSummaries:
    import capo_waf_regional.types.regex_pattern_set_summary

    out: RegexPatternSetSummaries = []
    for item in data:
        out.append(
            capo_waf_regional.types.regex_pattern_set_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
