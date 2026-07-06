"""Generated from Smithy shape ``com.amazonaws.emr#RemoveTagsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr.types.cluster_id
    import aws_sdk_emr.types.resource_id
    import aws_sdk_emr.types.string_list


class RemoveTagsInput(TypedDict, closed=True):
    resource_id: NotRequired["aws_sdk_emr.types.resource_id.ResourceId"]
    """<p>The Amazon EMR resource identifier from which tags will be removed. For example, a cluster identifier or an Amazon EMR Studio ID.</p>"""
    tag_keys: NotRequired["aws_sdk_emr.types.string_list.StringList"]
    """<p>A list of tag keys to remove from the resource.</p>"""
    cluster_id: NotRequired["aws_sdk_emr.types.cluster_id.ClusterId"]
    """<p>The ID of the cluster that scopes the tag operation. Required when the resource being untagged is a session-scoped resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoveTagsInput) -> dict:
    out: dict = {}
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "tag_keys" in value:
        import aws_sdk_emr.types.string_list

        out["TagKeys"] = aws_sdk_emr.types.string_list.serialize_aws_json_1_1(
            value["tag_keys"]
        )
    if "cluster_id" in value:
        out["ClusterId"] = value["cluster_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RemoveTagsInput:
    out: RemoveTagsInput = {}  # type: ignore[typeddict-item]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    if "TagKeys" in data:
        import aws_sdk_emr.types.string_list

        out["tag_keys"] = aws_sdk_emr.types.string_list.deserialize_aws_json_1_1(
            data["TagKeys"]
        )
    if "ClusterId" in data:
        out["cluster_id"] = data["ClusterId"]
    return out
