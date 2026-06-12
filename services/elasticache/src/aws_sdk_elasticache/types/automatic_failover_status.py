"""Generated from Smithy shape ``com.amazonaws.elasticache#AutomaticFailoverStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elasticache._protocol.xml import Element
from aws_sdk_elasticache.errors import DeserializationError

AutomaticFailoverStatus: TypeAlias = Literal[
    "enabled",
    "disabled",
    "enabling",
    "disabling",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "enabled",
        "disabled",
        "enabling",
        "disabling",
    )
)


def to_query_text(value: AutomaticFailoverStatus) -> str:
    return value


def from_query_text(text: str) -> AutomaticFailoverStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown AutomaticFailoverStatus value: {text!r}")
    return cast(AutomaticFailoverStatus, text)


def serialize_query(
    value: AutomaticFailoverStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> AutomaticFailoverStatus:
    return from_query_text(el.text or "")
