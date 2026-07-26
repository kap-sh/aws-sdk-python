"""Generated from Smithy shape ``com.amazonaws.waf#ByteMatchTuples``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_waf.types.byte_match_tuple

ByteMatchTuples: TypeAlias = list["capo_waf.types.byte_match_tuple.ByteMatchTuple"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ByteMatchTuples) -> list:
    import capo_waf.types.byte_match_tuple

    out: list = []
    for item in value:
        out.append(capo_waf.types.byte_match_tuple.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ByteMatchTuples:
    import capo_waf.types.byte_match_tuple

    out: ByteMatchTuples = []
    for item in data:
        out.append(capo_waf.types.byte_match_tuple.deserialize_aws_json_1_1(item))
    return out
