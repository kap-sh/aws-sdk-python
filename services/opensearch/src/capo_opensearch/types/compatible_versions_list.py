"""Generated from Smithy shape ``com.amazonaws.opensearch#CompatibleVersionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearch.types.compatible_versions_map

CompatibleVersionsList: TypeAlias = list[
    "capo_opensearch.types.compatible_versions_map.CompatibleVersionsMap"
]


# --- restJson1 ser/de ---
def serialize_json(value: CompatibleVersionsList) -> list:
    import capo_opensearch.types.compatible_versions_map

    out: list = []
    for item in value:
        out.append(capo_opensearch.types.compatible_versions_map.serialize_json(item))
    return out


def deserialize_json(data: list) -> CompatibleVersionsList:
    import capo_opensearch.types.compatible_versions_map

    out: CompatibleVersionsList = []
    for item in data:
        out.append(capo_opensearch.types.compatible_versions_map.deserialize_json(item))
    return out
