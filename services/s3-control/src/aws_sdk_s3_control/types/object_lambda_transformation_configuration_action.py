"""Generated from Smithy shape ``com.amazonaws.s3control#ObjectLambdaTransformationConfigurationAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3_control._protocol.xml import Element, SubElement
from aws_sdk_s3_control.errors import DeserializationError

ObjectLambdaTransformationConfigurationAction: TypeAlias = Literal[
    "GetObject",
    "HeadObject",
    "ListObjects",
    "ListObjectsV2",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GetObject",
        "HeadObject",
        "ListObjects",
        "ListObjectsV2",
    )
)


def to_xml_text(value: ObjectLambdaTransformationConfigurationAction) -> str:
    return value


def from_xml_text(text: str) -> ObjectLambdaTransformationConfigurationAction:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown ObjectLambdaTransformationConfigurationAction value: {text!r}"
        )
    return cast(ObjectLambdaTransformationConfigurationAction, text)


def serialize_xml(
    value: ObjectLambdaTransformationConfigurationAction, parent: Element, tag: str
) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ObjectLambdaTransformationConfigurationAction:
    return from_xml_text(el.text or "")
