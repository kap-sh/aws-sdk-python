"""Generated from Smithy shape ``com.amazonaws.cloudformation#DetailedStatus``."""

from typing import Literal, TypeAlias, cast

from capo_cloudformation._protocol.xml import Element

DetailedStatus: TypeAlias = Literal[
    "CONFIGURATION_COMPLETE",
    "VALIDATION_FAILED",
]


# --- awsQuery ser/de ---
def to_query_text(value: DetailedStatus) -> str:
    return value


def from_query_text(text: str) -> DetailedStatus:
    return cast(DetailedStatus, text)


def serialize_query(
    value: DetailedStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> DetailedStatus:
    return from_query_text(el.text or "")
