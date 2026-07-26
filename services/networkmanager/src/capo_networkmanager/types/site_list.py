"""Generated from Smithy shape ``com.amazonaws.networkmanager#SiteList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkmanager.types.site

SiteList: TypeAlias = list["capo_networkmanager.types.site.Site"]


# --- restJson1 ser/de ---
def serialize_json(value: SiteList) -> list:
    import capo_networkmanager.types.site

    out: list = []
    for item in value:
        out.append(capo_networkmanager.types.site.serialize_json(item))
    return out


def deserialize_json(data: list) -> SiteList:
    import capo_networkmanager.types.site

    out: SiteList = []
    for item in data:
        out.append(capo_networkmanager.types.site.deserialize_json(item))
    return out
