"""Generated from Smithy shape ``com.amazonaws.gamelift#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.amazon_resource_name
    import aws_sdk_gamelift.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: NotRequired[
        "aws_sdk_gamelift.types.amazon_resource_name.AmazonResourceName"
    ]
    r"""<p>The Amazon Resource Name (<a href=\"https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html\">ARN</a>) that uniquely identifies the Amazon GameLift Servers resource that you want to remove tags from. Amazon GameLift Servers includes resource ARNs in the data object for the resource. You can retrieve the ARN by calling a <code>List</code> or <code>Describe</code> operation for the resource type. </p>"""
    tag_keys: NotRequired["aws_sdk_gamelift.types.tag_key_list.TagKeyList"]
    """<p>A list of one or more tag keys to remove from the specified Amazon GameLift Servers resource. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceARN"] = value["resource_arn"]
    if "tag_keys" in value:
        import aws_sdk_gamelift.types.tag_key_list

        out["TagKeys"] = aws_sdk_gamelift.types.tag_key_list.serialize_aws_json_1_1(
            value["tag_keys"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    if "TagKeys" in data:
        import aws_sdk_gamelift.types.tag_key_list

        out["tag_keys"] = aws_sdk_gamelift.types.tag_key_list.deserialize_aws_json_1_1(
            data["TagKeys"]
        )
    return out
