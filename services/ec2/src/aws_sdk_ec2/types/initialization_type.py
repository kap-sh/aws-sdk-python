"""Generated from Smithy shape ``com.amazonaws.ec2#InitializationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

InitializationType: TypeAlias = Literal[
    "default",
    "provisioned-rate",
    "volume-copy",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "default",
        "provisioned-rate",
        "volume-copy",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "default",
        "provisioned-rate",
        "volume-copy",
    )
)


def to_ec2_query_text(value: InitializationType) -> str:
    return value


def from_ec2_query_text(text: str) -> InitializationType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown InitializationType value: {text!r}")
    return cast(InitializationType, text)


def serialize_ec2_query(
    value: InitializationType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> InitializationType:
    return from_ec2_query_text(el.text or "")
