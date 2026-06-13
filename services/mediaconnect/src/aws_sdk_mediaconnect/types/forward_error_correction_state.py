"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ForwardErrorCorrectionState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

ForwardErrorCorrectionState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: ForwardErrorCorrectionState) -> str:
    return value


def deserialize_json(data: str) -> ForwardErrorCorrectionState:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ForwardErrorCorrectionState value: {data!r}"
        )
    return cast(ForwardErrorCorrectionState, data)
