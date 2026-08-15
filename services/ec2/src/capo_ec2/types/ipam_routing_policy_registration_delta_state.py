"""Generated from Smithy shape ``com.amazonaws.ec2#IpamRoutingPolicyRegistrationDeltaState``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

"""<p>The state of a routing policy registration delta.</p>"""
IpamRoutingPolicyRegistrationDeltaState: TypeAlias = Literal[
    "pending",
    "published",
    "failed",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: IpamRoutingPolicyRegistrationDeltaState) -> str:
    return value


def from_ec2_query_text(text: str) -> IpamRoutingPolicyRegistrationDeltaState:
    return cast(IpamRoutingPolicyRegistrationDeltaState, text)


def serialize_ec2_query(
    value: IpamRoutingPolicyRegistrationDeltaState,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> IpamRoutingPolicyRegistrationDeltaState:
    return from_ec2_query_text(el.text or "")
