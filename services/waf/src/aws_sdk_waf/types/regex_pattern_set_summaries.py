"""Generated from Smithy shape ``com.amazonaws.waf#RegexPatternSetSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_waf.types.regex_pattern_set_summary

RegexPatternSetSummaries: TypeAlias = list[
    "aws_sdk_waf.types.regex_pattern_set_summary.RegexPatternSetSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegexPatternSetSummaries) -> list:
    import aws_sdk_waf.types.regex_pattern_set_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_waf.types.regex_pattern_set_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RegexPatternSetSummaries:
    import aws_sdk_waf.types.regex_pattern_set_summary

    out: RegexPatternSetSummaries = []
    for item in data:
        out.append(
            aws_sdk_waf.types.regex_pattern_set_summary.deserialize_aws_json_1_1(item)
        )
    return out
