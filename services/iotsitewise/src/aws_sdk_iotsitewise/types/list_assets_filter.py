"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListAssetsFilter``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

ListAssetsFilter: TypeAlias = Literal[
    "ALL",
    "TOP_LEVEL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL",
        "TOP_LEVEL",
    )
)


def serialize_json(value: ListAssetsFilter) -> str:
    return value


def deserialize_json(data: str) -> ListAssetsFilter:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ListAssetsFilter value: {data!r}")
    return cast(ListAssetsFilter, data)
