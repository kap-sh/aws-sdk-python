"""Generated from Smithy shape ``com.amazonaws.ec2#ClientVpnRouteStatusCode``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

ClientVpnRouteStatusCode: TypeAlias = Literal[
    "creating",
    "active",
    "failed",
    "deleting",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "creating",
        "active",
        "failed",
        "deleting",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "creating",
        "active",
        "failed",
        "deleting",
    )
)


def to_ec2_query_text(value: ClientVpnRouteStatusCode) -> str:
    return value


def from_ec2_query_text(text: str) -> ClientVpnRouteStatusCode:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ClientVpnRouteStatusCode value: {text!r}")
    return cast(ClientVpnRouteStatusCode, text)


def serialize_ec2_query(
    value: ClientVpnRouteStatusCode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ClientVpnRouteStatusCode:
    return from_ec2_query_text(el.text or "")
