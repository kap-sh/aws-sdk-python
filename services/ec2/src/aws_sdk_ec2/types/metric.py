"""Generated from Smithy shape ``com.amazonaws.ec2#Metric``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

Metric: TypeAlias = Literal[
    "reservation-total-capacity-hrs-vcpu",
    "reservation-total-capacity-hrs-inst",
    "reservation-max-size-vcpu",
    "reservation-max-size-inst",
    "reservation-min-size-vcpu",
    "reservation-min-size-inst",
    "reservation-unused-total-capacity-hrs-vcpu",
    "reservation-unused-total-capacity-hrs-inst",
    "reservation-unused-total-estimated-cost",
    "reservation-max-unused-size-vcpu",
    "reservation-max-unused-size-inst",
    "reservation-min-unused-size-vcpu",
    "reservation-min-unused-size-inst",
    "reservation-max-utilization",
    "reservation-min-utilization",
    "reservation-avg-utilization-vcpu",
    "reservation-avg-utilization-inst",
    "reservation-total-count",
    "reservation-total-estimated-cost",
    "reservation-avg-future-size-vcpu",
    "reservation-avg-future-size-inst",
    "reservation-min-future-size-vcpu",
    "reservation-min-future-size-inst",
    "reservation-max-future-size-vcpu",
    "reservation-max-future-size-inst",
    "reservation-avg-committed-size-vcpu",
    "reservation-avg-committed-size-inst",
    "reservation-max-committed-size-vcpu",
    "reservation-max-committed-size-inst",
    "reservation-min-committed-size-vcpu",
    "reservation-min-committed-size-inst",
    "reserved-total-usage-hrs-vcpu",
    "reserved-total-usage-hrs-inst",
    "reserved-total-estimated-cost",
    "unreserved-total-usage-hrs-vcpu",
    "unreserved-total-usage-hrs-inst",
    "unreserved-total-estimated-cost",
    "spot-total-usage-hrs-vcpu",
    "spot-total-usage-hrs-inst",
    "spot-total-estimated-cost",
    "spot-avg-run-time-before-interruption-inst",
    "spot-max-run-time-before-interruption-inst",
    "spot-min-run-time-before-interruption-inst",
    "spot-total-interruptions-inst",
    "spot-total-interruptions-vcpu",
    "spot-total-count-inst",
    "spot-total-count-vcpu",
    "spot-interruption-rate-inst",
    "spot-interruption-rate-vcpu",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "reservation-total-capacity-hrs-vcpu",
        "reservation-total-capacity-hrs-inst",
        "reservation-max-size-vcpu",
        "reservation-max-size-inst",
        "reservation-min-size-vcpu",
        "reservation-min-size-inst",
        "reservation-unused-total-capacity-hrs-vcpu",
        "reservation-unused-total-capacity-hrs-inst",
        "reservation-unused-total-estimated-cost",
        "reservation-max-unused-size-vcpu",
        "reservation-max-unused-size-inst",
        "reservation-min-unused-size-vcpu",
        "reservation-min-unused-size-inst",
        "reservation-max-utilization",
        "reservation-min-utilization",
        "reservation-avg-utilization-vcpu",
        "reservation-avg-utilization-inst",
        "reservation-total-count",
        "reservation-total-estimated-cost",
        "reservation-avg-future-size-vcpu",
        "reservation-avg-future-size-inst",
        "reservation-min-future-size-vcpu",
        "reservation-min-future-size-inst",
        "reservation-max-future-size-vcpu",
        "reservation-max-future-size-inst",
        "reservation-avg-committed-size-vcpu",
        "reservation-avg-committed-size-inst",
        "reservation-max-committed-size-vcpu",
        "reservation-max-committed-size-inst",
        "reservation-min-committed-size-vcpu",
        "reservation-min-committed-size-inst",
        "reserved-total-usage-hrs-vcpu",
        "reserved-total-usage-hrs-inst",
        "reserved-total-estimated-cost",
        "unreserved-total-usage-hrs-vcpu",
        "unreserved-total-usage-hrs-inst",
        "unreserved-total-estimated-cost",
        "spot-total-usage-hrs-vcpu",
        "spot-total-usage-hrs-inst",
        "spot-total-estimated-cost",
        "spot-avg-run-time-before-interruption-inst",
        "spot-max-run-time-before-interruption-inst",
        "spot-min-run-time-before-interruption-inst",
        "spot-total-interruptions-inst",
        "spot-total-interruptions-vcpu",
        "spot-total-count-inst",
        "spot-total-count-vcpu",
        "spot-interruption-rate-inst",
        "spot-interruption-rate-vcpu",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "reservation-total-capacity-hrs-vcpu",
        "reservation-total-capacity-hrs-inst",
        "reservation-max-size-vcpu",
        "reservation-max-size-inst",
        "reservation-min-size-vcpu",
        "reservation-min-size-inst",
        "reservation-unused-total-capacity-hrs-vcpu",
        "reservation-unused-total-capacity-hrs-inst",
        "reservation-unused-total-estimated-cost",
        "reservation-max-unused-size-vcpu",
        "reservation-max-unused-size-inst",
        "reservation-min-unused-size-vcpu",
        "reservation-min-unused-size-inst",
        "reservation-max-utilization",
        "reservation-min-utilization",
        "reservation-avg-utilization-vcpu",
        "reservation-avg-utilization-inst",
        "reservation-total-count",
        "reservation-total-estimated-cost",
        "reservation-avg-future-size-vcpu",
        "reservation-avg-future-size-inst",
        "reservation-min-future-size-vcpu",
        "reservation-min-future-size-inst",
        "reservation-max-future-size-vcpu",
        "reservation-max-future-size-inst",
        "reservation-avg-committed-size-vcpu",
        "reservation-avg-committed-size-inst",
        "reservation-max-committed-size-vcpu",
        "reservation-max-committed-size-inst",
        "reservation-min-committed-size-vcpu",
        "reservation-min-committed-size-inst",
        "reserved-total-usage-hrs-vcpu",
        "reserved-total-usage-hrs-inst",
        "reserved-total-estimated-cost",
        "unreserved-total-usage-hrs-vcpu",
        "unreserved-total-usage-hrs-inst",
        "unreserved-total-estimated-cost",
        "spot-total-usage-hrs-vcpu",
        "spot-total-usage-hrs-inst",
        "spot-total-estimated-cost",
        "spot-avg-run-time-before-interruption-inst",
        "spot-max-run-time-before-interruption-inst",
        "spot-min-run-time-before-interruption-inst",
        "spot-total-interruptions-inst",
        "spot-total-interruptions-vcpu",
        "spot-total-count-inst",
        "spot-total-count-vcpu",
        "spot-interruption-rate-inst",
        "spot-interruption-rate-vcpu",
    )
)


def to_ec2_query_text(value: Metric) -> str:
    return value


def from_ec2_query_text(text: str) -> Metric:
    if text not in _VALUES:
        raise DeserializationError(f"unknown Metric value: {text!r}")
    return cast(Metric, text)


def serialize_ec2_query(
    value: Metric, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> Metric:
    return from_ec2_query_text(el.text or "")
