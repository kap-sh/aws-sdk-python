"""Generated from Smithy shape ``com.amazonaws.rekognition#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.resource_arn
    import aws_sdk_rekognition.types.tag_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_rekognition.types.resource_arn.ResourceArn"
    """<p> Amazon Resource Name (ARN) of the model, collection, or stream processor that you want to assign the tags to. </p>"""
    tags: "aws_sdk_rekognition.types.tag_map.TagMap"
    """<p> The key-value tags to assign to the resource. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import aws_sdk_rekognition.types.tag_map

    out["Tags"] = aws_sdk_rekognition.types.tag_map.serialize_aws_json_1_1(
        value["tags"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("TagResourceRequest.resource_arn required")
    if "Tags" in data:
        import aws_sdk_rekognition.types.tag_map

        out["tags"] = aws_sdk_rekognition.types.tag_map.deserialize_aws_json_1_1(
            data["Tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
