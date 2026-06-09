"""Generated from Smithy shape ``com.amazonaws.ec2#ResetFpgaImageAttributeName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

ResetFpgaImageAttributeName: TypeAlias = Literal["loadPermission",]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(("loadPermission",))


_VALUES: frozenset[str] = frozenset(("loadPermission",))


def to_ec2_query_text(value: ResetFpgaImageAttributeName) -> str:
    return value


def from_ec2_query_text(text: str) -> ResetFpgaImageAttributeName:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown ResetFpgaImageAttributeName value: {text!r}"
        )
    return cast(ResetFpgaImageAttributeName, text)


def serialize_ec2_query(
    value: ResetFpgaImageAttributeName, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ResetFpgaImageAttributeName:
    return from_ec2_query_text(el.text or "")
