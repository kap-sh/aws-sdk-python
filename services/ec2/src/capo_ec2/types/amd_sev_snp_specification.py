"""Generated from Smithy shape ``com.amazonaws.ec2#AmdSevSnpSpecification``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

AmdSevSnpSpecification: TypeAlias = Literal[
    "enabled",
    "disabled",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: AmdSevSnpSpecification) -> str:
    return value


def from_ec2_query_text(text: str) -> AmdSevSnpSpecification:
    return cast(AmdSevSnpSpecification, text)


def serialize_ec2_query(
    value: AmdSevSnpSpecification, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> AmdSevSnpSpecification:
    return from_ec2_query_text(el.text or "")
