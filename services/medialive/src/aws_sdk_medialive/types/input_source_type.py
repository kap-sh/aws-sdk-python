"""Generated from Smithy shape ``com.amazonaws.medialive#InputSourceType``."""

from typing import Literal, TypeAlias, cast

"""There are two types of input sources, static and dynamic. If an input source is dynamic you can change the source url of the input dynamically using an input switch action. Currently, two input types support a dynamic url at this time, MP4_FILE and TS_FILE. By default all input sources are static."""
InputSourceType: TypeAlias = Literal[
    "STATIC",
    "DYNAMIC",
]


# --- restJson1 ser/de ---
def serialize_json(value: InputSourceType) -> str:
    return value


def deserialize_json(data: str) -> InputSourceType:
    return cast(InputSourceType, data)
