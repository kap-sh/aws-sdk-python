"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#TagKeyList``."""

from typing import TypeAlias

TagKeyList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: TagKeyList) -> list:
    return list(value)


def deserialize_json(data: list) -> TagKeyList:
    return list(data)
