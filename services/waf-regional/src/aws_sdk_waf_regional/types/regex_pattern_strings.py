"""Generated from Smithy shape ``com.amazonaws.wafregional#RegexPatternStrings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.regex_pattern_string

RegexPatternStrings: TypeAlias = list[
    "aws_sdk_waf_regional.types.regex_pattern_string.RegexPatternString"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegexPatternStrings) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> RegexPatternStrings:
    return list(data)
