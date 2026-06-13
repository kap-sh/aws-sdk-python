"""Generated from Smithy shape ``com.amazonaws.securityagent#FindingStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityagent.errors import DeserializationError

"""<p>Finding status.</p>"""
FindingStatus: TypeAlias = Literal[
    "ACTIVE",
    "RESOLVED",
    "ACCEPTED",
    "FALSE_POSITIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "RESOLVED",
        "ACCEPTED",
        "FALSE_POSITIVE",
    )
)


def serialize_json(value: FindingStatus) -> str:
    return value


def deserialize_json(data: str) -> FindingStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FindingStatus value: {data!r}")
    return cast(FindingStatus, data)
