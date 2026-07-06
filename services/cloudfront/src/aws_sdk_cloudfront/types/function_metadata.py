"""Generated from Smithy shape ``com.amazonaws.cloudfront#FunctionMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.function_stage
    import aws_sdk_cloudfront.types.string
    import aws_sdk_cloudfront.types.timestamp


class FunctionMetadata(TypedDict, closed=True):
    function_arn: "aws_sdk_cloudfront.types.string.string"
    """<p>The Amazon Resource Name (ARN) of the function. The ARN uniquely identifies the function.</p>"""
    stage: NotRequired["aws_sdk_cloudfront.types.function_stage.FunctionStage"]
    """<p>The stage that the function is in, either <code>DEVELOPMENT</code> or <code>LIVE</code>.</p> <p>When a function is in the <code>DEVELOPMENT</code> stage, you can test the function with <code>TestFunction</code>, and update it with <code>UpdateFunction</code>.</p> <p>When a function is in the <code>LIVE</code> stage, you can attach the function to a distribution's cache behavior, using the function's ARN.</p>"""
    created_time: NotRequired["aws_sdk_cloudfront.types.timestamp.timestamp"]
    """<p>The date and time when the function was created.</p>"""
    last_modified_time: "aws_sdk_cloudfront.types.timestamp.timestamp"
    """<p>The date and time when the function was most recently updated.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: FunctionMetadata, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "FunctionARN").text = str(value["function_arn"])
    if "stage" in value:
        import aws_sdk_cloudfront.types.function_stage

        aws_sdk_cloudfront.types.function_stage.serialize_xml(
            value["stage"], el, "Stage"
        )
    if "created_time" in value:
        import aws_sdk_cloudfront.types.timestamp

        aws_sdk_cloudfront.types.timestamp.serialize_xml(
            value["created_time"], el, "CreatedTime"
        )
    import aws_sdk_cloudfront.types.timestamp

    aws_sdk_cloudfront.types.timestamp.serialize_xml(
        value["last_modified_time"], el, "LastModifiedTime"
    )


def deserialize_xml(el: Element) -> FunctionMetadata:
    out: FunctionMetadata = {}  # type: ignore[typeddict-item]
    child_function_arn = el.find("FunctionARN")
    if child_function_arn is not None:
        out["function_arn"] = str(child_function_arn.text or "")
    else:
        raise DeserializationError("FunctionMetadata.function_arn required")
    child_stage = el.find("Stage")
    if child_stage is not None:
        import aws_sdk_cloudfront.types.function_stage

        out["stage"] = aws_sdk_cloudfront.types.function_stage.deserialize_xml(
            child_stage
        )
    child_created_time = el.find("CreatedTime")
    if child_created_time is not None:
        import aws_sdk_cloudfront.types.timestamp

        out["created_time"] = aws_sdk_cloudfront.types.timestamp.deserialize_xml(
            child_created_time
        )
    child_last_modified_time = el.find("LastModifiedTime")
    if child_last_modified_time is not None:
        import aws_sdk_cloudfront.types.timestamp

        out["last_modified_time"] = aws_sdk_cloudfront.types.timestamp.deserialize_xml(
            child_last_modified_time
        )
    else:
        raise DeserializationError("FunctionMetadata.last_modified_time required")
    return out
