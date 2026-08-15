"""Generated from Smithy shape ``com.amazonaws.ec2#AllocationType``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

AllocationType: TypeAlias = Literal[
    "used",
    "future",
    "cancelling",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: AllocationType) -> str:
    return value


def from_ec2_query_text(text: str) -> AllocationType:
    return cast(AllocationType, text)


def serialize_ec2_query(
    value: AllocationType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> AllocationType:
    return from_ec2_query_text(el.text or "")
