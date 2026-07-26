"""Generated from Smithy shape ``com.amazonaws.rds#IAMAuthMode``."""

from typing import Literal, TypeAlias, cast

from capo_rds._protocol.xml import Element

IAMAuthMode: TypeAlias = Literal[
    "DISABLED",
    "REQUIRED",
    "ENABLED",
]


# --- awsQuery ser/de ---
def to_query_text(value: IAMAuthMode) -> str:
    return value


def from_query_text(text: str) -> IAMAuthMode:
    return cast(IAMAuthMode, text)


def serialize_query(
    value: IAMAuthMode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> IAMAuthMode:
    return from_query_text(el.text or "")
