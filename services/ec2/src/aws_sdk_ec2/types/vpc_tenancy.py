"""Generated from Smithy shape ``com.amazonaws.ec2#VpcTenancy``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

VpcTenancy: TypeAlias = Literal["default",]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(("default",))


_VALUES: frozenset[str] = frozenset(("default",))


def to_ec2_query_text(value: VpcTenancy) -> str:
    return value


def from_ec2_query_text(text: str) -> VpcTenancy:
    if text not in _VALUES:
        raise DeserializationError(f"unknown VpcTenancy value: {text!r}")
    return cast(VpcTenancy, text)


def serialize_ec2_query(
    value: VpcTenancy, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> VpcTenancy:
    return from_ec2_query_text(el.text or "")
