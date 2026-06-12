"""Generated from Smithy shape ``com.amazonaws.medialive#M2tsAbsentInputAudioBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""M2ts Absent Input Audio Behavior"""
M2tsAbsentInputAudioBehavior: TypeAlias = Literal[
    "DROP",
    "ENCODE_SILENCE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DROP",
        "ENCODE_SILENCE",
    )
)


def serialize_json(value: M2tsAbsentInputAudioBehavior) -> str:
    return value


def deserialize_json(data: str) -> M2tsAbsentInputAudioBehavior:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown M2tsAbsentInputAudioBehavior value: {data!r}"
        )
    return cast(M2tsAbsentInputAudioBehavior, data)
