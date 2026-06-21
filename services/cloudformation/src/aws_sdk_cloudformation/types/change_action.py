"""Generated from Smithy shape ``com.amazonaws.cloudformation#ChangeAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element

ChangeAction: TypeAlias = Literal[
    "Add",
    "Modify",
    "Remove",
    "Import",
    "Dynamic",
    "SyncWithActual",
]


# --- awsQuery ser/de ---
def to_query_text(value: ChangeAction) -> str:
    return value


def from_query_text(text: str) -> ChangeAction:
    return cast(ChangeAction, text)


def serialize_query(
    value: ChangeAction, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ChangeAction:
    return from_query_text(el.text or "")
