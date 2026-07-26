"""Generated from Smithy shape ``com.amazonaws.apigateway#ResponseTransferMode``."""

from typing import Literal, TypeAlias, cast

ResponseTransferMode: TypeAlias = Literal[
    "BUFFERED",
    "STREAM",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResponseTransferMode) -> str:
    return value


def deserialize_json(data: str) -> ResponseTransferMode:
    return cast(ResponseTransferMode, data)
