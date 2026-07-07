"""Generated from Smithy shape ``com.amazonaws.kendra#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.amazon_resource_name
    import aws_sdk_kendra.types.tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_kendra.types.amazon_resource_name.AmazonResourceName"
    r"""<p>The Amazon Resource Name (ARN) of the index, FAQ, data source, or other resource to add a tag. For example, the ARN of an index is constructed as follows: <i>arn:aws:kendra:your-region:your-account-id:index/index-id</i> For information on how to construct an ARN for all types of Amazon Kendra resources, see <a href=\"https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonkendra.html#amazonkendra-resources-for-iam-policies\">Resource types</a>.</p>"""
    tags: "aws_sdk_kendra.types.tag_list.TagList"
    """<p>A list of tag keys to add to the index, FAQ, data source, or other resource. If a tag already exists, the existing value is replaced with the new value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import aws_sdk_kendra.types.tag_list

    out["Tags"] = aws_sdk_kendra.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("TagResourceRequest.resource_arn required")
    if "Tags" in data:
        import aws_sdk_kendra.types.tag_list

        out["tags"] = aws_sdk_kendra.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
