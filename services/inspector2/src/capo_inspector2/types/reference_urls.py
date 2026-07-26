"""Generated from Smithy shape ``com.amazonaws.inspector2#ReferenceUrls``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.non_empty_string

ReferenceUrls: TypeAlias = list["capo_inspector2.types.non_empty_string.NonEmptyString"]


# --- restJson1 ser/de ---
def serialize_json(value: ReferenceUrls) -> list:
    return list(value)


def deserialize_json(data: list) -> ReferenceUrls:
    return list(data)
