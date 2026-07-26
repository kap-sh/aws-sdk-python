"""Generated from Smithy shape ``com.amazonaws.cloudformation#VersionBump``."""

from typing import Literal, TypeAlias, cast

from capo_cloudformation._protocol.xml import Element

VersionBump: TypeAlias = Literal[
    "MAJOR",
    "MINOR",
]


# --- awsQuery ser/de ---
def to_query_text(value: VersionBump) -> str:
    return value


def from_query_text(text: str) -> VersionBump:
    return cast(VersionBump, text)


def serialize_query(
    value: VersionBump, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> VersionBump:
    return from_query_text(el.text or "")
