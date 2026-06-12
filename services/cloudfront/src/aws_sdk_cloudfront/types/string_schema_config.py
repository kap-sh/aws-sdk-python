"""Generated from Smithy shape ``com.amazonaws.cloudfront#StringSchemaConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.boolean
    import aws_sdk_cloudfront.types.parameter_value
    import aws_sdk_cloudfront.types.sensitive_string_type


class StringSchemaConfig(TypedDict):
    comment: NotRequired[
        "aws_sdk_cloudfront.types.sensitive_string_type.sensitiveStringType"
    ]
    """<p>A comment to describe the parameter.</p>"""
    default_value: NotRequired[
        "aws_sdk_cloudfront.types.parameter_value.ParameterValue"
    ]
    """<p>The default value of the parameter.</p>"""
    required: "aws_sdk_cloudfront.types.boolean.boolean"
    """<p>Whether the defined parameter is required.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: StringSchemaConfig, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "comment" in value:
        SubElement(el, "Comment").text = str(value["comment"])
    if "default_value" in value:
        SubElement(el, "DefaultValue").text = str(value["default_value"])
    SubElement(el, "Required").text = "true" if value["required"] else "false"


def deserialize_xml(el: Element) -> StringSchemaConfig:
    out: StringSchemaConfig = {}  # type: ignore[typeddict-item]
    child_comment = el.find("Comment")
    if child_comment is not None:
        out["comment"] = str(child_comment.text or "")
    child_default_value = el.find("DefaultValue")
    if child_default_value is not None:
        out["default_value"] = str(child_default_value.text or "")
    child_required = el.find("Required")
    if child_required is not None:
        out["required"] = (child_required.text or "").lower() == "true"
    else:
        raise DeserializationError("StringSchemaConfig.required required")
    return out
