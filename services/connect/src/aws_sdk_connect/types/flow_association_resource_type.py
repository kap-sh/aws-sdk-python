"""Generated from Smithy shape ``com.amazonaws.connect#FlowAssociationResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

FlowAssociationResourceType: TypeAlias = Literal[
    "SMS_PHONE_NUMBER",
    "INBOUND_EMAIL",
    "OUTBOUND_EMAIL",
    "ANALYTICS_CONNECTOR",
    "WHATSAPP_MESSAGING_PHONE_NUMBER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SMS_PHONE_NUMBER",
        "INBOUND_EMAIL",
        "OUTBOUND_EMAIL",
        "ANALYTICS_CONNECTOR",
        "WHATSAPP_MESSAGING_PHONE_NUMBER",
    )
)


def serialize_json(value: FlowAssociationResourceType) -> str:
    return value


def deserialize_json(data: str) -> FlowAssociationResourceType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown FlowAssociationResourceType value: {data!r}"
        )
    return cast(FlowAssociationResourceType, data)
