"""Generated from Smithy shape ``com.amazonaws.workdocs#SignedHeaderMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.header_name_type
    import aws_sdk_workdocs.types.header_value_type

SignedHeaderMap: TypeAlias = dict[
    "aws_sdk_workdocs.types.header_name_type.HeaderNameType",
    "aws_sdk_workdocs.types.header_value_type.HeaderValueType",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: SignedHeaderMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> SignedHeaderMap:
    out: SignedHeaderMap = {}
    for key, value in data.items():
        out[key] = value
    return out
