"""Generated from Smithy shape ``com.amazonaws.opensearch#OverallChangeStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

"""<p>The overall status value of the domain configuration change.</p>"""
OverallChangeStatus: TypeAlias = Literal[
    "PENDING",
    "PROCESSING",
    "COMPLETED",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "PROCESSING",
        "COMPLETED",
        "FAILED",
    )
)


def serialize_json(value: OverallChangeStatus) -> str:
    return value


def deserialize_json(data: str) -> OverallChangeStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OverallChangeStatus value: {data!r}")
    return cast(OverallChangeStatus, data)
