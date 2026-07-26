"""Generated from Smithy shape ``com.amazonaws.autoscaling#LocalStorage``."""

from typing import Literal, TypeAlias, cast

from capo_auto_scaling._protocol.xml import Element

LocalStorage: TypeAlias = Literal[
    "included",
    "excluded",
    "required",
]


# --- awsQuery ser/de ---
def to_query_text(value: LocalStorage) -> str:
    return value


def from_query_text(text: str) -> LocalStorage:
    return cast(LocalStorage, text)


def serialize_query(
    value: LocalStorage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> LocalStorage:
    return from_query_text(el.text or "")
