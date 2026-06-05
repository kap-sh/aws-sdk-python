"""Generated from Smithy shape ``com.amazonaws.ec2#ServiceManaged``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

ServiceManaged: TypeAlias = Literal[
    "alb",
    "nlb",
    "rnat",
    "rds",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "alb",
        "nlb",
        "rnat",
        "rds",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "alb",
        "nlb",
        "rnat",
        "rds",
    )
)


def to_ec2_query_text(value: ServiceManaged) -> str:
    return value


def from_ec2_query_text(text: str) -> ServiceManaged:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ServiceManaged value: {text!r}")
    return cast(ServiceManaged, text)


def serialize_ec2_query(
    value: ServiceManaged, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ServiceManaged:
    return from_ec2_query_text(el.text or "")
