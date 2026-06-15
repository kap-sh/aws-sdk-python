"""Generated from Smithy shape ``com.amazonaws.ssoadmin#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.instance_arn
    import aws_sdk_sso_admin.types.tag_list
    import aws_sdk_sso_admin.types.taggable_resource_arn


class TagResourceRequest(TypedDict):
    instance_arn: NotRequired["aws_sdk_sso_admin.types.instance_arn.InstanceArn"]
    r"""<p>The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see <a href=\"/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    resource_arn: "aws_sdk_sso_admin.types.taggable_resource_arn.TaggableResourceArn"
    """<p>The ARN of the resource with the tags to be listed.</p>"""
    tags: "aws_sdk_sso_admin.types.tag_list.TagList"
    """<p>A set of key-value pairs that are used to manage the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    if "instance_arn" in value:
        out["InstanceArn"] = value["instance_arn"]
    out["ResourceArn"] = value["resource_arn"]
    import aws_sdk_sso_admin.types.tag_list

    out["Tags"] = aws_sdk_sso_admin.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "InstanceArn" in data:
        out["instance_arn"] = data["InstanceArn"]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("TagResourceRequest.resource_arn required")
    if "Tags" in data:
        import aws_sdk_sso_admin.types.tag_list

        out["tags"] = aws_sdk_sso_admin.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
