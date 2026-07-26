"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServerPropagationState``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

RouteServerPropagationState: TypeAlias = Literal[
    "pending",
    "available",
    "deleting",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: RouteServerPropagationState) -> str:
    return value


def from_ec2_query_text(text: str) -> RouteServerPropagationState:
    return cast(RouteServerPropagationState, text)


def serialize_ec2_query(
    value: RouteServerPropagationState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> RouteServerPropagationState:
    return from_ec2_query_text(el.text or "")
