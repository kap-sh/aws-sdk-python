"""Generated from Smithy shape ``com.amazonaws.ec2#DestinationFileFormat``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

DestinationFileFormat: TypeAlias = Literal[
    "plain-text",
    "parquet",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "plain-text",
        "parquet",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "plain-text",
        "parquet",
    )
)


def to_ec2_query_text(value: DestinationFileFormat) -> str:
    return value


def from_ec2_query_text(text: str) -> DestinationFileFormat:
    if text not in _VALUES:
        raise DeserializationError(f"unknown DestinationFileFormat value: {text!r}")
    return cast(DestinationFileFormat, text)


def serialize_ec2_query(
    value: DestinationFileFormat, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> DestinationFileFormat:
    return from_ec2_query_text(el.text or "")
