"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessLogDeliveryStatusCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

VerifiedAccessLogDeliveryStatusCode: TypeAlias = Literal[
    "success",
    "failed",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "success",
        "failed",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "success",
        "failed",
    )
)


def to_ec2_query_text(value: VerifiedAccessLogDeliveryStatusCode) -> str:
    return value


def from_ec2_query_text(text: str) -> VerifiedAccessLogDeliveryStatusCode:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown VerifiedAccessLogDeliveryStatusCode value: {text!r}"
        )
    return cast(VerifiedAccessLogDeliveryStatusCode, text)


def serialize_ec2_query(
    value: VerifiedAccessLogDeliveryStatusCode,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> VerifiedAccessLogDeliveryStatusCode:
    return from_ec2_query_text(el.text or "")
