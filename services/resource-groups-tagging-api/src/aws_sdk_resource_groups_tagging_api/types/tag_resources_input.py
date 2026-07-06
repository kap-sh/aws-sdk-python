"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#TagResourcesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_resource_groups_tagging_api.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resource_groups_tagging_api.types.resource_arn_list_for_tag_untag
    import aws_sdk_resource_groups_tagging_api.types.tag_map


class TagResourcesInput(TypedDict, closed=True):
    resource_arn_list: "aws_sdk_resource_groups_tagging_api.types.resource_arn_list_for_tag_untag.ResourceARNListForTagUntag"
    r"""<p>Specifies the list of ARNs of the resources that you want to apply tags to.</p> <p>An ARN (Amazon Resource Name) uniquely identifies a resource. For more information, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    tags: "aws_sdk_resource_groups_tagging_api.types.tag_map.TagMap"
    """<p>Specifies a list of tags that you want to add to the specified resources. A tag consists of a key and a value that you define.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourcesInput) -> dict:
    out: dict = {}
    import aws_sdk_resource_groups_tagging_api.types.resource_arn_list_for_tag_untag

    out["ResourceARNList"] = (
        aws_sdk_resource_groups_tagging_api.types.resource_arn_list_for_tag_untag.serialize_aws_json_1_1(
            value["resource_arn_list"]
        )
    )
    import aws_sdk_resource_groups_tagging_api.types.tag_map

    out["Tags"] = (
        aws_sdk_resource_groups_tagging_api.types.tag_map.serialize_aws_json_1_1(
            value["tags"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourcesInput:
    out: TagResourcesInput = {}  # type: ignore[typeddict-item]
    if "ResourceARNList" in data:
        import aws_sdk_resource_groups_tagging_api.types.resource_arn_list_for_tag_untag

        out["resource_arn_list"] = (
            aws_sdk_resource_groups_tagging_api.types.resource_arn_list_for_tag_untag.deserialize_aws_json_1_1(
                data["ResourceARNList"]
            )
        )
    else:
        raise DeserializationError("TagResourcesInput.resource_arn_list required")
    if "Tags" in data:
        import aws_sdk_resource_groups_tagging_api.types.tag_map

        out["tags"] = (
            aws_sdk_resource_groups_tagging_api.types.tag_map.deserialize_aws_json_1_1(
                data["Tags"]
            )
        )
    else:
        raise DeserializationError("TagResourcesInput.tags required")
    return out
