"""Generated from Smithy shape ``com.amazonaws.mediaconvert#InputFilterEnable``."""

from typing import Literal, TypeAlias, cast

"""Specify whether to apply input filtering to improve the video quality of your input. To apply filtering depending on your input type and quality: Choose Auto. To apply no filtering: Choose Disable. To apply filtering regardless of your input type and quality: Choose Force. When you do, you must also specify a value for Filter strength."""
InputFilterEnable: TypeAlias = Literal[
    "AUTO",
    "DISABLE",
    "FORCE",
]


# --- restJson1 ser/de ---
def serialize_json(value: InputFilterEnable) -> str:
    return value


def deserialize_json(data: str) -> InputFilterEnable:
    return cast(InputFilterEnable, data)
