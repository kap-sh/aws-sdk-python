"""Generated from Smithy shape ``com.amazonaws.groundstation#ComponentVersionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.component_version

ComponentVersionList: TypeAlias = list[
    "aws_sdk_groundstation.types.component_version.ComponentVersion"
]


# --- restJson1 ser/de ---
def serialize_json(value: ComponentVersionList) -> list:
    import aws_sdk_groundstation.types.component_version

    out: list = []
    for item in value:
        out.append(aws_sdk_groundstation.types.component_version.serialize_json(item))
    return out


def deserialize_json(data: list) -> ComponentVersionList:
    import aws_sdk_groundstation.types.component_version

    out: ComponentVersionList = []
    for item in data:
        out.append(aws_sdk_groundstation.types.component_version.deserialize_json(item))
    return out
