"""Generated from Smithy shape ``com.amazonaws.ec2#Tenancy``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

Tenancy: TypeAlias = Literal[
    "default",
    "dedicated",
    "host",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: Tenancy) -> str:
    return value


def from_ec2_query_text(text: str) -> Tenancy:
    return cast(Tenancy, text)


def serialize_ec2_query(
    value: Tenancy, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> Tenancy:
    return from_ec2_query_text(el.text or "")
