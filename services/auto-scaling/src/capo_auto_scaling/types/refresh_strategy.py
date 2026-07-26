"""Generated from Smithy shape ``com.amazonaws.autoscaling#RefreshStrategy``."""

from typing import Literal, TypeAlias, cast

from capo_auto_scaling._protocol.xml import Element

RefreshStrategy: TypeAlias = Literal[
    "Rolling",
    "ReplaceRootVolume",
]


# --- awsQuery ser/de ---
def to_query_text(value: RefreshStrategy) -> str:
    return value


def from_query_text(text: str) -> RefreshStrategy:
    return cast(RefreshStrategy, text)


def serialize_query(
    value: RefreshStrategy, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> RefreshStrategy:
    return from_query_text(el.text or "")
