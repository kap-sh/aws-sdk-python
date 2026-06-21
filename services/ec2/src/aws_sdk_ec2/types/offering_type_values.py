"""Generated from Smithy shape ``com.amazonaws.ec2#OfferingTypeValues``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

OfferingTypeValues: TypeAlias = Literal[
    "Heavy Utilization",
    "Medium Utilization",
    "Light Utilization",
    "No Upfront",
    "Partial Upfront",
    "All Upfront",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: OfferingTypeValues) -> str:
    return value


def from_ec2_query_text(text: str) -> OfferingTypeValues:
    return cast(OfferingTypeValues, text)


def serialize_ec2_query(
    value: OfferingTypeValues, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> OfferingTypeValues:
    return from_ec2_query_text(el.text or "")
