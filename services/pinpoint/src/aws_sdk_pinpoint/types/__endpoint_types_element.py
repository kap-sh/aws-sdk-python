"""Generated from Smithy shape ``com.amazonaws.pinpoint#__EndpointTypesElement``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: __EndpointTypesElement) -> str:
    return value


def deserialize_json(data: str) -> __EndpointTypesElement:
    return cast(__EndpointTypesElement, data)
