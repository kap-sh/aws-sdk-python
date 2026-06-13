"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#FindingStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehubv2.errors import DeserializationError

FindingStatus: TypeAlias = Literal[
    "OPEN",
    "RESOLVED",
    "IRRELEVANT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OPEN",
        "RESOLVED",
        "IRRELEVANT",
    )
)


def serialize_json(value: FindingStatus) -> str:
    return value


def deserialize_json(data: str) -> FindingStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FindingStatus value: {data!r}")
    return cast(FindingStatus, data)
