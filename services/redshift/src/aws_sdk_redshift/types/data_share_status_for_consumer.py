"""Generated from Smithy shape ``com.amazonaws.redshift#DataShareStatusForConsumer``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_redshift._protocol.xml import Element
from aws_sdk_redshift.errors import DeserializationError

DataShareStatusForConsumer: TypeAlias = Literal[
    "ACTIVE",
    "AVAILABLE",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "AVAILABLE",
    )
)


def to_query_text(value: DataShareStatusForConsumer) -> str:
    return value


def from_query_text(text: str) -> DataShareStatusForConsumer:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown DataShareStatusForConsumer value: {text!r}"
        )
    return cast(DataShareStatusForConsumer, text)


def serialize_query(
    value: DataShareStatusForConsumer, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> DataShareStatusForConsumer:
    return from_query_text(el.text or "")
