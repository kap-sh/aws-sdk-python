"""Generated from Smithy shape ``com.amazonaws.greengrassv2#ResolvedComponentVersionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_greengrassv2.types.resolved_component_version

ResolvedComponentVersionsList: TypeAlias = list[
    "capo_greengrassv2.types.resolved_component_version.ResolvedComponentVersion"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResolvedComponentVersionsList) -> list:
    import capo_greengrassv2.types.resolved_component_version

    out: list = []
    for item in value:
        out.append(
            capo_greengrassv2.types.resolved_component_version.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ResolvedComponentVersionsList:
    import capo_greengrassv2.types.resolved_component_version

    out: ResolvedComponentVersionsList = []
    for item in data:
        out.append(
            capo_greengrassv2.types.resolved_component_version.deserialize_json(item)
        )
    return out
