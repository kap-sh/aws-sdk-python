"""Generated from Smithy shape ``com.amazonaws.autoscaling#LifecycleState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auto_scaling._protocol.xml import Element

LifecycleState: TypeAlias = Literal[
    "Pending",
    "Pending:Wait",
    "Pending:Proceed",
    "Quarantined",
    "InService",
    "Terminating",
    "Terminating:Wait",
    "Terminating:Proceed",
    "Terminating:Retained",
    "Terminated",
    "Detaching",
    "Detached",
    "EnteringStandby",
    "Standby",
    "ReplacingRootVolume",
    "ReplacingRootVolume:Wait",
    "ReplacingRootVolume:Proceed",
    "RootVolumeReplaced",
    "Warmed:Pending",
    "Warmed:Pending:Wait",
    "Warmed:Pending:Proceed",
    "Warmed:Pending:Retained",
    "Warmed:Terminating",
    "Warmed:Terminating:Wait",
    "Warmed:Terminating:Proceed",
    "Warmed:Terminating:Retained",
    "Warmed:Terminated",
    "Warmed:Stopped",
    "Warmed:Running",
    "Warmed:Hibernated",
]


# --- awsQuery ser/de ---
def to_query_text(value: LifecycleState) -> str:
    return value


def from_query_text(text: str) -> LifecycleState:
    return cast(LifecycleState, text)


def serialize_query(
    value: LifecycleState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> LifecycleState:
    return from_query_text(el.text or "")
