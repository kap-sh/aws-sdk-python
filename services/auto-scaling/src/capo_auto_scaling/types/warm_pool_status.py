"""Generated from Smithy shape ``com.amazonaws.autoscaling#WarmPoolStatus``."""

from typing import Literal, TypeAlias, cast

from capo_auto_scaling._protocol.xml import Element

WarmPoolStatus: TypeAlias = Literal["PendingDelete",]


# --- awsQuery ser/de ---
def to_query_text(value: WarmPoolStatus) -> str:
    return value


def from_query_text(text: str) -> WarmPoolStatus:
    return cast(WarmPoolStatus, text)


def serialize_query(
    value: WarmPoolStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> WarmPoolStatus:
    return from_query_text(el.text or "")
