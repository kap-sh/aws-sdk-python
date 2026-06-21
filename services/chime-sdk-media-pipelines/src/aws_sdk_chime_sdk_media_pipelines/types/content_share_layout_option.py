"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#ContentShareLayoutOption``."""

from typing import Literal, TypeAlias, cast

ContentShareLayoutOption: TypeAlias = Literal[
    "PresenterOnly",
    "Horizontal",
    "Vertical",
    "ActiveSpeakerOnly",
]


# --- restJson1 ser/de ---
def serialize_json(value: ContentShareLayoutOption) -> str:
    return value


def deserialize_json(data: str) -> ContentShareLayoutOption:
    return cast(ContentShareLayoutOption, data)
