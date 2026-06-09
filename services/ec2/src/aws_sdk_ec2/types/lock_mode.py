"""Generated from Smithy shape ``com.amazonaws.ec2#LockMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

LockMode: TypeAlias = Literal[
    "compliance",
    "governance",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "compliance",
        "governance",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "compliance",
        "governance",
    )
)


def to_ec2_query_text(value: LockMode) -> str:
    return value


def from_ec2_query_text(text: str) -> LockMode:
    if text not in _VALUES:
        raise DeserializationError(f"unknown LockMode value: {text!r}")
    return cast(LockMode, text)


def serialize_ec2_query(
    value: LockMode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> LockMode:
    return from_ec2_query_text(el.text or "")
