"""Generated from Smithy shape ``com.amazonaws.cloudfront#Parameter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.parameter_name
    import aws_sdk_cloudfront.types.parameter_value


class Parameter(TypedDict, closed=True):
    name: "aws_sdk_cloudfront.types.parameter_name.ParameterName"
    """<p>The parameter name.</p>"""
    value: "aws_sdk_cloudfront.types.parameter_value.ParameterValue"
    """<p>The parameter value.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: Parameter, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Name").text = str(value["name"])
    SubElement(el, "Value").text = str(value["value"])


def deserialize_xml(el: Element) -> Parameter:
    out: Parameter = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        raise DeserializationError("Parameter.name required")
    child_value = el.find("Value")
    if child_value is not None:
        out["value"] = str(child_value.text or "")
    else:
        raise DeserializationError("Parameter.value required")
    return out
