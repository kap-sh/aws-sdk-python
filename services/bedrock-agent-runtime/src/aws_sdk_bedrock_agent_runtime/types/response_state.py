"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ResponseState``."""

from typing import Literal, TypeAlias, cast

ResponseState: TypeAlias = Literal[
    "FAILURE",
    "REPROMPT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResponseState) -> str:
    return value


def deserialize_json(data: str) -> ResponseState:
    return cast(ResponseState, data)
