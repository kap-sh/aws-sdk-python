"""Generated from Smithy shape ``com.amazonaws.cloudformation#BeaconStackOperationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element

BeaconStackOperationStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "SUCCEEDED",
    "FAILED",
]


# --- awsQuery ser/de ---
def to_query_text(value: BeaconStackOperationStatus) -> str:
    return value


def from_query_text(text: str) -> BeaconStackOperationStatus:
    return cast(BeaconStackOperationStatus, text)


def serialize_query(
    value: BeaconStackOperationStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> BeaconStackOperationStatus:
    return from_query_text(el.text or "")
