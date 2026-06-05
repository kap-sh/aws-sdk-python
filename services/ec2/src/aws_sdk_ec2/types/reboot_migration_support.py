"""Generated from Smithy shape ``com.amazonaws.ec2#RebootMigrationSupport``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

RebootMigrationSupport: TypeAlias = Literal[
    "unsupported",
    "supported",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "unsupported",
        "supported",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "unsupported",
        "supported",
    )
)


def to_ec2_query_text(value: RebootMigrationSupport) -> str:
    return value


def from_ec2_query_text(text: str) -> RebootMigrationSupport:
    if text not in _VALUES:
        raise DeserializationError(f"unknown RebootMigrationSupport value: {text!r}")
    return cast(RebootMigrationSupport, text)


def serialize_ec2_query(
    value: RebootMigrationSupport, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> RebootMigrationSupport:
    return from_ec2_query_text(el.text or "")
