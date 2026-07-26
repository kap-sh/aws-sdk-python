"""Generated from Smithy shape ``com.amazonaws.wafv2#RegularExpressionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wafv2.types.regex

RegularExpressionList: TypeAlias = list["capo_wafv2.types.regex.Regex"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegularExpressionList) -> list:
    import capo_wafv2.types.regex

    out: list = []
    for item in value:
        out.append(capo_wafv2.types.regex.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RegularExpressionList:
    import capo_wafv2.types.regex

    out: RegularExpressionList = []
    for item in data:
        out.append(capo_wafv2.types.regex.deserialize_aws_json_1_1(item))
    return out
