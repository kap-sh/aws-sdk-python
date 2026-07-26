"""Generated from Smithy shape ``com.amazonaws.ec2#LockState``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

LockState: TypeAlias = Literal[
    "compliance",
    "governance",
    "compliance-cooloff",
    "expired",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: LockState) -> str:
    return value


def from_ec2_query_text(text: str) -> LockState:
    return cast(LockState, text)


def serialize_ec2_query(
    value: LockState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> LockState:
    return from_ec2_query_text(el.text or "")
