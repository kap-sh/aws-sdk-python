"""Generated from Smithy shape ``com.amazonaws.quicksight#UserIndexCapacitySortOrder``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

"""<p>The sort order for user index capacity results.</p>"""
UserIndexCapacitySortOrder: TypeAlias = Literal[
    "ASC",
    "DESC",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASC",
        "DESC",
    )
)


def serialize_json(value: UserIndexCapacitySortOrder) -> str:
    return value


def deserialize_json(data: str) -> UserIndexCapacitySortOrder:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown UserIndexCapacitySortOrder value: {data!r}"
        )
    return cast(UserIndexCapacitySortOrder, data)
