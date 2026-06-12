"""Generated from Smithy shape ``com.amazonaws.licensemanagerlinuxsubscriptions#ProductCodeList``."""

from typing import TypeAlias

ProductCodeList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ProductCodeList) -> list:
    return list(value)


def deserialize_json(data: list) -> ProductCodeList:
    return list(data)
