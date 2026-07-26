"""Generated from Smithy shape ``com.amazonaws.quicksight#UserIndexCapacitySortOrder``."""

from typing import Literal, TypeAlias, cast

"""<p>The sort order for user index capacity results.</p>"""
UserIndexCapacitySortOrder: TypeAlias = Literal[
    "ASC",
    "DESC",
]


# --- restJson1 ser/de ---
def serialize_json(value: UserIndexCapacitySortOrder) -> str:
    return value


def deserialize_json(data: str) -> UserIndexCapacitySortOrder:
    return cast(UserIndexCapacitySortOrder, data)
