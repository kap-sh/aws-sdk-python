"""Generated from Smithy shape ``com.amazonaws.eventbridge#ConnectionOAuthHttpMethod``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_eventbridge.errors import DeserializationError

ConnectionOAuthHttpMethod: TypeAlias = Literal[
    "GET",
    "POST",
    "PUT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GET",
        "POST",
        "PUT",
    )
)


def serialize_aws_json_1_1(value: ConnectionOAuthHttpMethod) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConnectionOAuthHttpMethod:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectionOAuthHttpMethod value: {data!r}")
    return cast(ConnectionOAuthHttpMethod, data)
