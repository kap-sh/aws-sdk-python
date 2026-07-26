"""Generated from Smithy shape ``com.amazonaws.ec2#NitroEnclavesSupport``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

NitroEnclavesSupport: TypeAlias = Literal[
    "unsupported",
    "supported",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: NitroEnclavesSupport) -> str:
    return value


def from_ec2_query_text(text: str) -> NitroEnclavesSupport:
    return cast(NitroEnclavesSupport, text)


def serialize_ec2_query(
    value: NitroEnclavesSupport, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> NitroEnclavesSupport:
    return from_ec2_query_text(el.text or "")
