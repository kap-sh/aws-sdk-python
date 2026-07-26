"""Generated from Smithy shape ``com.amazonaws.autoscaling#LocalStorageType``."""

from typing import Literal, TypeAlias, cast

from capo_auto_scaling._protocol.xml import Element

LocalStorageType: TypeAlias = Literal[
    "hdd",
    "ssd",
]


# --- awsQuery ser/de ---
def to_query_text(value: LocalStorageType) -> str:
    return value


def from_query_text(text: str) -> LocalStorageType:
    return cast(LocalStorageType, text)


def serialize_query(
    value: LocalStorageType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> LocalStorageType:
    return from_query_text(el.text or "")
