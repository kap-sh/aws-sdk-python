"""Generated from Smithy shape ``com.amazonaws.quicksight#UserIndexCapacitySortBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

"""<p>The field to sort user index capacity results by.</p>"""
UserIndexCapacitySortBy: TypeAlias = Literal["TOTAL_CAPACITY_BYTES",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("TOTAL_CAPACITY_BYTES",))


def serialize_json(value: UserIndexCapacitySortBy) -> str:
    return value


def deserialize_json(data: str) -> UserIndexCapacitySortBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UserIndexCapacitySortBy value: {data!r}")
    return cast(UserIndexCapacitySortBy, data)
