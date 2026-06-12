"""Generated from Smithy shape ``com.amazonaws.cloudformation#PermissionModels``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

PermissionModels: TypeAlias = Literal[
    "SERVICE_MANAGED",
    "SELF_MANAGED",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SERVICE_MANAGED",
        "SELF_MANAGED",
    )
)


def to_query_text(value: PermissionModels) -> str:
    return value


def from_query_text(text: str) -> PermissionModels:
    if text not in _VALUES:
        raise DeserializationError(f"unknown PermissionModels value: {text!r}")
    return cast(PermissionModels, text)


def serialize_query(
    value: PermissionModels, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> PermissionModels:
    return from_query_text(el.text or "")
