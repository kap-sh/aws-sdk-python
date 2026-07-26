"""Generated from Smithy shape ``com.amazonaws.mediaconvert#InputPolicy``."""

from typing import Literal, TypeAlias, cast

"""An input policy allows or disallows a job you submit to run based on the conditions that you specify."""
InputPolicy: TypeAlias = Literal[
    "ALLOWED",
    "DISALLOWED",
]


# --- restJson1 ser/de ---
def serialize_json(value: InputPolicy) -> str:
    return value


def deserialize_json(data: str) -> InputPolicy:
    return cast(InputPolicy, data)
