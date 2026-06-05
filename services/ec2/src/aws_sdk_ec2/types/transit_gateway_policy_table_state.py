"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayPolicyTableState``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

TransitGatewayPolicyTableState: TypeAlias = Literal[
    "pending",
    "available",
    "deleting",
    "deleted",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "pending",
        "available",
        "deleting",
        "deleted",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "pending",
        "available",
        "deleting",
        "deleted",
    )
)


def to_ec2_query_text(value: TransitGatewayPolicyTableState) -> str:
    return value


def from_ec2_query_text(text: str) -> TransitGatewayPolicyTableState:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown TransitGatewayPolicyTableState value: {text!r}"
        )
    return cast(TransitGatewayPolicyTableState, text)


def serialize_ec2_query(
    value: TransitGatewayPolicyTableState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> TransitGatewayPolicyTableState:
    return from_ec2_query_text(el.text or "")
