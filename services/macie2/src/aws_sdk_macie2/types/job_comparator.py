"""Generated from Smithy shape ``com.amazonaws.macie2#JobComparator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

"""<p>The operator to use in a condition. Depending on the type of condition, possible values are:</p>"""
JobComparator: TypeAlias = Literal[
    "EQ",
    "GT",
    "GTE",
    "LT",
    "LTE",
    "NE",
    "CONTAINS",
    "STARTS_WITH",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EQ",
        "GT",
        "GTE",
        "LT",
        "LTE",
        "NE",
        "CONTAINS",
        "STARTS_WITH",
    )
)


def serialize_json(value: JobComparator) -> str:
    return value


def deserialize_json(data: str) -> JobComparator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JobComparator value: {data!r}")
    return cast(JobComparator, data)
