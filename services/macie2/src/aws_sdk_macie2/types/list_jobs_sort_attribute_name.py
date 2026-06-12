"""Generated from Smithy shape ``com.amazonaws.macie2#ListJobsSortAttributeName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

"""<p>The property to sort the results by. Valid values are:</p>"""
ListJobsSortAttributeName: TypeAlias = Literal[
    "createdAt",
    "jobStatus",
    "name",
    "jobType",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "createdAt",
        "jobStatus",
        "name",
        "jobType",
    )
)


def serialize_json(value: ListJobsSortAttributeName) -> str:
    return value


def deserialize_json(data: str) -> ListJobsSortAttributeName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ListJobsSortAttributeName value: {data!r}")
    return cast(ListJobsSortAttributeName, data)
