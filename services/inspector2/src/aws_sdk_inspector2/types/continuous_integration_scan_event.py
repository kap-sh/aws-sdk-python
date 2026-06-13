"""Generated from Smithy shape ``com.amazonaws.inspector2#ContinuousIntegrationScanEvent``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_inspector2.errors import DeserializationError

ContinuousIntegrationScanEvent: TypeAlias = Literal[
    "PULL_REQUEST",
    "PUSH",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PULL_REQUEST",
        "PUSH",
    )
)


def serialize_json(value: ContinuousIntegrationScanEvent) -> str:
    return value


def deserialize_json(data: str) -> ContinuousIntegrationScanEvent:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ContinuousIntegrationScanEvent value: {data!r}"
        )
    return cast(ContinuousIntegrationScanEvent, data)
