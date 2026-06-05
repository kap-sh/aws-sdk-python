"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateErrorCode``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

LaunchTemplateErrorCode: TypeAlias = Literal[
    "launchTemplateIdDoesNotExist",
    "launchTemplateIdMalformed",
    "launchTemplateNameDoesNotExist",
    "launchTemplateNameMalformed",
    "launchTemplateVersionDoesNotExist",
    "unexpectedError",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "launchTemplateIdDoesNotExist",
        "launchTemplateIdMalformed",
        "launchTemplateNameDoesNotExist",
        "launchTemplateNameMalformed",
        "launchTemplateVersionDoesNotExist",
        "unexpectedError",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "launchTemplateIdDoesNotExist",
        "launchTemplateIdMalformed",
        "launchTemplateNameDoesNotExist",
        "launchTemplateNameMalformed",
        "launchTemplateVersionDoesNotExist",
        "unexpectedError",
    )
)


def to_ec2_query_text(value: LaunchTemplateErrorCode) -> str:
    return value


def from_ec2_query_text(text: str) -> LaunchTemplateErrorCode:
    if text not in _VALUES:
        raise DeserializationError(f"unknown LaunchTemplateErrorCode value: {text!r}")
    return cast(LaunchTemplateErrorCode, text)


def serialize_ec2_query(
    value: LaunchTemplateErrorCode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> LaunchTemplateErrorCode:
    return from_ec2_query_text(el.text or "")
