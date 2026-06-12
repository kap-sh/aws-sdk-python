"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#Regions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.region

Regions: TypeAlias = list["aws_sdk_observabilityadmin.types.region.Region"]


# --- restJson1 ser/de ---
def serialize_json(value: Regions) -> list:
    return list(value)


def deserialize_json(data: list) -> Regions:
    return list(data)
