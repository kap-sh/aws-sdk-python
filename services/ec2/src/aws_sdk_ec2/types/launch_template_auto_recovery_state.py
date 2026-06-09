"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateAutoRecoveryState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

LaunchTemplateAutoRecoveryState: TypeAlias = Literal[
    "default",
    "disabled",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "default",
        "disabled",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "default",
        "disabled",
    )
)


def to_ec2_query_text(value: LaunchTemplateAutoRecoveryState) -> str:
    return value


def from_ec2_query_text(text: str) -> LaunchTemplateAutoRecoveryState:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown LaunchTemplateAutoRecoveryState value: {text!r}"
        )
    return cast(LaunchTemplateAutoRecoveryState, text)


def serialize_ec2_query(
    value: LaunchTemplateAutoRecoveryState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> LaunchTemplateAutoRecoveryState:
    return from_ec2_query_text(el.text or "")
