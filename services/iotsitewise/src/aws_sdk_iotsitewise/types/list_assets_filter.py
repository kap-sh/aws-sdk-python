"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListAssetsFilter``."""

from typing import Literal, TypeAlias, cast

ListAssetsFilter: TypeAlias = Literal[
    "ALL",
    "TOP_LEVEL",
]


# --- restJson1 ser/de ---
def serialize_json(value: ListAssetsFilter) -> str:
    return value


def deserialize_json(data: str) -> ListAssetsFilter:
    return cast(ListAssetsFilter, data)
