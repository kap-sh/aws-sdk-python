"""Generated from Smithy shape ``com.amazonaws.ec2#HostTenancy``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

HostTenancy: TypeAlias = Literal[
    "default",
    "dedicated",
    "host",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: HostTenancy) -> str:
    return value


def from_ec2_query_text(text: str) -> HostTenancy:
    return cast(HostTenancy, text)


def serialize_ec2_query(
    value: HostTenancy, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> HostTenancy:
    return from_ec2_query_text(el.text or "")
