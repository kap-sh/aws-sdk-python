"""Generated from Smithy shape ``com.amazonaws.ec2#ServiceManaged``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

ServiceManaged: TypeAlias = Literal[
    "alb",
    "nlb",
    "rnat",
    "rds",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: ServiceManaged) -> str:
    return value


def from_ec2_query_text(text: str) -> ServiceManaged:
    return cast(ServiceManaged, text)


def serialize_ec2_query(
    value: ServiceManaged, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ServiceManaged:
    return from_ec2_query_text(el.text or "")
