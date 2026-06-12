"""Generated from Smithy shape ``com.amazonaws.waf#RegexMatchSetUpdates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_waf.types.regex_match_set_update

RegexMatchSetUpdates: TypeAlias = list[
    "aws_sdk_waf.types.regex_match_set_update.RegexMatchSetUpdate"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegexMatchSetUpdates) -> list:
    import aws_sdk_waf.types.regex_match_set_update

    out: list = []
    for item in value:
        out.append(
            aws_sdk_waf.types.regex_match_set_update.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RegexMatchSetUpdates:
    import aws_sdk_waf.types.regex_match_set_update

    out: RegexMatchSetUpdates = []
    for item in data:
        out.append(
            aws_sdk_waf.types.regex_match_set_update.deserialize_aws_json_1_1(item)
        )
    return out
