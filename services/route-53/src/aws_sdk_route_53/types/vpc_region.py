"""Generated from Smithy shape ``com.amazonaws.route53#VPCRegion``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route_53._protocol.xml import Element, SubElement
from aws_sdk_route_53.errors import DeserializationError

VPCRegion: TypeAlias = Literal[
    "us-east-1",
    "us-east-2",
    "us-west-1",
    "us-west-2",
    "eu-west-1",
    "eu-west-2",
    "eu-west-3",
    "eu-central-1",
    "eu-central-2",
    "ap-east-1",
    "me-south-1",
    "us-gov-west-1",
    "us-gov-east-1",
    "us-iso-east-1",
    "us-iso-west-1",
    "us-isob-east-1",
    "me-central-1",
    "ap-southeast-1",
    "ap-southeast-2",
    "ap-southeast-3",
    "ap-south-1",
    "ap-south-2",
    "ap-northeast-1",
    "ap-northeast-2",
    "ap-northeast-3",
    "eu-north-1",
    "sa-east-1",
    "ca-central-1",
    "cn-north-1",
    "cn-northwest-1",
    "af-south-1",
    "eu-south-1",
    "eu-south-2",
    "ap-southeast-4",
    "il-central-1",
    "ca-west-1",
    "ap-southeast-5",
    "mx-central-1",
    "us-isof-south-1",
    "us-isof-east-1",
    "ap-southeast-7",
    "ap-east-2",
    "eu-isoe-west-1",
    "ap-southeast-6",
    "us-isob-west-1",
    "eusc-de-east-1",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "us-east-1",
        "us-east-2",
        "us-west-1",
        "us-west-2",
        "eu-west-1",
        "eu-west-2",
        "eu-west-3",
        "eu-central-1",
        "eu-central-2",
        "ap-east-1",
        "me-south-1",
        "us-gov-west-1",
        "us-gov-east-1",
        "us-iso-east-1",
        "us-iso-west-1",
        "us-isob-east-1",
        "me-central-1",
        "ap-southeast-1",
        "ap-southeast-2",
        "ap-southeast-3",
        "ap-south-1",
        "ap-south-2",
        "ap-northeast-1",
        "ap-northeast-2",
        "ap-northeast-3",
        "eu-north-1",
        "sa-east-1",
        "ca-central-1",
        "cn-north-1",
        "cn-northwest-1",
        "af-south-1",
        "eu-south-1",
        "eu-south-2",
        "ap-southeast-4",
        "il-central-1",
        "ca-west-1",
        "ap-southeast-5",
        "mx-central-1",
        "us-isof-south-1",
        "us-isof-east-1",
        "ap-southeast-7",
        "ap-east-2",
        "eu-isoe-west-1",
        "ap-southeast-6",
        "us-isob-west-1",
        "eusc-de-east-1",
    )
)


def to_xml_text(value: VPCRegion) -> str:
    return value


def from_xml_text(text: str) -> VPCRegion:
    if text not in _VALUES:
        raise DeserializationError(f"unknown VPCRegion value: {text!r}")
    return cast(VPCRegion, text)


def serialize_xml(value: VPCRegion, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> VPCRegion:
    return from_xml_text(el.text or "")
