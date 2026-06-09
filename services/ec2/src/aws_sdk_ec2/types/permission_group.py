"""Generated from Smithy shape ``com.amazonaws.ec2#PermissionGroup``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

PermissionGroup: TypeAlias = Literal["all",]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(("all",))


_VALUES: frozenset[str] = frozenset(("all",))


def to_ec2_query_text(value: PermissionGroup) -> str:
    return value


def from_ec2_query_text(text: str) -> PermissionGroup:
    if text not in _VALUES:
        raise DeserializationError(f"unknown PermissionGroup value: {text!r}")
    return cast(PermissionGroup, text)


def serialize_ec2_query(
    value: PermissionGroup, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> PermissionGroup:
    return from_ec2_query_text(el.text or "")
