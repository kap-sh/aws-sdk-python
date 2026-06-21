"""Generated from Smithy shape ``com.amazonaws.medialive#InputSourceEndBehavior``."""

from typing import Literal, TypeAlias, cast

"""Input Source End Behavior"""
InputSourceEndBehavior: TypeAlias = Literal[
    "CONTINUE",
    "LOOP",
]


# --- restJson1 ser/de ---
def serialize_json(value: InputSourceEndBehavior) -> str:
    return value


def deserialize_json(data: str) -> InputSourceEndBehavior:
    return cast(InputSourceEndBehavior, data)
