"""Generated from Smithy shape ``com.amazonaws.ec2#OutputFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

OutputFormat: TypeAlias = Literal[
    "csv",
    "parquet",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "csv",
        "parquet",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "csv",
        "parquet",
    )
)


def to_ec2_query_text(value: OutputFormat) -> str:
    return value


def from_ec2_query_text(text: str) -> OutputFormat:
    if text not in _VALUES:
        raise DeserializationError(f"unknown OutputFormat value: {text!r}")
    return cast(OutputFormat, text)


def serialize_ec2_query(
    value: OutputFormat, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> OutputFormat:
    return from_ec2_query_text(el.text or "")
