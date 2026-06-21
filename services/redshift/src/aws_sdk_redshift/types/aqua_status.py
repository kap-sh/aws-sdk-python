"""Generated from Smithy shape ``com.amazonaws.redshift#AquaStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_redshift._protocol.xml import Element

AquaStatus: TypeAlias = Literal[
    "enabled",
    "disabled",
    "applying",
]


# --- awsQuery ser/de ---
def to_query_text(value: AquaStatus) -> str:
    return value


def from_query_text(text: str) -> AquaStatus:
    return cast(AquaStatus, text)


def serialize_query(
    value: AquaStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> AquaStatus:
    return from_query_text(el.text or "")
