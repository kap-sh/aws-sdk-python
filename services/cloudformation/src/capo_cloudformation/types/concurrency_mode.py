"""Generated from Smithy shape ``com.amazonaws.cloudformation#ConcurrencyMode``."""

from typing import Literal, TypeAlias, cast

from capo_cloudformation._protocol.xml import Element

ConcurrencyMode: TypeAlias = Literal[
    "STRICT_FAILURE_TOLERANCE",
    "SOFT_FAILURE_TOLERANCE",
]


# --- awsQuery ser/de ---
def to_query_text(value: ConcurrencyMode) -> str:
    return value


def from_query_text(text: str) -> ConcurrencyMode:
    return cast(ConcurrencyMode, text)


def serialize_query(
    value: ConcurrencyMode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ConcurrencyMode:
    return from_query_text(el.text or "")
