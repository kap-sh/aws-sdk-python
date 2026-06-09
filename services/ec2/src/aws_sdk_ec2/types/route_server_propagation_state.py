"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServerPropagationState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

RouteServerPropagationState: TypeAlias = Literal[
    "pending",
    "available",
    "deleting",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "pending",
        "available",
        "deleting",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "pending",
        "available",
        "deleting",
    )
)


def to_ec2_query_text(value: RouteServerPropagationState) -> str:
    return value


def from_ec2_query_text(text: str) -> RouteServerPropagationState:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown RouteServerPropagationState value: {text!r}"
        )
    return cast(RouteServerPropagationState, text)


def serialize_ec2_query(
    value: RouteServerPropagationState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> RouteServerPropagationState:
    return from_ec2_query_text(el.text or "")
