"""Generated from Smithy shape ``com.amazonaws.rds#LifecycleSupportName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rds._protocol.xml import Element

LifecycleSupportName: TypeAlias = Literal[
    "open-source-rds-standard-support",
    "open-source-rds-extended-support",
]


# --- awsQuery ser/de ---
def to_query_text(value: LifecycleSupportName) -> str:
    return value


def from_query_text(text: str) -> LifecycleSupportName:
    return cast(LifecycleSupportName, text)


def serialize_query(
    value: LifecycleSupportName, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> LifecycleSupportName:
    return from_query_text(el.text or "")
