"""Generated from Smithy shape ``com.amazonaws.iotsitewise#PortalTools``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.name

PortalTools: TypeAlias = list["aws_sdk_iotsitewise.types.name.Name"]


# --- restJson1 ser/de ---
def serialize_json(value: PortalTools) -> list:
    return list(value)


def deserialize_json(data: list) -> PortalTools:
    return list(data)
