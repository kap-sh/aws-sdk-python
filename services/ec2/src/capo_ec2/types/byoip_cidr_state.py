"""Generated from Smithy shape ``com.amazonaws.ec2#ByoipCidrState``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

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
def to_ec2_query_text(value: ByoipCidrState) -> str:
    return value


def from_ec2_query_text(text: str) -> ByoipCidrState:
    return cast(ByoipCidrState, text)


def serialize_ec2_query(
    value: ByoipCidrState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ByoipCidrState:
    return from_ec2_query_text(el.text or "")
