"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_timestream_write.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_timestream_write.types.amazon_resource_name
    import aws_sdk_timestream_write.types.tag_list


class TagResourceRequest(TypedDict):
    resource_arn: (
        "aws_sdk_timestream_write.types.amazon_resource_name.AmazonResourceName"
    )
    """<p> Identifies the Timestream resource to which tags should be added. This value is an Amazon Resource Name (ARN). </p>"""
    tags: "aws_sdk_timestream_write.types.tag_list.TagList"
    """<p> The tags to be assigned to the Timestream resource. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import aws_sdk_timestream_write.types.tag_list

    out["Tags"] = aws_sdk_timestream_write.types.tag_list.serialize_aws_json_1_0(
        value["tags"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("TagResourceRequest.resource_arn required")
    if "Tags" in data:
        import aws_sdk_timestream_write.types.tag_list

        out["tags"] = aws_sdk_timestream_write.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
