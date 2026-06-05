"""Generated from Smithy shape ``com.amazonaws.ec2#ClientVpnAuthorizationRuleStatusCode``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

ClientVpnAuthorizationRuleStatusCode: TypeAlias = Literal[
    "authorizing",
    "active",
    "failed",
    "revoking",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "authorizing",
        "active",
        "failed",
        "revoking",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "authorizing",
        "active",
        "failed",
        "revoking",
    )
)


def to_ec2_query_text(value: ClientVpnAuthorizationRuleStatusCode) -> str:
    return value


def from_ec2_query_text(text: str) -> ClientVpnAuthorizationRuleStatusCode:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown ClientVpnAuthorizationRuleStatusCode value: {text!r}"
        )
    return cast(ClientVpnAuthorizationRuleStatusCode, text)


def serialize_ec2_query(
    value: ClientVpnAuthorizationRuleStatusCode,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ClientVpnAuthorizationRuleStatusCode:
    return from_ec2_query_text(el.text or "")
