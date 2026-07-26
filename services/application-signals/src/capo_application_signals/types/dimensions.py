"""Generated from Smithy shape ``com.amazonaws.applicationsignals#Dimensions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_signals.types.dimension

Dimensions: TypeAlias = list["capo_application_signals.types.dimension.Dimension"]


# --- restJson1 ser/de ---
def serialize_json(value: Dimensions) -> list:
    import capo_application_signals.types.dimension

    out: list = []
    for item in value:
        out.append(capo_application_signals.types.dimension.serialize_json(item))
    return out


def deserialize_json(data: list) -> Dimensions:
    import capo_application_signals.types.dimension

    out: Dimensions = []
    for item in data:
        out.append(capo_application_signals.types.dimension.deserialize_json(item))
    return out
