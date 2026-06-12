"""Generated from Smithy shape ``com.amazonaws.redshift#DataShareType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_redshift._protocol.xml import Element
from aws_sdk_redshift.errors import DeserializationError

DataShareType: TypeAlias = Literal["INTERNAL",]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(("INTERNAL",))


def to_query_text(value: DataShareType) -> str:
    return value


def from_query_text(text: str) -> DataShareType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown DataShareType value: {text!r}")
    return cast(DataShareType, text)


def serialize_query(
    value: DataShareType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> DataShareType:
    return from_query_text(el.text or "")
