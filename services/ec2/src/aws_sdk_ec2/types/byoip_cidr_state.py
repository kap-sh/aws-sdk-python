"""Generated from Smithy shape ``com.amazonaws.ec2#ByoipCidrState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

ByoipCidrState: TypeAlias = Literal[
    "advertised",
    "deprovisioned",
    "failed-deprovision",
    "failed-provision",
    "pending-advertising",
    "pending-deprovision",
    "pending-provision",
    "pending-withdrawal",
    "provisioned",
    "provisioned-not-publicly-advertisable",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "advertised",
        "deprovisioned",
        "failed-deprovision",
        "failed-provision",
        "pending-advertising",
        "pending-deprovision",
        "pending-provision",
        "pending-withdrawal",
        "provisioned",
        "provisioned-not-publicly-advertisable",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "advertised",
        "deprovisioned",
        "failed-deprovision",
        "failed-provision",
        "pending-advertising",
        "pending-deprovision",
        "pending-provision",
        "pending-withdrawal",
        "provisioned",
        "provisioned-not-publicly-advertisable",
    )
)


def to_ec2_query_text(value: ByoipCidrState) -> str:
    return value


def from_ec2_query_text(text: str) -> ByoipCidrState:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ByoipCidrState value: {text!r}")
    return cast(ByoipCidrState, text)


def serialize_ec2_query(
    value: ByoipCidrState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ByoipCidrState:
    return from_ec2_query_text(el.text or "")
