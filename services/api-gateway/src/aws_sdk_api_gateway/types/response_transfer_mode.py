"""Generated from Smithy shape ``com.amazonaws.apigateway#ResponseTransferMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_api_gateway.errors import DeserializationError

ResponseTransferMode: TypeAlias = Literal[
    "BUFFERED",
    "STREAM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BUFFERED",
        "STREAM",
    )
)


def serialize_json(value: ResponseTransferMode) -> str:
    return value


def deserialize_json(data: str) -> ResponseTransferMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResponseTransferMode value: {data!r}")
    return cast(ResponseTransferMode, data)
