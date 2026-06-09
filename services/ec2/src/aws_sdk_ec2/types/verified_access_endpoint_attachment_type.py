"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessEndpointAttachmentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

VerifiedAccessEndpointAttachmentType: TypeAlias = Literal["vpc",]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(("vpc",))


_VALUES: frozenset[str] = frozenset(("vpc",))


def to_ec2_query_text(value: VerifiedAccessEndpointAttachmentType) -> str:
    return value


def from_ec2_query_text(text: str) -> VerifiedAccessEndpointAttachmentType:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown VerifiedAccessEndpointAttachmentType value: {text!r}"
        )
    return cast(VerifiedAccessEndpointAttachmentType, text)


def serialize_ec2_query(
    value: VerifiedAccessEndpointAttachmentType,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> VerifiedAccessEndpointAttachmentType:
    return from_ec2_query_text(el.text or "")
