"""Generated from Smithy shape ``com.amazonaws.rekognition#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.resource_arn
    import aws_sdk_rekognition.types.tag_key_list


class UntagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_rekognition.types.resource_arn.ResourceArn"
    """<p> Amazon Resource Name (ARN) of the model, collection, or stream processor that you want to remove the tags from. </p>"""
    tag_keys: "aws_sdk_rekognition.types.tag_key_list.TagKeyList"
    """<p> A list of the tags that you want to remove. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import aws_sdk_rekognition.types.tag_key_list

    out["TagKeys"] = aws_sdk_rekognition.types.tag_key_list.serialize_aws_json_1_1(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("UntagResourceRequest.resource_arn required")
    if "TagKeys" in data:
        import aws_sdk_rekognition.types.tag_key_list

        out["tag_keys"] = (
            aws_sdk_rekognition.types.tag_key_list.deserialize_aws_json_1_1(
                data["TagKeys"]
            )
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out
