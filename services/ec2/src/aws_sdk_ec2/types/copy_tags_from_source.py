"""Generated from Smithy shape ``com.amazonaws.ec2#CopyTagsFromSource``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

CopyTagsFromSource: TypeAlias = Literal["volume",]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(("volume",))


_VALUES: frozenset[str] = frozenset(("volume",))


def to_ec2_query_text(value: CopyTagsFromSource) -> str:
    return value


def from_ec2_query_text(text: str) -> CopyTagsFromSource:
    if text not in _VALUES:
        raise DeserializationError(f"unknown CopyTagsFromSource value: {text!r}")
    return cast(CopyTagsFromSource, text)


def serialize_ec2_query(
    value: CopyTagsFromSource, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> CopyTagsFromSource:
    return from_ec2_query_text(el.text or "")
