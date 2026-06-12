"""Generated from Smithy shape ``com.amazonaws.greengrassv2#ResolvedComponentVersionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.resolved_component_version

ResolvedComponentVersionsList: TypeAlias = list[
    "aws_sdk_greengrassv2.types.resolved_component_version.ResolvedComponentVersion"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResolvedComponentVersionsList) -> list:
    import aws_sdk_greengrassv2.types.resolved_component_version

    out: list = []
    for item in value:
        out.append(
            aws_sdk_greengrassv2.types.resolved_component_version.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ResolvedComponentVersionsList:
    import aws_sdk_greengrassv2.types.resolved_component_version

    out: ResolvedComponentVersionsList = []
    for item in data:
        out.append(
            aws_sdk_greengrassv2.types.resolved_component_version.deserialize_json(item)
        )
    return out
