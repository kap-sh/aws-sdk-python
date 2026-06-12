"""Generated from Smithy shape ``com.amazonaws.networkmanager#SiteIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.site_id

SiteIdList: TypeAlias = list["aws_sdk_networkmanager.types.site_id.SiteId"]


# --- restJson1 ser/de ---
def serialize_json(value: SiteIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> SiteIdList:
    return list(data)
