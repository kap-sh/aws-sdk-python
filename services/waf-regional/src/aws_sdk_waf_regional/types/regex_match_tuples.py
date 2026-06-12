"""Generated from Smithy shape ``com.amazonaws.wafregional#RegexMatchTuples``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.regex_match_tuple

RegexMatchTuples: TypeAlias = list[
    "aws_sdk_waf_regional.types.regex_match_tuple.RegexMatchTuple"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegexMatchTuples) -> list:
    import aws_sdk_waf_regional.types.regex_match_tuple

    out: list = []
    for item in value:
        out.append(
            aws_sdk_waf_regional.types.regex_match_tuple.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RegexMatchTuples:
    import aws_sdk_waf_regional.types.regex_match_tuple

    out: RegexMatchTuples = []
    for item in data:
        out.append(
            aws_sdk_waf_regional.types.regex_match_tuple.deserialize_aws_json_1_1(item)
        )
    return out
