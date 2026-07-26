"""Generated from Smithy shape ``com.amazonaws.cloudformation#ResourceAttribute``."""

from typing import Literal, TypeAlias, cast

from capo_cloudformation._protocol.xml import Element

ResourceAttribute: TypeAlias = Literal[
    "Properties",
    "Metadata",
    "CreationPolicy",
    "UpdatePolicy",
    "DeletionPolicy",
    "UpdateReplacePolicy",
    "Tags",
]


# --- awsQuery ser/de ---
def to_query_text(value: ResourceAttribute) -> str:
    return value


def from_query_text(text: str) -> ResourceAttribute:
    return cast(ResourceAttribute, text)


def serialize_query(
    value: ResourceAttribute, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ResourceAttribute:
    return from_query_text(el.text or "")
