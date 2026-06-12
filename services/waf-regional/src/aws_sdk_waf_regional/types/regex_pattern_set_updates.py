"""Generated from Smithy shape ``com.amazonaws.wafregional#RegexPatternSetUpdates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.regex_pattern_set_update

RegexPatternSetUpdates: TypeAlias = list[
    "aws_sdk_waf_regional.types.regex_pattern_set_update.RegexPatternSetUpdate"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegexPatternSetUpdates) -> list:
    import aws_sdk_waf_regional.types.regex_pattern_set_update

    out: list = []
    for item in value:
        out.append(
            aws_sdk_waf_regional.types.regex_pattern_set_update.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RegexPatternSetUpdates:
    import aws_sdk_waf_regional.types.regex_pattern_set_update

    out: RegexPatternSetUpdates = []
    for item in data:
        out.append(
            aws_sdk_waf_regional.types.regex_pattern_set_update.deserialize_aws_json_1_1(
                item
            )
        )
    return out
