"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservationTenancy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

CapacityReservationTenancy: TypeAlias = Literal[
    "default",
    "dedicated",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "default",
        "dedicated",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "default",
        "dedicated",
    )
)


def to_ec2_query_text(value: CapacityReservationTenancy) -> str:
    return value


def from_ec2_query_text(text: str) -> CapacityReservationTenancy:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown CapacityReservationTenancy value: {text!r}"
        )
    return cast(CapacityReservationTenancy, text)


def serialize_ec2_query(
    value: CapacityReservationTenancy, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> CapacityReservationTenancy:
    return from_ec2_query_text(el.text or "")
