"""Generated from Smithy shape ``com.amazonaws.cloudfront#UpdateConnectionFunctionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.function_blob
    import aws_sdk_cloudfront.types.function_config
    import aws_sdk_cloudfront.types.resource_id
    import aws_sdk_cloudfront.types.string


class UpdateConnectionFunctionRequest(TypedDict, closed=True):
    id: "aws_sdk_cloudfront.types.resource_id.ResourceId"
    """<p>The connection function ID.</p>"""
    if_match: "aws_sdk_cloudfront.types.string.string"
    """<p>The current version (<code>ETag</code> value) of the connection function you are updating.</p>"""
    connection_function_config: (
        "aws_sdk_cloudfront.types.function_config.FunctionConfig"
    )
    connection_function_code: "aws_sdk_cloudfront.types.function_blob.FunctionBlob"
    """<p>The connection function code.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: UpdateConnectionFunctionRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_cloudfront.types.function_config

    aws_sdk_cloudfront.types.function_config.serialize_xml(
        value["connection_function_config"], el, "ConnectionFunctionConfig"
    )
    import aws_sdk_cloudfront.types.function_blob

    aws_sdk_cloudfront.types.function_blob.serialize_xml(
        value["connection_function_code"], el, "ConnectionFunctionCode"
    )


def deserialize_xml(el: Element) -> UpdateConnectionFunctionRequest:
    out: UpdateConnectionFunctionRequest = {}  # type: ignore[typeddict-item]
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
            "UpdateConnectionFunctionRequest.connection_function_config required"
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
            "UpdateConnectionFunctionRequest.connection_function_code required"
        )
    return out
