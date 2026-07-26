"""Generated from Smithy shape ``com.amazonaws.mediatailor#__listOfSourceLocation``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediatailor.types.source_location

__listOfSourceLocation: TypeAlias = list[
    "capo_mediatailor.types.source_location.SourceLocation"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfSourceLocation) -> list:
    import capo_mediatailor.types.source_location

    out: list = []
    for item in value:
        out.append(capo_mediatailor.types.source_location.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfSourceLocation:
    import capo_mediatailor.types.source_location

    out: __listOfSourceLocation = []
    for item in data:
        out.append(capo_mediatailor.types.source_location.deserialize_json(item))
    return out
