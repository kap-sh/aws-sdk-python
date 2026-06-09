"""Generated from Smithy shape ``com.amazonaws.ec2#ImdsSupportValues``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

ImdsSupportValues: TypeAlias = Literal["v2.0",]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(("v2.0",))


_VALUES: frozenset[str] = frozenset(("v2.0",))


def to_ec2_query_text(value: ImdsSupportValues) -> str:
    return value


def from_ec2_query_text(text: str) -> ImdsSupportValues:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ImdsSupportValues value: {text!r}")
    return cast(ImdsSupportValues, text)


def serialize_ec2_query(
    value: ImdsSupportValues, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ImdsSupportValues:
    return from_ec2_query_text(el.text or "")
