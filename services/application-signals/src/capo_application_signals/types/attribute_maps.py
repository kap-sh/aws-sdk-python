"""Generated from Smithy shape ``com.amazonaws.applicationsignals#AttributeMaps``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_signals.types.attribute_map

AttributeMaps: TypeAlias = list[
    "capo_application_signals.types.attribute_map.AttributeMap"
]


# --- restJson1 ser/de ---
def serialize_json(value: AttributeMaps) -> list:
    import capo_application_signals.types.attribute_map

    out: list = []
    for item in value:
        out.append(capo_application_signals.types.attribute_map.serialize_json(item))
    return out


def deserialize_json(data: list) -> AttributeMaps:
    import capo_application_signals.types.attribute_map

    out: AttributeMaps = []
    for item in data:
        out.append(capo_application_signals.types.attribute_map.deserialize_json(item))
    return out
