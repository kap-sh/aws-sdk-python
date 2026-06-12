"""Generated from Smithy shape ``com.amazonaws.elasticache#DataStorageUnit``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elasticache._protocol.xml import Element
from aws_sdk_elasticache.errors import DeserializationError

DataStorageUnit: TypeAlias = Literal["GB",]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(("GB",))


def to_query_text(value: DataStorageUnit) -> str:
    return value


def from_query_text(text: str) -> DataStorageUnit:
    if text not in _VALUES:
        raise DeserializationError(f"unknown DataStorageUnit value: {text!r}")
    return cast(DataStorageUnit, text)


def serialize_query(
    value: DataStorageUnit, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> DataStorageUnit:
    return from_query_text(el.text or "")
