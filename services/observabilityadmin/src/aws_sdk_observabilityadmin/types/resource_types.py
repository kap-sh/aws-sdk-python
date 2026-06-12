"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#ResourceTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.resource_type

ResourceTypes: TypeAlias = list[
    "aws_sdk_observabilityadmin.types.resource_type.ResourceType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceTypes) -> list:
    import aws_sdk_observabilityadmin.types.resource_type

    out: list = []
    for item in value:
        out.append(aws_sdk_observabilityadmin.types.resource_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResourceTypes:
    import aws_sdk_observabilityadmin.types.resource_type

    out: ResourceTypes = []
    for item in data:
        out.append(
            aws_sdk_observabilityadmin.types.resource_type.deserialize_json(item)
        )
    return out
