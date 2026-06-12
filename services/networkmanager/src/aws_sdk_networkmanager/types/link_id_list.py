"""Generated from Smithy shape ``com.amazonaws.networkmanager#LinkIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.link_id

LinkIdList: TypeAlias = list["aws_sdk_networkmanager.types.link_id.LinkId"]


# --- restJson1 ser/de ---
def serialize_json(value: LinkIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> LinkIdList:
    return list(data)
