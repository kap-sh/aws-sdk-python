"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#CapacityReservationStateEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

CapacityReservationStateEnum: TypeAlias = Literal[
    "provisioned",
    "pending",
    "rebalancing",
    "failed",
]


# --- awsQuery ser/de ---
def to_query_text(value: CapacityReservationStateEnum) -> str:
    return value


def from_query_text(text: str) -> CapacityReservationStateEnum:
    return cast(CapacityReservationStateEnum, text)


def serialize_query(
    value: CapacityReservationStateEnum, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> CapacityReservationStateEnum:
    return from_query_text(el.text or "")
