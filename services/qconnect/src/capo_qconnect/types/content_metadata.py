"""Generated from Smithy shape ``com.amazonaws.qconnect#ContentMetadata``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.non_empty_string

ContentMetadata: TypeAlias = dict[
    "capo_qconnect.types.non_empty_string.NonEmptyString",
    "capo_qconnect.types.non_empty_string.NonEmptyString",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ContentMetadata) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ContentMetadata:
    out: ContentMetadata = {}
    for key, value in data.items():
        out[key] = value
    return out
