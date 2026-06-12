"""Generated from Smithy shape ``com.amazonaws.connect#ListFlowAssociationResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

ListFlowAssociationResourceType: TypeAlias = Literal[
    "WHATSAPP_MESSAGING_PHONE_NUMBER",
    "VOICE_PHONE_NUMBER",
    "INBOUND_EMAIL",
    "OUTBOUND_EMAIL",
    "ANALYTICS_CONNECTOR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "WHATSAPP_MESSAGING_PHONE_NUMBER",
        "VOICE_PHONE_NUMBER",
        "INBOUND_EMAIL",
        "OUTBOUND_EMAIL",
        "ANALYTICS_CONNECTOR",
    )
)


def serialize_json(value: ListFlowAssociationResourceType) -> str:
    return value


def deserialize_json(data: str) -> ListFlowAssociationResourceType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ListFlowAssociationResourceType value: {data!r}"
        )
    return cast(ListFlowAssociationResourceType, data)
