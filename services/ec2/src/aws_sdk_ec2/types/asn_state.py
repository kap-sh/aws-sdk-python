"""Generated from Smithy shape ``com.amazonaws.ec2#AsnState``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

AsnState: TypeAlias = Literal[
    "deprovisioned",
    "failed-deprovision",
    "failed-provision",
    "pending-deprovision",
    "pending-provision",
    "provisioned",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "deprovisioned",
        "failed-deprovision",
        "failed-provision",
        "pending-deprovision",
        "pending-provision",
        "provisioned",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "deprovisioned",
        "failed-deprovision",
        "failed-provision",
        "pending-deprovision",
        "pending-provision",
        "provisioned",
    )
)


def to_ec2_query_text(value: AsnState) -> str:
    return value


def from_ec2_query_text(text: str) -> AsnState:
    if text not in _VALUES:
        raise DeserializationError(f"unknown AsnState value: {text!r}")
    return cast(AsnState, text)


def serialize_ec2_query(
    value: AsnState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> AsnState:
    return from_ec2_query_text(el.text or "")
