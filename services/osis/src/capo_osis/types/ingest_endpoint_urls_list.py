"""Generated from Smithy shape ``com.amazonaws.osis#IngestEndpointUrlsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_osis.types.string

IngestEndpointUrlsList: TypeAlias = list["capo_osis.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: IngestEndpointUrlsList) -> list:
    return list(value)


def deserialize_json(data: list) -> IngestEndpointUrlsList:
    return list(data)
