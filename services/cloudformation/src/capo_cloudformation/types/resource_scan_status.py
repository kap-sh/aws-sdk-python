"""Generated from Smithy shape ``com.amazonaws.cloudformation#ResourceScanStatus``."""

from typing import Literal, TypeAlias, cast

from capo_cloudformation._protocol.xml import Element

ResourceScanStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "FAILED",
    "COMPLETE",
    "EXPIRED",
]


# --- awsQuery ser/de ---
def to_query_text(value: ResourceScanStatus) -> str:
    return value


def from_query_text(text: str) -> ResourceScanStatus:
    return cast(ResourceScanStatus, text)


def serialize_query(
    value: ResourceScanStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ResourceScanStatus:
    return from_query_text(el.text or "")
