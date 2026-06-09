"""Generated from Smithy shape ``com.amazonaws.ec2#IpamState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

IpamState: TypeAlias = Literal[
    "create-in-progress",
    "create-complete",
    "create-failed",
    "modify-in-progress",
    "modify-complete",
    "modify-failed",
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
        "delete-in-progress",
        "delete-complete",
        "delete-failed",
        "isolate-in-progress",
        "isolate-complete",
        "restore-in-progress",
    )
)


def to_ec2_query_text(value: IpamState) -> str:
    return value


def from_ec2_query_text(text: str) -> IpamState:
    if text not in _VALUES:
        raise DeserializationError(f"unknown IpamState value: {text!r}")
    return cast(IpamState, text)


def serialize_ec2_query(
    value: IpamState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> IpamState:
    return from_ec2_query_text(el.text or "")
