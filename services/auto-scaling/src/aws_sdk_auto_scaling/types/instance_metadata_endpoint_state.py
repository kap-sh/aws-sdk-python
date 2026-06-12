"""Generated from Smithy shape ``com.amazonaws.autoscaling#InstanceMetadataEndpointState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auto_scaling._protocol.xml import Element
from aws_sdk_auto_scaling.errors import DeserializationError

InstanceMetadataEndpointState: TypeAlias = Literal[
    "disabled",
    "enabled",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "disabled",
        "enabled",
    )
)


def to_query_text(value: InstanceMetadataEndpointState) -> str:
    return value


def from_query_text(text: str) -> InstanceMetadataEndpointState:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown InstanceMetadataEndpointState value: {text!r}"
        )
    return cast(InstanceMetadataEndpointState, text)


def serialize_query(
    value: InstanceMetadataEndpointState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> InstanceMetadataEndpointState:
    return from_query_text(el.text or "")
