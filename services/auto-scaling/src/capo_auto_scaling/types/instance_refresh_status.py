"""Generated from Smithy shape ``com.amazonaws.autoscaling#InstanceRefreshStatus``."""

from typing import Literal, TypeAlias, cast

from capo_auto_scaling._protocol.xml import Element

InstanceRefreshStatus: TypeAlias = Literal[
    "Pending",
    "InProgress",
    "Successful",
    "Failed",
    "Cancelling",
    "Cancelled",
    "RollbackInProgress",
    "RollbackFailed",
    "RollbackSuccessful",
    "Baking",
]


# --- awsQuery ser/de ---
def to_query_text(value: InstanceRefreshStatus) -> str:
    return value


def from_query_text(text: str) -> InstanceRefreshStatus:
    return cast(InstanceRefreshStatus, text)


def serialize_query(
    value: InstanceRefreshStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> InstanceRefreshStatus:
    return from_query_text(el.text or "")
