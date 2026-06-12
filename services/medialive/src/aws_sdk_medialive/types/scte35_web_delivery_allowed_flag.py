"""Generated from Smithy shape ``com.amazonaws.medialive#Scte35WebDeliveryAllowedFlag``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Corresponds to the web_delivery_allowed_flag parameter. A value of WEB_DELIVERY_NOT_ALLOWED corresponds to 0 (false) in the SCTE-35 specification. If you include one of the \"restriction\" flags then you must include all four of them."""
Scte35WebDeliveryAllowedFlag: TypeAlias = Literal[
    "WEB_DELIVERY_NOT_ALLOWED",
    "WEB_DELIVERY_ALLOWED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "WEB_DELIVERY_NOT_ALLOWED",
        "WEB_DELIVERY_ALLOWED",
    )
)


def serialize_json(value: Scte35WebDeliveryAllowedFlag) -> str:
    return value


def deserialize_json(data: str) -> Scte35WebDeliveryAllowedFlag:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown Scte35WebDeliveryAllowedFlag value: {data!r}"
        )
    return cast(Scte35WebDeliveryAllowedFlag, data)
