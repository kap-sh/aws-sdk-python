"""Generated from Smithy shape ``com.amazonaws.medialive#VideoDescriptionRespondToAfd``."""

from typing import Literal, TypeAlias, cast

"""Video Description Respond To Afd"""
VideoDescriptionRespondToAfd: TypeAlias = Literal[
    "NONE",
    "PASSTHROUGH",
    "RESPOND",
]


# --- restJson1 ser/de ---
def serialize_json(value: VideoDescriptionRespondToAfd) -> str:
    return value


def deserialize_json(data: str) -> VideoDescriptionRespondToAfd:
    return cast(VideoDescriptionRespondToAfd, data)
