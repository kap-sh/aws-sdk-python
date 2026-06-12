"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateRealtimeLogConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.end_point_list
    import aws_sdk_cloudfront.types.field_list
    import aws_sdk_cloudfront.types.long
    import aws_sdk_cloudfront.types.string


class CreateRealtimeLogConfigRequest(TypedDict):
    end_points: "aws_sdk_cloudfront.types.end_point_list.EndPointList"
    """<p>Contains information about the Amazon Kinesis data stream where you are sending real-time log data.</p>"""
    fields: "aws_sdk_cloudfront.types.field_list.FieldList"
    """<p>A list of fields to include in each real-time log record.</p> <p>For more information about fields, see <a href=\"https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/real-time-logs.html#understand-real-time-log-config-fields\">Real-time log configuration fields</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>"""
    name: "aws_sdk_cloudfront.types.string.string"
    """<p>A unique name to identify this real-time log configuration.</p>"""
    sampling_rate: "aws_sdk_cloudfront.types.long.long"
    """<p>The sampling rate for this real-time log configuration. You can specify a whole number between 1 and 100 (inclusive) to determine the percentage of viewer requests that are represented in the real-time log data.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CreateRealtimeLogConfigRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_cloudfront.types.end_point_list

    aws_sdk_cloudfront.types.end_point_list.serialize_xml(
        value["end_points"], el, "EndPoints"
    )
    import aws_sdk_cloudfront.types.field_list

    aws_sdk_cloudfront.types.field_list.serialize_xml(value["fields"], el, "Fields")
    SubElement(el, "Name").text = str(value["name"])
    SubElement(el, "SamplingRate").text = str(value["sampling_rate"])


def deserialize_xml(el: Element) -> CreateRealtimeLogConfigRequest:
    out: CreateRealtimeLogConfigRequest = {}  # type: ignore[typeddict-item]
    child_end_points = el.find("EndPoints")
    if child_end_points is not None:
        import aws_sdk_cloudfront.types.end_point_list

        out["end_points"] = aws_sdk_cloudfront.types.end_point_list.deserialize_xml(
            child_end_points
        )
    else:
        raise DeserializationError("CreateRealtimeLogConfigRequest.end_points required")
    child_fields = el.find("Fields")
    if child_fields is not None:
        import aws_sdk_cloudfront.types.field_list

        out["fields"] = aws_sdk_cloudfront.types.field_list.deserialize_xml(
            child_fields
        )
    else:
        raise DeserializationError("CreateRealtimeLogConfigRequest.fields required")
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        raise DeserializationError("CreateRealtimeLogConfigRequest.name required")
    child_sampling_rate = el.find("SamplingRate")
    if child_sampling_rate is not None:
        out["sampling_rate"] = int(child_sampling_rate.text or "")
    else:
        raise DeserializationError(
            "CreateRealtimeLogConfigRequest.sampling_rate required"
        )
    return out
