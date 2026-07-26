"""Generated from Smithy shape ``com.amazonaws.elasticache#PendingAutomaticFailoverStatus``."""

from typing import Literal, TypeAlias, cast

from capo_elasticache._protocol.xml import Element

PendingAutomaticFailoverStatus: TypeAlias = Literal[
    "enabled",
    "disabled",
]


# --- awsQuery ser/de ---
def to_query_text(value: PendingAutomaticFailoverStatus) -> str:
    return value


def from_query_text(text: str) -> PendingAutomaticFailoverStatus:
    return cast(PendingAutomaticFailoverStatus, text)


def serialize_query(
    value: PendingAutomaticFailoverStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> PendingAutomaticFailoverStatus:
    return from_query_text(el.text or "")
