"""Generated from Smithy shape ``com.amazonaws.ec2#UnlimitedSupportedInstanceFamily``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

UnlimitedSupportedInstanceFamily: TypeAlias = Literal[
    "t2",
    "t3",
    "t3a",
    "t4g",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: UnlimitedSupportedInstanceFamily) -> str:
    return value


def from_ec2_query_text(text: str) -> UnlimitedSupportedInstanceFamily:
    return cast(UnlimitedSupportedInstanceFamily, text)


def serialize_ec2_query(
    value: UnlimitedSupportedInstanceFamily, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> UnlimitedSupportedInstanceFamily:
    return from_ec2_query_text(el.text or "")
