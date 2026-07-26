"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPrefixListResolverTargetState``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

IpamPrefixListResolverTargetState: TypeAlias = Literal[
    "create-in-progress",
    "create-complete",
    "create-failed",
    "modify-in-progress",
    "modify-complete",
    "modify-failed",
    "sync-in-progress",
    "sync-complete",
    "sync-failed",
    "delete-in-progress",
    "delete-complete",
    "delete-failed",
    "isolate-in-progress",
    "isolate-complete",
    "restore-in-progress",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: IpamPrefixListResolverTargetState) -> str:
    return value


def from_ec2_query_text(text: str) -> IpamPrefixListResolverTargetState:
    return cast(IpamPrefixListResolverTargetState, text)


def serialize_ec2_query(
    value: IpamPrefixListResolverTargetState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> IpamPrefixListResolverTargetState:
    return from_ec2_query_text(el.text or "")
