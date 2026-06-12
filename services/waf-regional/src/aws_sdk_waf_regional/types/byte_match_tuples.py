"""Generated from Smithy shape ``com.amazonaws.wafregional#ByteMatchTuples``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.byte_match_tuple

ByteMatchTuples: TypeAlias = list[
    "aws_sdk_waf_regional.types.byte_match_tuple.ByteMatchTuple"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ByteMatchTuples) -> list:
    import aws_sdk_waf_regional.types.byte_match_tuple

    out: list = []
    for item in value:
        out.append(
            aws_sdk_waf_regional.types.byte_match_tuple.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ByteMatchTuples:
    import aws_sdk_waf_regional.types.byte_match_tuple

    out: ByteMatchTuples = []
    for item in data:
        out.append(
            aws_sdk_waf_regional.types.byte_match_tuple.deserialize_aws_json_1_1(item)
        )
    return out
