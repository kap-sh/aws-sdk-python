"""Generated from Smithy shape ``com.amazonaws.cloudfront#ParameterDefinitionSchema``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string_schema_config


class ParameterDefinitionSchema(TypedDict):
    string_schema: NotRequired[
        "aws_sdk_cloudfront.types.string_schema_config.StringSchemaConfig"
    ]
    """<p>An object that contains information about the string schema.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ParameterDefinitionSchema, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "string_schema" in value:
        import aws_sdk_cloudfront.types.string_schema_config

        aws_sdk_cloudfront.types.string_schema_config.serialize_xml(
            value["string_schema"], el, "StringSchema"
        )


def deserialize_xml(el: Element) -> ParameterDefinitionSchema:
    out: ParameterDefinitionSchema = {}  # type: ignore[typeddict-item]
    child_string_schema = el.find("StringSchema")
    if child_string_schema is not None:
        import aws_sdk_cloudfront.types.string_schema_config

        out["string_schema"] = (
            aws_sdk_cloudfront.types.string_schema_config.deserialize_xml(
                child_string_schema
            )
        )
    return out
