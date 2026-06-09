"""Generated from Smithy shape ``com.amazonaws.ec2#AttachmentLimitType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

AttachmentLimitType: TypeAlias = Literal[
    "shared",
    "dedicated",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "shared",
        "dedicated",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "shared",
        "dedicated",
    )
)


def to_ec2_query_text(value: AttachmentLimitType) -> str:
    return value


def from_ec2_query_text(text: str) -> AttachmentLimitType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown AttachmentLimitType value: {text!r}")
    return cast(AttachmentLimitType, text)


def serialize_ec2_query(
    value: AttachmentLimitType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> AttachmentLimitType:
    return from_ec2_query_text(el.text or "")
