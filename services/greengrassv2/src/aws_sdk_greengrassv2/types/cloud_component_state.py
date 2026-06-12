"""Generated from Smithy shape ``com.amazonaws.greengrassv2#CloudComponentState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_greengrassv2.errors import DeserializationError

CloudComponentState: TypeAlias = Literal[
    "REQUESTED",
    "INITIATED",
    "DEPLOYABLE",
    "FAILED",
    "DEPRECATED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REQUESTED",
        "INITIATED",
        "DEPLOYABLE",
        "FAILED",
        "DEPRECATED",
    )
)


def serialize_json(value: CloudComponentState) -> str:
    return value


def deserialize_json(data: str) -> CloudComponentState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CloudComponentState value: {data!r}")
    return cast(CloudComponentState, data)
