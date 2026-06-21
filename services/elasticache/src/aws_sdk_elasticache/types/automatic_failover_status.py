"""Generated from Smithy shape ``com.amazonaws.elasticache#AutomaticFailoverStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elasticache._protocol.xml import Element

AutomaticFailoverStatus: TypeAlias = Literal[
    "enabled",
    "disabled",
    "enabling",
    "disabling",
]


# --- awsQuery ser/de ---
def to_query_text(value: AutomaticFailoverStatus) -> str:
    return value


def from_query_text(text: str) -> AutomaticFailoverStatus:
    return cast(AutomaticFailoverStatus, text)


def serialize_query(
    value: AutomaticFailoverStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> AutomaticFailoverStatus:
    return from_query_text(el.text or "")
