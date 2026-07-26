"""Generated from Smithy shape ``com.amazonaws.account#RegionOptList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_account.types.region

RegionOptList: TypeAlias = list["capo_account.types.region.Region"]


# --- restJson1 ser/de ---
def serialize_json(value: RegionOptList) -> list:
    import capo_account.types.region

    out: list = []
    for item in value:
        out.append(capo_account.types.region.serialize_json(item))
    return out


def deserialize_json(data: list) -> RegionOptList:
    import capo_account.types.region

    out: RegionOptList = []
    for item in data:
        out.append(capo_account.types.region.deserialize_json(item))
    return out
