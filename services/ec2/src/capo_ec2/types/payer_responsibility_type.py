"""Generated from Smithy shape ``com.amazonaws.ec2#PayerResponsibilityType``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

PayerResponsibilityType: TypeAlias = Literal[
    "vpc-endpoint-account",
    "vpc-endpoint-service-account",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: PayerResponsibilityType) -> str:
    return value


def from_ec2_query_text(text: str) -> PayerResponsibilityType:
    return cast(PayerResponsibilityType, text)


def serialize_ec2_query(
    value: PayerResponsibilityType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> PayerResponsibilityType:
    return from_ec2_query_text(el.text or "")
