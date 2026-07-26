"""Generated from Smithy shape ``com.amazonaws.rds#FailoverStatus``."""

from typing import Literal, TypeAlias, cast

from capo_rds._protocol.xml import Element

FailoverStatus: TypeAlias = Literal[
    "pending",
    "failing-over",
    "cancelling",
]


# --- awsQuery ser/de ---
def to_query_text(value: FailoverStatus) -> str:
    return value


def from_query_text(text: str) -> FailoverStatus:
    return cast(FailoverStatus, text)


def serialize_query(
    value: FailoverStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> FailoverStatus:
    return from_query_text(el.text or "")
