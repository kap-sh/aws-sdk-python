"""Generated from Smithy shape ``com.amazonaws.inspector2#CisSortOrder``."""

from typing import Literal, TypeAlias, cast

CisSortOrder: TypeAlias = Literal[
    "ASC",
    "DESC",
]


# --- restJson1 ser/de ---
def serialize_json(value: CisSortOrder) -> str:
    return value


def deserialize_json(data: str) -> CisSortOrder:
    return cast(CisSortOrder, data)
