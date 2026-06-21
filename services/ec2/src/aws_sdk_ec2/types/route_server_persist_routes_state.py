"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServerPersistRoutesState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

RouteServerPersistRoutesState: TypeAlias = Literal[
    "enabling",
    "enabled",
    "resetting",
    "disabling",
    "disabled",
    "modifying",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: RouteServerPersistRoutesState) -> str:
    return value


def from_ec2_query_text(text: str) -> RouteServerPersistRoutesState:
    return cast(RouteServerPersistRoutesState, text)


def serialize_ec2_query(
    value: RouteServerPersistRoutesState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> RouteServerPersistRoutesState:
    return from_ec2_query_text(el.text or "")
