"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServerPersistRoutesAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

RouteServerPersistRoutesAction: TypeAlias = Literal[
    "enable",
    "disable",
    "reset",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "enable",
        "disable",
        "reset",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "enable",
        "disable",
        "reset",
    )
)


def to_ec2_query_text(value: RouteServerPersistRoutesAction) -> str:
    return value


def from_ec2_query_text(text: str) -> RouteServerPersistRoutesAction:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown RouteServerPersistRoutesAction value: {text!r}"
        )
    return cast(RouteServerPersistRoutesAction, text)


def serialize_ec2_query(
    value: RouteServerPersistRoutesAction, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> RouteServerPersistRoutesAction:
    return from_ec2_query_text(el.text or "")
