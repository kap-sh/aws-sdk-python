"""Generated from Smithy shape ``com.amazonaws.s3control#ObjectLambdaTransformationConfigurationAction``."""

from typing import Literal, TypeAlias, cast

from capo_s3_control._protocol.xml import Element, SubElement

ObjectLambdaTransformationConfigurationAction: TypeAlias = Literal[
    "GetObject",
    "HeadObject",
    "ListObjects",
    "ListObjectsV2",
]


# --- restXml ser/de ---
def to_xml_text(value: ObjectLambdaTransformationConfigurationAction) -> str:
    return value


def from_xml_text(text: str) -> ObjectLambdaTransformationConfigurationAction:
    return cast(ObjectLambdaTransformationConfigurationAction, text)


def serialize_xml(
    value: ObjectLambdaTransformationConfigurationAction, parent: Element, tag: str
) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ObjectLambdaTransformationConfigurationAction:
    return from_xml_text(el.text or "")
