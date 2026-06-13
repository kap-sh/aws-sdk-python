"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#FailureCategory``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehubv2.errors import DeserializationError

FailureCategory: TypeAlias = Literal[
    "SHARED_FATE",
    "EXCESSIVE_LOAD",
    "EXCESSIVE_LATENCY",
    "MISCONFIGURATION_AND_BUGS",
    "SINGLE_POINT_OF_FAILURE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SHARED_FATE",
        "EXCESSIVE_LOAD",
        "EXCESSIVE_LATENCY",
        "MISCONFIGURATION_AND_BUGS",
        "SINGLE_POINT_OF_FAILURE",
    )
)


def serialize_json(value: FailureCategory) -> str:
    return value


def deserialize_json(data: str) -> FailureCategory:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FailureCategory value: {data!r}")
    return cast(FailureCategory, data)
