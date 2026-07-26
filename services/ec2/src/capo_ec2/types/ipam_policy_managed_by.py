"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPolicyManagedBy``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

IpamPolicyManagedBy: TypeAlias = Literal[
    "account",
    "delegated-administrator-for-ipam",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: IpamPolicyManagedBy) -> str:
    return value


def from_ec2_query_text(text: str) -> IpamPolicyManagedBy:
    return cast(IpamPolicyManagedBy, text)


def serialize_ec2_query(
    value: IpamPolicyManagedBy, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> IpamPolicyManagedBy:
    return from_ec2_query_text(el.text or "")
