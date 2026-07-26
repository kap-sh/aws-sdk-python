"""Generated from Smithy shape ``com.amazonaws.signer#RevokedEntities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_signer.types.string

RevokedEntities: TypeAlias = list["capo_signer.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: RevokedEntities) -> list:
    return list(value)


def deserialize_json(data: list) -> RevokedEntities:
    return list(data)
