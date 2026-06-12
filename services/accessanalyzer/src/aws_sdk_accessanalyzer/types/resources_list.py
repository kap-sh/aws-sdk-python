"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#ResourcesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.resource

ResourcesList: TypeAlias = list["aws_sdk_accessanalyzer.types.resource.Resource"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourcesList) -> list:
    return list(value)


def deserialize_json(data: list) -> ResourcesList:
    return list(data)
