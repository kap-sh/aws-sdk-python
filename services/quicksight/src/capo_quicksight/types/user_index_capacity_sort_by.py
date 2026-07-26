"""Generated from Smithy shape ``com.amazonaws.quicksight#UserIndexCapacitySortBy``."""

from typing import Literal, TypeAlias, cast

"""<p>The field to sort user index capacity results by.</p>"""
UserIndexCapacitySortBy: TypeAlias = Literal["TOTAL_CAPACITY_BYTES",]


# --- restJson1 ser/de ---
def serialize_json(value: UserIndexCapacitySortBy) -> str:
    return value


def deserialize_json(data: str) -> UserIndexCapacitySortBy:
    return cast(UserIndexCapacitySortBy, data)
