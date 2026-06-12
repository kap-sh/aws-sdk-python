"""Generated from Smithy shape ``com.amazonaws.medialive#M2tsTimedMetadataBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""M2ts Timed Metadata Behavior"""
M2tsTimedMetadataBehavior: TypeAlias = Literal[
    "NO_PASSTHROUGH",
    "PASSTHROUGH",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NO_PASSTHROUGH",
        "PASSTHROUGH",
    )
)


def serialize_json(value: M2tsTimedMetadataBehavior) -> str:
    return value


def deserialize_json(data: str) -> M2tsTimedMetadataBehavior:
    if data not in _VALUES:
        raise DeserializationError(f"unknown M2tsTimedMetadataBehavior value: {data!r}")
    return cast(M2tsTimedMetadataBehavior, data)
