"""Generated from Smithy shape ``com.amazonaws.cloudfront#ContinuousDeploymentPolicyType``."""

from typing import Literal, TypeAlias, cast

from capo_cloudfront._protocol.xml import Element, SubElement

ContinuousDeploymentPolicyType: TypeAlias = Literal[
    "SingleWeight",
    "SingleHeader",
]


# --- restXml ser/de ---
def to_xml_text(value: ContinuousDeploymentPolicyType) -> str:
    return value


def from_xml_text(text: str) -> ContinuousDeploymentPolicyType:
    return cast(ContinuousDeploymentPolicyType, text)


def serialize_xml(
    value: ContinuousDeploymentPolicyType, parent: Element, tag: str
) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ContinuousDeploymentPolicyType:
    return from_xml_text(el.text or "")
