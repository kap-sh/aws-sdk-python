"""Generated from Smithy shape ``com.amazonaws.s3control#ObjectLambdaAccessPointAliasStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3_control._protocol.xml import Element, SubElement

ObjectLambdaAccessPointAliasStatus: TypeAlias = Literal[
    "PROVISIONING",
    "READY",
]


# --- restXml ser/de ---
def to_xml_text(value: ObjectLambdaAccessPointAliasStatus) -> str:
    return value


def from_xml_text(text: str) -> ObjectLambdaAccessPointAliasStatus:
    return cast(ObjectLambdaAccessPointAliasStatus, text)


def serialize_xml(
    value: ObjectLambdaAccessPointAliasStatus, parent: Element, tag: str
) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ObjectLambdaAccessPointAliasStatus:
    return from_xml_text(el.text or "")
