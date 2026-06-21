"""Generated from Smithy shape ``com.amazonaws.redshift#ApplicationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_redshift._protocol.xml import Element

ApplicationType: TypeAlias = Literal[
    "None",
    "Lakehouse",
]


# --- awsQuery ser/de ---
def to_query_text(value: ApplicationType) -> str:
    return value


def from_query_text(text: str) -> ApplicationType:
    return cast(ApplicationType, text)


def serialize_query(
    value: ApplicationType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ApplicationType:
    return from_query_text(el.text or "")
