"""Generated from Smithy shape ``com.amazonaws.guardduty#ResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.string

ResourceList: TypeAlias = list["aws_sdk_guardduty.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceList) -> list:
    return list(value)


def deserialize_json(data: list) -> ResourceList:
    return list(data)
