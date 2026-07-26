"""Generated from Smithy shape ``com.amazonaws.ec2#EphemeralNvmeSupport``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

EphemeralNvmeSupport: TypeAlias = Literal[
    "unsupported",
    "supported",
    "required",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: EphemeralNvmeSupport) -> str:
    return value


def from_ec2_query_text(text: str) -> EphemeralNvmeSupport:
    return cast(EphemeralNvmeSupport, text)


def serialize_ec2_query(
    value: EphemeralNvmeSupport, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> EphemeralNvmeSupport:
    return from_ec2_query_text(el.text or "")
