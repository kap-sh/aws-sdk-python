"""Generated from Smithy shape ``com.amazonaws.connect#EndpointType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

EndpointType: TypeAlias = Literal[
    "TELEPHONE_NUMBER",
    "VOIP",
    "CONTACT_FLOW",
    "CONNECT_PHONENUMBER_ARN",
    "EMAIL_ADDRESS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TELEPHONE_NUMBER",
        "VOIP",
        "CONTACT_FLOW",
        "CONNECT_PHONENUMBER_ARN",
        "EMAIL_ADDRESS",
    )
)


def serialize_json(value: EndpointType) -> str:
    return value


def deserialize_json(data: str) -> EndpointType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EndpointType value: {data!r}")
    return cast(EndpointType, data)
