"""Generated from Smithy shape ``com.amazonaws.ec2#EkPubKeyFormat``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

EkPubKeyFormat: TypeAlias = Literal[
    "der",
    "tpmt",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "der",
        "tpmt",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "der",
        "tpmt",
    )
)


def to_ec2_query_text(value: EkPubKeyFormat) -> str:
    return value


def from_ec2_query_text(text: str) -> EkPubKeyFormat:
    if text not in _VALUES:
        raise DeserializationError(f"unknown EkPubKeyFormat value: {text!r}")
    return cast(EkPubKeyFormat, text)


def serialize_ec2_query(
    value: EkPubKeyFormat, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> EkPubKeyFormat:
    return from_ec2_query_text(el.text or "")
