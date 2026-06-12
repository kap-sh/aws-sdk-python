"""Generated from Smithy shape ``com.amazonaws.dlm#ResourceTypeValuesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dlm.types.resource_type_values

ResourceTypeValuesList: TypeAlias = list[
    "aws_sdk_dlm.types.resource_type_values.ResourceTypeValues"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceTypeValuesList) -> list:
    import aws_sdk_dlm.types.resource_type_values

    out: list = []
    for item in value:
        out.append(aws_sdk_dlm.types.resource_type_values.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResourceTypeValuesList:
    import aws_sdk_dlm.types.resource_type_values

    out: ResourceTypeValuesList = []
    for item in data:
        out.append(aws_sdk_dlm.types.resource_type_values.deserialize_json(item))
    return out
