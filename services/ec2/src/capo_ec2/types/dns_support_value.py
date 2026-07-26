"""Generated from Smithy shape ``com.amazonaws.ec2#DnsSupportValue``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

DnsSupportValue: TypeAlias = Literal[
    "enable",
    "disable",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: DnsSupportValue) -> str:
    return value


def from_ec2_query_text(text: str) -> DnsSupportValue:
    return cast(DnsSupportValue, text)


def serialize_ec2_query(
    value: DnsSupportValue, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> DnsSupportValue:
    return from_ec2_query_text(el.text or "")
