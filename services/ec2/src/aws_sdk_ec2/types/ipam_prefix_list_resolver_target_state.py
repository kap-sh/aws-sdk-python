"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPrefixListResolverTargetState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def to_ec2_query_text(value: IpamPrefixListResolverTargetState) -> str:
    return value


def from_ec2_query_text(text: str) -> IpamPrefixListResolverTargetState:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown IpamPrefixListResolverTargetState value: {text!r}"
        )
    return cast(IpamPrefixListResolverTargetState, text)


def serialize_ec2_query(
    value: IpamPrefixListResolverTargetState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> IpamPrefixListResolverTargetState:
    return from_ec2_query_text(el.text or "")
