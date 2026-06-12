"""Generated from Smithy shape ``com.amazonaws.autoscaling#ScalingActivityStatusCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auto_scaling._protocol.xml import Element
from aws_sdk_auto_scaling.errors import DeserializationError

ScalingActivityStatusCode: TypeAlias = Literal[
    "PendingSpotBidPlacement",
    "WaitingForSpotInstanceRequestId",
    "WaitingForSpotInstanceId",
    "WaitingForInstanceId",
    "PreInService",
    "InProgress",
    "WaitingForELBConnectionDraining",
    "MidLifecycleAction",
    "WaitingForInstanceWarmup",
    "Successful",
    "Failed",
    "Cancelled",
    "WaitingForConnectionDraining",
    "WaitingForInPlaceUpdateToStart",
    "WaitingForInPlaceUpdateToFinalize",
    "InPlaceUpdateInProgress",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PendingSpotBidPlacement",
        "WaitingForSpotInstanceRequestId",
        "WaitingForSpotInstanceId",
        "WaitingForInstanceId",
        "PreInService",
        "InProgress",
        "WaitingForELBConnectionDraining",
        "MidLifecycleAction",
        "WaitingForInstanceWarmup",
        "Successful",
        "Failed",
        "Cancelled",
        "WaitingForConnectionDraining",
        "WaitingForInPlaceUpdateToStart",
        "WaitingForInPlaceUpdateToFinalize",
        "InPlaceUpdateInProgress",
    )
)


def to_query_text(value: ScalingActivityStatusCode) -> str:
    return value


def from_query_text(text: str) -> ScalingActivityStatusCode:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ScalingActivityStatusCode value: {text!r}")
    return cast(ScalingActivityStatusCode, text)


def serialize_query(
    value: ScalingActivityStatusCode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ScalingActivityStatusCode:
    return from_query_text(el.text or "")
