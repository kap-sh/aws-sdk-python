"""Generated from Smithy shape ``com.amazonaws.ec2#AggregationStatusEnum``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

AggregationStatusEnum: TypeAlias = Literal[
    "included",
    "excluded",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: AggregationStatusEnum) -> str:
    return value


def from_ec2_query_text(text: str) -> AggregationStatusEnum:
    return cast(AggregationStatusEnum, text)


def serialize_ec2_query(
    value: AggregationStatusEnum, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> AggregationStatusEnum:
    return from_ec2_query_text(el.text or "")
