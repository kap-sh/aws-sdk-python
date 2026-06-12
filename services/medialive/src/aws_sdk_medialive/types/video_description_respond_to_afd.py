"""Generated from Smithy shape ``com.amazonaws.medialive#VideoDescriptionRespondToAfd``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Video Description Respond To Afd"""
VideoDescriptionRespondToAfd: TypeAlias = Literal[
    "NONE",
    "PASSTHROUGH",
    "RESPOND",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "PASSTHROUGH",
        "RESPOND",
    )
)


def serialize_json(value: VideoDescriptionRespondToAfd) -> str:
    return value


def deserialize_json(data: str) -> VideoDescriptionRespondToAfd:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown VideoDescriptionRespondToAfd value: {data!r}"
        )
    return cast(VideoDescriptionRespondToAfd, data)
