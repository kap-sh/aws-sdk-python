"""Generated from Smithy shape ``com.amazonaws.m2#IdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_m2.types.identifier

IdentifierList: TypeAlias = list["aws_sdk_m2.types.identifier.Identifier"]


# --- restJson1 ser/de ---
def serialize_json(value: IdentifierList) -> list:
    return list(value)


def deserialize_json(data: list) -> IdentifierList:
    return list(data)
