"""Generated from Smithy shape ``com.amazonaws.macie2#SearchResourcesComparator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

"""<p>The operator to use in a condition that filters the results of a query. Valid values are:</p>"""
SearchResourcesComparator: TypeAlias = Literal[
    "EQ",
    "NE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EQ",
        "NE",
    )
)


def serialize_json(value: SearchResourcesComparator) -> str:
    return value


def deserialize_json(data: str) -> SearchResourcesComparator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SearchResourcesComparator value: {data!r}")
    return cast(SearchResourcesComparator, data)
