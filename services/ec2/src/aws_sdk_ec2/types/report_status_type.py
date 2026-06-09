"""Generated from Smithy shape ``com.amazonaws.ec2#ReportStatusType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

ReportStatusType: TypeAlias = Literal[
    "ok",
    "impaired",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ok",
        "impaired",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "ok",
        "impaired",
    )
)


def to_ec2_query_text(value: ReportStatusType) -> str:
    return value


def from_ec2_query_text(text: str) -> ReportStatusType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ReportStatusType value: {text!r}")
    return cast(ReportStatusType, text)


def serialize_ec2_query(
    value: ReportStatusType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ReportStatusType:
    return from_ec2_query_text(el.text or "")
