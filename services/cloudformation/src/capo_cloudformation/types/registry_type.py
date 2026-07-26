"""Generated from Smithy shape ``com.amazonaws.cloudformation#RegistryType``."""

from typing import Literal, TypeAlias, cast

from capo_cloudformation._protocol.xml import Element

RegistryType: TypeAlias = Literal[
    "RESOURCE",
    "MODULE",
    "HOOK",
]


# --- awsQuery ser/de ---
def to_query_text(value: RegistryType) -> str:
    return value


def from_query_text(text: str) -> RegistryType:
    return cast(RegistryType, text)


def serialize_query(
    value: RegistryType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> RegistryType:
    return from_query_text(el.text or "")
