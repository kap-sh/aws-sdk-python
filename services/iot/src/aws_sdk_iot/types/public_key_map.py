"""Generated from Smithy shape ``com.amazonaws.iot#PublicKeyMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.key_name
    import aws_sdk_iot.types.key_value

PublicKeyMap: TypeAlias = dict[
    "aws_sdk_iot.types.key_name.KeyName", "aws_sdk_iot.types.key_value.KeyValue"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: PublicKeyMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> PublicKeyMap:
    out: PublicKeyMap = {}
    for key, value in data.items():
        out[key] = value
    return out
