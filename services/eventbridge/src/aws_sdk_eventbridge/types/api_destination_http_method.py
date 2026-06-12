"""Generated from Smithy shape ``com.amazonaws.eventbridge#ApiDestinationHttpMethod``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_eventbridge.errors import DeserializationError

ApiDestinationHttpMethod: TypeAlias = Literal[
    "POST",
    "GET",
    "HEAD",
    "OPTIONS",
    "PUT",
    "PATCH",
    "DELETE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "POST",
        "GET",
        "HEAD",
        "OPTIONS",
        "PUT",
        "PATCH",
        "DELETE",
    )
)


def serialize_aws_json_1_1(value: ApiDestinationHttpMethod) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ApiDestinationHttpMethod:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ApiDestinationHttpMethod value: {data!r}")
    return cast(ApiDestinationHttpMethod, data)
