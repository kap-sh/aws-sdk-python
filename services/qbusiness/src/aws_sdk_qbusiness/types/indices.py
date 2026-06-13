"""Generated from Smithy shape ``com.amazonaws.qbusiness#Indices``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.index

Indices: TypeAlias = list["aws_sdk_qbusiness.types.index.Index"]


# --- restJson1 ser/de ---
def serialize_json(value: Indices) -> list:
    import aws_sdk_qbusiness.types.index

    out: list = []
    for item in value:
        out.append(aws_sdk_qbusiness.types.index.serialize_json(item))
    return out


def deserialize_json(data: list) -> Indices:
    import aws_sdk_qbusiness.types.index

    out: Indices = []
    for item in data:
        out.append(aws_sdk_qbusiness.types.index.deserialize_json(item))
    return out
