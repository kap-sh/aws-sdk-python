"""Generated from Smithy shape ``com.amazonaws.ec2#ExcessCapacityTerminationPolicy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

ExcessCapacityTerminationPolicy: TypeAlias = Literal[
    "noTermination",
    "default",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "noTermination",
        "default",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "noTermination",
        "default",
    )
)


def to_ec2_query_text(value: ExcessCapacityTerminationPolicy) -> str:
    return value


def from_ec2_query_text(text: str) -> ExcessCapacityTerminationPolicy:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown ExcessCapacityTerminationPolicy value: {text!r}"
        )
    return cast(ExcessCapacityTerminationPolicy, text)


def serialize_ec2_query(
    value: ExcessCapacityTerminationPolicy, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ExcessCapacityTerminationPolicy:
    return from_ec2_query_text(el.text or "")
