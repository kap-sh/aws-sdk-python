"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#OutputKeys``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_elastic_transcoder.types.key

OutputKeys: TypeAlias = list["capo_elastic_transcoder.types.key.Key"]


# --- restJson1 ser/de ---
def serialize_json(value: OutputKeys) -> list:
    return list(value)


def deserialize_json(data: list) -> OutputKeys:
    return list(data)
