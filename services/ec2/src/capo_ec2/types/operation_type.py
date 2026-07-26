"""Generated from Smithy shape ``com.amazonaws.ec2#OperationType``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

OperationType: TypeAlias = Literal[
    "add",
    "remove",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: OperationType) -> str:
    return value


def from_ec2_query_text(text: str) -> OperationType:
    return cast(OperationType, text)


def serialize_ec2_query(
    value: OperationType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> OperationType:
    return from_ec2_query_text(el.text or "")
