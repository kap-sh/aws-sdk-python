"""Generated from Smithy shape ``com.amazonaws.ec2#ExcessCapacityTerminationPolicy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

ExcessCapacityTerminationPolicy: TypeAlias = Literal[
    "noTermination",
    "default",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: ExcessCapacityTerminationPolicy) -> str:
    return value


def from_ec2_query_text(text: str) -> ExcessCapacityTerminationPolicy:
    return cast(ExcessCapacityTerminationPolicy, text)


def serialize_ec2_query(
    value: ExcessCapacityTerminationPolicy, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ExcessCapacityTerminationPolicy:
    return from_ec2_query_text(el.text or "")
