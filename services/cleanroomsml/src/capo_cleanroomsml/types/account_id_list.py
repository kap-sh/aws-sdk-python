"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#AccountIdList``."""

from typing import TypeAlias

AccountIdList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: AccountIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> AccountIdList:
    return list(data)
