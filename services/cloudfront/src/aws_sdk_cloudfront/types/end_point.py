"""Generated from Smithy shape ``com.amazonaws.cloudfront#EndPoint``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.kinesis_stream_config
    import aws_sdk_cloudfront.types.string


class EndPoint(TypedDict):
    stream_type: "aws_sdk_cloudfront.types.string.string"
    """<p>The type of data stream where you are sending real-time log data. The only valid value is <code>Kinesis</code>.</p>"""
    kinesis_stream_config: NotRequired[
        "aws_sdk_cloudfront.types.kinesis_stream_config.KinesisStreamConfig"
    ]
    """<p>Contains information about the Amazon Kinesis data stream where you are sending real-time log data in a real-time log configuration.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: EndPoint, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "StreamType").text = str(value["stream_type"])
    if "kinesis_stream_config" in value:
        import aws_sdk_cloudfront.types.kinesis_stream_config

        aws_sdk_cloudfront.types.kinesis_stream_config.serialize_xml(
            value["kinesis_stream_config"], el, "KinesisStreamConfig"
        )


def deserialize_xml(el: Element) -> EndPoint:
    out: EndPoint = {}  # type: ignore[typeddict-item]
    child_stream_type = el.find("StreamType")
    if child_stream_type is not None:
        out["stream_type"] = str(child_stream_type.text or "")
    else:
        raise DeserializationError("EndPoint.stream_type required")
    child_kinesis_stream_config = el.find("KinesisStreamConfig")
    if child_kinesis_stream_config is not None:
        import aws_sdk_cloudfront.types.kinesis_stream_config

        out["kinesis_stream_config"] = (
            aws_sdk_cloudfront.types.kinesis_stream_config.deserialize_xml(
                child_kinesis_stream_config
            )
        )
    return out
