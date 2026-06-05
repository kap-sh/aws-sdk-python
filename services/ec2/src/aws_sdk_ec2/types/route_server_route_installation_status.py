"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServerRouteInstallationStatus``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

RouteServerRouteInstallationStatus: TypeAlias = Literal[
    "installed",
    "rejected",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "installed",
        "rejected",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "installed",
        "rejected",
    )
)


def to_ec2_query_text(value: RouteServerRouteInstallationStatus) -> str:
    return value


def from_ec2_query_text(text: str) -> RouteServerRouteInstallationStatus:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown RouteServerRouteInstallationStatus value: {text!r}"
        )
    return cast(RouteServerRouteInstallationStatus, text)


def serialize_ec2_query(
    value: RouteServerRouteInstallationStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> RouteServerRouteInstallationStatus:
    return from_ec2_query_text(el.text or "")
