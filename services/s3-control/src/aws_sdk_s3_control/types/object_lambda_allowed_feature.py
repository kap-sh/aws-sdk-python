"""Generated from Smithy shape ``com.amazonaws.s3control#ObjectLambdaAllowedFeature``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3_control._protocol.xml import Element, SubElement

ObjectLambdaAllowedFeature: TypeAlias = Literal[
    "GetObject-Range",
    "GetObject-PartNumber",
    "HeadObject-Range",
    "HeadObject-PartNumber",
]


# --- restXml ser/de ---
def to_xml_text(value: ObjectLambdaAllowedFeature) -> str:
    return value


def from_xml_text(text: str) -> ObjectLambdaAllowedFeature:
    return cast(ObjectLambdaAllowedFeature, text)


def serialize_xml(value: ObjectLambdaAllowedFeature, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ObjectLambdaAllowedFeature:
    return from_xml_text(el.text or "")
