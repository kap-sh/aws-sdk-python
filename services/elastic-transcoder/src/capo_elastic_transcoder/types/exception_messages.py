"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#ExceptionMessages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_elastic_transcoder.types.string

ExceptionMessages: TypeAlias = list["capo_elastic_transcoder.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: ExceptionMessages) -> list:
    return list(value)


def deserialize_json(data: list) -> ExceptionMessages:
    return list(data)
