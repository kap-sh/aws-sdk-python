"""Generated from Smithy shape ``com.amazonaws.ec2#FpgaImageAttributeName``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

FpgaImageAttributeName: TypeAlias = Literal[
    "description",
    "name",
    "loadPermission",
    "productCodes",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "description",
        "name",
        "loadPermission",
        "productCodes",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "description",
        "name",
        "loadPermission",
        "productCodes",
    )
)


def to_ec2_query_text(value: FpgaImageAttributeName) -> str:
    return value


def from_ec2_query_text(text: str) -> FpgaImageAttributeName:
    if text not in _VALUES:
        raise DeserializationError(f"unknown FpgaImageAttributeName value: {text!r}")
    return cast(FpgaImageAttributeName, text)


def serialize_ec2_query(
    value: FpgaImageAttributeName, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> FpgaImageAttributeName:
    return from_ec2_query_text(el.text or "")
