"""Generated from Smithy shape ``com.amazonaws.autoscaling#DeletionProtection``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auto_scaling._protocol.xml import Element

DeletionProtection: TypeAlias = Literal[
    "none",
    "prevent-force-deletion",
    "prevent-all-deletion",
]


# --- awsQuery ser/de ---
def to_query_text(value: DeletionProtection) -> str:
    return value


def from_query_text(text: str) -> DeletionProtection:
    return cast(DeletionProtection, text)


def serialize_query(
    value: DeletionProtection, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> DeletionProtection:
    return from_query_text(el.text or "")
