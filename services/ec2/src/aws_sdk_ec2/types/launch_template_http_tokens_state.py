"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateHttpTokensState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

LaunchTemplateHttpTokensState: TypeAlias = Literal[
    "optional",
    "required",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "optional",
        "required",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "optional",
        "required",
    )
)


def to_ec2_query_text(value: LaunchTemplateHttpTokensState) -> str:
    return value


def from_ec2_query_text(text: str) -> LaunchTemplateHttpTokensState:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown LaunchTemplateHttpTokensState value: {text!r}"
        )
    return cast(LaunchTemplateHttpTokensState, text)


def serialize_ec2_query(
    value: LaunchTemplateHttpTokensState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> LaunchTemplateHttpTokensState:
    return from_ec2_query_text(el.text or "")
