"""Generated from Smithy shape ``com.amazonaws.rds#TargetHealthReason``."""

from typing import Literal, TypeAlias, cast

from capo_rds._protocol.xml import Element

TargetHealthReason: TypeAlias = Literal[
    "UNREACHABLE",
    "CONNECTION_FAILED",
    "AUTH_FAILURE",
    "PENDING_PROXY_CAPACITY",
    "INVALID_REPLICATION_STATE",
    "PROMOTED",
]


# --- awsQuery ser/de ---
def to_query_text(value: TargetHealthReason) -> str:
    return value


def from_query_text(text: str) -> TargetHealthReason:
    return cast(TargetHealthReason, text)


def serialize_query(
    value: TargetHealthReason, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> TargetHealthReason:
    return from_query_text(el.text or "")
