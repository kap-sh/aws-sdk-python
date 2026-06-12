"""Generated from Smithy shape ``com.amazonaws.rds#TargetConnectionNetworkType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rds._protocol.xml import Element
from aws_sdk_rds.errors import DeserializationError

TargetConnectionNetworkType: TypeAlias = Literal[
    "IPV4",
    "IPV6",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IPV4",
        "IPV6",
    )
)


def to_query_text(value: TargetConnectionNetworkType) -> str:
    return value


def from_query_text(text: str) -> TargetConnectionNetworkType:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown TargetConnectionNetworkType value: {text!r}"
        )
    return cast(TargetConnectionNetworkType, text)


def serialize_query(
    value: TargetConnectionNetworkType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> TargetConnectionNetworkType:
    return from_query_text(el.text or "")
