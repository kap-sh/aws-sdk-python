"""Generated from Smithy shape ``com.amazonaws.macie2#ListJobsFilterKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

"""<p>The property to use to filter the results. Valid values are:</p>"""
ListJobsFilterKey: TypeAlias = Literal[
    "jobType",
    "jobStatus",
    "createdAt",
    "name",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "jobType",
        "jobStatus",
        "createdAt",
        "name",
    )
)


def serialize_json(value: ListJobsFilterKey) -> str:
    return value


def deserialize_json(data: str) -> ListJobsFilterKey:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ListJobsFilterKey value: {data!r}")
    return cast(ListJobsFilterKey, data)
