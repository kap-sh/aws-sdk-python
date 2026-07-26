"""Generated from Smithy shape ``com.amazonaws.ec2#SpreadLevel``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

SpreadLevel: TypeAlias = Literal[
    "host",
    "rack",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: SpreadLevel) -> str:
    return value


def from_ec2_query_text(text: str) -> SpreadLevel:
    return cast(SpreadLevel, text)


def serialize_ec2_query(
    value: SpreadLevel, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> SpreadLevel:
    return from_ec2_query_text(el.text or "")
