"""Generated from Smithy shape ``com.amazonaws.rds#UpgradeRolloutOrder``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rds._protocol.xml import Element

UpgradeRolloutOrder: TypeAlias = Literal[
    "first",
    "second",
    "last",
]


# --- awsQuery ser/de ---
def to_query_text(value: UpgradeRolloutOrder) -> str:
    return value


def from_query_text(text: str) -> UpgradeRolloutOrder:
    return cast(UpgradeRolloutOrder, text)


def serialize_query(
    value: UpgradeRolloutOrder, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> UpgradeRolloutOrder:
    return from_query_text(el.text or "")
