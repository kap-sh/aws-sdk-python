"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPoolCidrState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

IpamPoolCidrState: TypeAlias = Literal[
    "pending-provision",
    "provisioned",
    "failed-provision",
    "pending-deprovision",
    "deprovisioned",
    "failed-deprovision",
    "pending-import",
    "failed-import",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "pending-provision",
        "provisioned",
        "failed-provision",
        "pending-deprovision",
        "deprovisioned",
        "failed-deprovision",
        "pending-import",
        "failed-import",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "pending-provision",
        "provisioned",
        "failed-provision",
        "pending-deprovision",
        "deprovisioned",
        "failed-deprovision",
        "pending-import",
        "failed-import",
    )
)


def to_ec2_query_text(value: IpamPoolCidrState) -> str:
    return value


def from_ec2_query_text(text: str) -> IpamPoolCidrState:
    if text not in _VALUES:
        raise DeserializationError(f"unknown IpamPoolCidrState value: {text!r}")
    return cast(IpamPoolCidrState, text)


def serialize_ec2_query(
    value: IpamPoolCidrState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> IpamPoolCidrState:
    return from_ec2_query_text(el.text or "")
