"""Generated from Smithy shape ``com.amazonaws.waf#RegexPatternStrings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_waf.types.regex_pattern_string

RegexPatternStrings: TypeAlias = list[
    "capo_waf.types.regex_pattern_string.RegexPatternString"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegexPatternStrings) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> RegexPatternStrings:
    return list(data)
