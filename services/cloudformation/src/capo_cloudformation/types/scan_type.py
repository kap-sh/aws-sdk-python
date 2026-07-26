"""Generated from Smithy shape ``com.amazonaws.cloudformation#ScanType``."""

from typing import Literal, TypeAlias, cast

from capo_cloudformation._protocol.xml import Element

ScanType: TypeAlias = Literal[
    "FULL",
    "PARTIAL",
]


# --- awsQuery ser/de ---
def to_query_text(value: ScanType) -> str:
    return value


def from_query_text(text: str) -> ScanType:
    return cast(ScanType, text)


def serialize_query(value: ScanType, pairs: list[tuple[str, str]], prefix: str) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ScanType:
    return from_query_text(el.text or "")
