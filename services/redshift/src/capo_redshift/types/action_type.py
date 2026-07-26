"""Generated from Smithy shape ``com.amazonaws.redshift#ActionType``."""

from typing import Literal, TypeAlias, cast

from capo_redshift._protocol.xml import Element

ActionType: TypeAlias = Literal[
    "restore-cluster",
    "recommend-node-config",
    "resize-cluster",
]


# --- awsQuery ser/de ---
def to_query_text(value: ActionType) -> str:
    return value


def from_query_text(text: str) -> ActionType:
    return cast(ActionType, text)


def serialize_query(
    value: ActionType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ActionType:
    return from_query_text(el.text or "")
