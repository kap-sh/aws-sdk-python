"""Generated from Smithy shape ``com.amazonaws.m2#AlternateKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_m2.types.alternate_key

AlternateKeyList: TypeAlias = list["aws_sdk_m2.types.alternate_key.AlternateKey"]


# --- restJson1 ser/de ---
def serialize_json(value: AlternateKeyList) -> list:
    import aws_sdk_m2.types.alternate_key

    out: list = []
    for item in value:
        out.append(aws_sdk_m2.types.alternate_key.serialize_json(item))
    return out


def deserialize_json(data: list) -> AlternateKeyList:
    import aws_sdk_m2.types.alternate_key

    out: AlternateKeyList = []
    for item in data:
        out.append(aws_sdk_m2.types.alternate_key.deserialize_json(item))
    return out
