"""Generated from Smithy shape ``com.amazonaws.ec2#IpamByoipCidrState``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

"""<p>The state of a BYOIP CIDR.</p>"""
IpamByoipCidrState: TypeAlias = Literal[
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
def to_ec2_query_text(value: IpamByoipCidrState) -> str:
    return value


def from_ec2_query_text(text: str) -> IpamByoipCidrState:
    return cast(IpamByoipCidrState, text)


def serialize_ec2_query(
    value: IpamByoipCidrState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> IpamByoipCidrState:
    return from_ec2_query_text(el.text or "")
