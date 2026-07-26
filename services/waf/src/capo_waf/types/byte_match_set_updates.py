"""Generated from Smithy shape ``com.amazonaws.waf#ByteMatchSetUpdates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_waf.types.byte_match_set_update

ByteMatchSetUpdates: TypeAlias = list[
    "capo_waf.types.byte_match_set_update.ByteMatchSetUpdate"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ByteMatchSetUpdates) -> list:
    import capo_waf.types.byte_match_set_update

    out: list = []
    for item in value:
        out.append(capo_waf.types.byte_match_set_update.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ByteMatchSetUpdates:
    import capo_waf.types.byte_match_set_update

    out: ByteMatchSetUpdates = []
    for item in data:
        out.append(capo_waf.types.byte_match_set_update.deserialize_aws_json_1_1(item))
    return out
