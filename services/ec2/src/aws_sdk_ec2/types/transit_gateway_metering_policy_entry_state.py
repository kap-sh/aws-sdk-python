"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayMeteringPolicyEntryState``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

TransitGatewayMeteringPolicyEntryState: TypeAlias = Literal[
    "available",
    "deleted",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "available",
        "deleted",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "available",
        "deleted",
    )
)


def to_ec2_query_text(value: TransitGatewayMeteringPolicyEntryState) -> str:
    return value


def from_ec2_query_text(text: str) -> TransitGatewayMeteringPolicyEntryState:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown TransitGatewayMeteringPolicyEntryState value: {text!r}"
        )
    return cast(TransitGatewayMeteringPolicyEntryState, text)


def serialize_ec2_query(
    value: TransitGatewayMeteringPolicyEntryState,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> TransitGatewayMeteringPolicyEntryState:
    return from_ec2_query_text(el.text or "")
