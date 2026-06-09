"""Generated from Smithy shape ``com.amazonaws.ec2#DeviceTrustProviderType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

DeviceTrustProviderType: TypeAlias = Literal[
    "jamf",
    "crowdstrike",
    "jumpcloud",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "jamf",
        "crowdstrike",
        "jumpcloud",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "jamf",
        "crowdstrike",
        "jumpcloud",
    )
)


def to_ec2_query_text(value: DeviceTrustProviderType) -> str:
    return value


def from_ec2_query_text(text: str) -> DeviceTrustProviderType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown DeviceTrustProviderType value: {text!r}")
    return cast(DeviceTrustProviderType, text)


def serialize_ec2_query(
    value: DeviceTrustProviderType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> DeviceTrustProviderType:
    return from_ec2_query_text(el.text or "")
