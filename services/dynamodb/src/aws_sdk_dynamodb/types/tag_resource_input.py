"""Generated from Smithy shape ``com.amazonaws.dynamodb#TagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.resource_arn_string
    import aws_sdk_dynamodb.types.tag_list


class TagResourceInput(TypedDict, closed=True):
    resource_arn: "aws_sdk_dynamodb.types.resource_arn_string.ResourceArnString"
    """<p>Identifies the Amazon DynamoDB resource to which tags should be added. This value is an Amazon Resource Name (ARN).</p>"""
    tags: "aws_sdk_dynamodb.types.tag_list.TagList"
    """<p>The tags to be assigned to the Amazon DynamoDB resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagResourceInput) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import aws_sdk_dynamodb.types.tag_list

    out["Tags"] = aws_sdk_dynamodb.types.tag_list.serialize_aws_json_1_0(value["tags"])
    return out


def deserialize_aws_json_1_0(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("TagResourceInput.resource_arn required")
    if "Tags" in data:
        import aws_sdk_dynamodb.types.tag_list

        out["tags"] = aws_sdk_dynamodb.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    else:
        raise DeserializationError("TagResourceInput.tags required")
    return out
