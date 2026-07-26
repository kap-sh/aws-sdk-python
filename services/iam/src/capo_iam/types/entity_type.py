"""Generated from Smithy shape ``com.amazonaws.iam#EntityType``."""

from typing import Literal, TypeAlias, cast

from capo_iam._protocol.xml import Element

EntityType: TypeAlias = Literal[
    "User",
    "Role",
    "Group",
    "LocalManagedPolicy",
    "AWSManagedPolicy",
]


# --- awsQuery ser/de ---
def to_query_text(value: EntityType) -> str:
    return value


def from_query_text(text: str) -> EntityType:
    return cast(EntityType, text)


def serialize_query(
    value: EntityType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> EntityType:
    return from_query_text(el.text or "")
