"""Generated from Smithy shape ``com.amazonaws.pinpoint#__EndpointTypesElement``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pinpoint.errors import DeserializationError

__EndpointTypesElement: TypeAlias = Literal[
    "PUSH",
    "GCM",
    "APNS",
    "APNS_SANDBOX",
    "APNS_VOIP",
    "APNS_VOIP_SANDBOX",
    "ADM",
    "SMS",
    "VOICE",
    "EMAIL",
    "BAIDU",
    "CUSTOM",
    "IN_APP",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PUSH",
        "GCM",
        "APNS",
        "APNS_SANDBOX",
        "APNS_VOIP",
        "APNS_VOIP_SANDBOX",
        "ADM",
        "SMS",
        "VOICE",
        "EMAIL",
        "BAIDU",
        "CUSTOM",
        "IN_APP",
    )
)


def serialize_json(value: __EndpointTypesElement) -> str:
    return value


def deserialize_json(data: str) -> __EndpointTypesElement:
    if data not in _VALUES:
        raise DeserializationError(f"unknown __EndpointTypesElement value: {data!r}")
    return cast(__EndpointTypesElement, data)
