"""Generated from Smithy shape ``com.amazonaws.emr#AddTagsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.cluster_id
    import capo_emr.types.resource_id
    import capo_emr.types.tag_list


class AddTagsInput(TypedDict, closed=True):
    resource_id: NotRequired["capo_emr.types.resource_id.ResourceId"]
    """<p>The Amazon EMR resource identifier to which tags will be added. For example, a cluster identifier or an Amazon EMR Studio ID.</p>"""
    tags: NotRequired["capo_emr.types.tag_list.TagList"]
    """<p>A list of tags to associate with a resource. Tags are user-defined key-value pairs that consist of a required key string with a maximum of 128 characters, and an optional value string with a maximum of 256 characters.</p>"""
    cluster_id: NotRequired["capo_emr.types.cluster_id.ClusterId"]
    """<p>The ID of the cluster that scopes the tag operation. Required when the resource being tagged is a session-scoped resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddTagsInput) -> dict:
    out: dict = {}
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "tags" in value:
        import capo_emr.types.tag_list

        out["Tags"] = capo_emr.types.tag_list.serialize_aws_json_1_1(value["tags"])
    if "cluster_id" in value:
        out["ClusterId"] = value["cluster_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AddTagsInput:
    out: AddTagsInput = {}  # type: ignore[typeddict-item]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    if "Tags" in data:
        import capo_emr.types.tag_list

        out["tags"] = capo_emr.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    if "ClusterId" in data:
        out["cluster_id"] = data["ClusterId"]
    return out
