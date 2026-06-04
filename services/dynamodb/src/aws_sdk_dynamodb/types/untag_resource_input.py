"""Generated from Smithy shape ``com.amazonaws.dynamodb#UntagResourceInput``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.resource_arn_string
    import aws_sdk_dynamodb.types.tag_key_list


class UntagResourceInput(TypedDict):
    resource_arn: "aws_sdk_dynamodb.types.resource_arn_string.ResourceArnString"
    """<p>The DynamoDB resource that the tags will be removed from. This value is an Amazon Resource Name (ARN).</p>"""
    tag_keys: "aws_sdk_dynamodb.types.tag_key_list.TagKeyList"
    """<p>A list of tag keys. Existing tags of the resource whose keys are members of this list will be removed from the DynamoDB resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UntagResourceInput) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import aws_sdk_dynamodb.types.tag_key_list

    out["TagKeys"] = aws_sdk_dynamodb.types.tag_key_list.serialize_aws_json_1_0(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("UntagResourceInput.resource_arn required")
    if "TagKeys" in data:
        import aws_sdk_dynamodb.types.tag_key_list

        out["tag_keys"] = aws_sdk_dynamodb.types.tag_key_list.deserialize_aws_json_1_0(
            data["TagKeys"]
        )
    else:
        raise DeserializationError("UntagResourceInput.tag_keys required")
    return out
