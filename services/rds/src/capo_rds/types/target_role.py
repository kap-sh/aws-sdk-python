"""Generated from Smithy shape ``com.amazonaws.rds#TargetRole``."""

from typing import Literal, TypeAlias, cast

from capo_rds._protocol.xml import Element

TargetRole: TypeAlias = Literal[
    "READ_WRITE",
    "READ_ONLY",
    "UNKNOWN",
]


# --- awsQuery ser/de ---
def to_query_text(value: TargetRole) -> str:
    return value


def from_query_text(text: str) -> TargetRole:
    return cast(TargetRole, text)


def serialize_query(
    value: TargetRole, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> TargetRole:
    return from_query_text(el.text or "")
