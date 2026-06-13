"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#Identifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_gameliftstreams.types.identifier

Identifiers: TypeAlias = list["aws_sdk_gameliftstreams.types.identifier.Identifier"]


# --- restJson1 ser/de ---
def serialize_json(value: Identifiers) -> list:
    return list(value)


def deserialize_json(data: list) -> Identifiers:
    return list(data)
