"""Generated from Smithy shape ``com.amazonaws.pipes#HeaderParametersMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pipes.types.header_key
    import aws_sdk_pipes.types.header_value

HeaderParametersMap: TypeAlias = dict[
    "aws_sdk_pipes.types.header_key.HeaderKey",
    "aws_sdk_pipes.types.header_value.HeaderValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: HeaderParametersMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> HeaderParametersMap:
    out: HeaderParametersMap = {}
    for key, value in data.items():
        out[key] = value
    return out
