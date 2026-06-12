"""Generated from Smithy shape ``com.amazonaws.cloudfront#ParameterDefinition``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.parameter_definition_schema
    import aws_sdk_cloudfront.types.parameter_name


class ParameterDefinition(TypedDict):
    name: "aws_sdk_cloudfront.types.parameter_name.ParameterName"
    """<p>The name of the parameter.</p>"""
    definition: (
        "aws_sdk_cloudfront.types.parameter_definition_schema.ParameterDefinitionSchema"
    )
    """<p>The value that you assigned to the parameter.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ParameterDefinition, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Name").text = str(value["name"])
    import aws_sdk_cloudfront.types.parameter_definition_schema

    aws_sdk_cloudfront.types.parameter_definition_schema.serialize_xml(
        value["definition"], el, "Definition"
    )


def deserialize_xml(el: Element) -> ParameterDefinition:
    out: ParameterDefinition = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        raise DeserializationError("ParameterDefinition.name required")
    child_definition = el.find("Definition")
    if child_definition is not None:
        import aws_sdk_cloudfront.types.parameter_definition_schema

        out["definition"] = (
            aws_sdk_cloudfront.types.parameter_definition_schema.deserialize_xml(
                child_definition
            )
        )
    else:
        raise DeserializationError("ParameterDefinition.definition required")
    return out
