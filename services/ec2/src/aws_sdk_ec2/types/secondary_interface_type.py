"""Generated from Smithy shape ``com.amazonaws.ec2#SecondaryInterfaceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

SecondaryInterfaceType: TypeAlias = Literal["secondary",]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(("secondary",))


_VALUES: frozenset[str] = frozenset(("secondary",))


def to_ec2_query_text(value: SecondaryInterfaceType) -> str:
    return value


def from_ec2_query_text(text: str) -> SecondaryInterfaceType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown SecondaryInterfaceType value: {text!r}")
    return cast(SecondaryInterfaceType, text)


def serialize_ec2_query(
    value: SecondaryInterfaceType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> SecondaryInterfaceType:
    return from_ec2_query_text(el.text or "")
