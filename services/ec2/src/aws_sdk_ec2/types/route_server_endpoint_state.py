"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServerEndpointState``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

RouteServerEndpointState: TypeAlias = Literal[
    "pending",
    "available",
    "deleting",
    "deleted",
    "failing",
    "failed",
    "delete-failed",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "pending",
        "available",
        "deleting",
        "deleted",
        "failing",
        "failed",
        "delete-failed",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "pending",
        "available",
        "deleting",
        "deleted",
        "failing",
        "failed",
        "delete-failed",
    )
)


def to_ec2_query_text(value: RouteServerEndpointState) -> str:
    return value


def from_ec2_query_text(text: str) -> RouteServerEndpointState:
    if text not in _VALUES:
        raise DeserializationError(f"unknown RouteServerEndpointState value: {text!r}")
    return cast(RouteServerEndpointState, text)


def serialize_ec2_query(
    value: RouteServerEndpointState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> RouteServerEndpointState:
    return from_ec2_query_text(el.text or "")
