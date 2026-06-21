"""Generated from Smithy shape ``com.amazonaws.autoscaling#ScalingActivityStatusCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auto_scaling._protocol.xml import Element

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
def to_query_text(value: ScalingActivityStatusCode) -> str:
    return value


def from_query_text(text: str) -> ScalingActivityStatusCode:
    return cast(ScalingActivityStatusCode, text)


def serialize_query(
    value: ScalingActivityStatusCode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ScalingActivityStatusCode:
    return from_query_text(el.text or "")
