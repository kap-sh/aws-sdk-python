"""Generated from Smithy shape ``com.amazonaws.ec2#SqlServerLicenseUsage``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

SqlServerLicenseUsage: TypeAlias = Literal[
    "full",
    "waived",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "full",
        "waived",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "full",
        "waived",
    )
)


def to_ec2_query_text(value: SqlServerLicenseUsage) -> str:
    return value


def from_ec2_query_text(text: str) -> SqlServerLicenseUsage:
    if text not in _VALUES:
        raise DeserializationError(f"unknown SqlServerLicenseUsage value: {text!r}")
    return cast(SqlServerLicenseUsage, text)


def serialize_ec2_query(
    value: SqlServerLicenseUsage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> SqlServerLicenseUsage:
    return from_ec2_query_text(el.text or "")
