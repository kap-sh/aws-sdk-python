"""Generated from Smithy shape ``com.amazonaws.ec2#ClientVpnConnectionStatusCode``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

ClientVpnConnectionStatusCode: TypeAlias = Literal[
    "active",
    "failed-to-terminate",
    "terminating",
    "terminated",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "active",
        "failed-to-terminate",
        "terminating",
        "terminated",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "active",
        "failed-to-terminate",
        "terminating",
        "terminated",
    )
)


def to_ec2_query_text(value: ClientVpnConnectionStatusCode) -> str:
    return value


def from_ec2_query_text(text: str) -> ClientVpnConnectionStatusCode:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown ClientVpnConnectionStatusCode value: {text!r}"
        )
    return cast(ClientVpnConnectionStatusCode, text)


def serialize_ec2_query(
    value: ClientVpnConnectionStatusCode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ClientVpnConnectionStatusCode:
    return from_ec2_query_text(el.text or "")
