"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateConnectionFunctionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.function_blob
    import aws_sdk_cloudfront.types.function_config
    import aws_sdk_cloudfront.types.function_name
    import aws_sdk_cloudfront.types.tags


class CreateConnectionFunctionRequest(TypedDict):
    name: "aws_sdk_cloudfront.types.function_name.FunctionName"
    """<p>A name for the connection function.</p>"""
    connection_function_config: (
        "aws_sdk_cloudfront.types.function_config.FunctionConfig"
    )
    connection_function_code: "aws_sdk_cloudfront.types.function_blob.FunctionBlob"
    """<p>The code for the connection function.</p>"""
    tags: NotRequired["aws_sdk_cloudfront.types.tags.Tags"]


# --- restXml ser/de ---
def serialize_xml(
    value: CreateConnectionFunctionRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Name").text = str(value["name"])
    import aws_sdk_cloudfront.types.function_config

    aws_sdk_cloudfront.types.function_config.serialize_xml(
        value["connection_function_config"], el, "ConnectionFunctionConfig"
    )
    import aws_sdk_cloudfront.types.function_blob

    aws_sdk_cloudfront.types.function_blob.serialize_xml(
        value["connection_function_code"], el, "ConnectionFunctionCode"
    )
    if "tags" in value:
        import aws_sdk_cloudfront.types.tags

        aws_sdk_cloudfront.types.tags.serialize_xml(value["tags"], el, "Tags")


def deserialize_xml(el: Element) -> CreateConnectionFunctionRequest:
    out: CreateConnectionFunctionRequest = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        raise DeserializationError("CreateConnectionFunctionRequest.name required")
    child_connection_function_config = el.find("ConnectionFunctionConfig")
    if child_connection_function_config is not None:
        import aws_sdk_cloudfront.types.function_config

        out["connection_function_config"] = (
            aws_sdk_cloudfront.types.function_config.deserialize_xml(
                child_connection_function_config
            )
        )
    else:
        raise DeserializationError(
            "CreateConnectionFunctionRequest.connection_function_config required"
        )
    child_connection_function_code = el.find("ConnectionFunctionCode")
    if child_connection_function_code is not None:
        import aws_sdk_cloudfront.types.function_blob

        out["connection_function_code"] = (
            aws_sdk_cloudfront.types.function_blob.deserialize_xml(
                child_connection_function_code
            )
        )
    else:
        raise DeserializationError(
            "CreateConnectionFunctionRequest.connection_function_code required"
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_cloudfront.types.tags

        out["tags"] = aws_sdk_cloudfront.types.tags.deserialize_xml(child_tags)
    return out
