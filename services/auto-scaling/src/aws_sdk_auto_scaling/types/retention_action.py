"""Generated from Smithy shape ``com.amazonaws.autoscaling#RetentionAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auto_scaling._protocol.xml import Element

RetentionAction: TypeAlias = Literal[
    "retain",
    "terminate",
]


# --- awsQuery ser/de ---
def to_query_text(value: RetentionAction) -> str:
    return value


def from_query_text(text: str) -> RetentionAction:
    return cast(RetentionAction, text)


def serialize_query(
    value: RetentionAction, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> RetentionAction:
    return from_query_text(el.text or "")
