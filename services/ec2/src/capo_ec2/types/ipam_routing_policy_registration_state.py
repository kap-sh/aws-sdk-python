"""Generated from Smithy shape ``com.amazonaws.ec2#IpamRoutingPolicyRegistrationState``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

"""<p>The state of a routing policy registration.</p>"""
IpamRoutingPolicyRegistrationState: TypeAlias = Literal[
    "pending-activate",
    "activate-failed",
    "create-in-progress",
    "create-complete",
    "update-in-progress",
    "update-complete",
    "delete-in-progress",
    "delete-complete",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: IpamRoutingPolicyRegistrationState) -> str:
    return value


def from_ec2_query_text(text: str) -> IpamRoutingPolicyRegistrationState:
    return cast(IpamRoutingPolicyRegistrationState, text)


def serialize_ec2_query(
    value: IpamRoutingPolicyRegistrationState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> IpamRoutingPolicyRegistrationState:
    return from_ec2_query_text(el.text or "")
