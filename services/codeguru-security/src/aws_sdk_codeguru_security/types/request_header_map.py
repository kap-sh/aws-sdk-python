"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#RequestHeaderMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codeguru_security.types.header_key
    import aws_sdk_codeguru_security.types.header_value

RequestHeaderMap: TypeAlias = dict[
    "aws_sdk_codeguru_security.types.header_key.HeaderKey",
    "aws_sdk_codeguru_security.types.header_value.HeaderValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: RequestHeaderMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> RequestHeaderMap:
    out: RequestHeaderMap = {}
    for key, value in data.items():
        out[key] = value
    return out
