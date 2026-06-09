"""Generated from Smithy shape ``com.amazonaws.ec2#LockState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

LockState: TypeAlias = Literal[
    "compliance",
    "governance",
    "compliance-cooloff",
    "expired",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "compliance",
        "governance",
        "compliance-cooloff",
        "expired",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "compliance",
        "governance",
        "compliance-cooloff",
        "expired",
    )
)


def to_ec2_query_text(value: LockState) -> str:
    return value


def from_ec2_query_text(text: str) -> LockState:
    if text not in _VALUES:
        raise DeserializationError(f"unknown LockState value: {text!r}")
    return cast(LockState, text)


def serialize_ec2_query(
    value: LockState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> LockState:
    return from_ec2_query_text(el.text or "")
