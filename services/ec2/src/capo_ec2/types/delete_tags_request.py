"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteTagsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.resource_id_list
    import capo_ec2.types.tag_list


class DeleteTagsRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    resources: NotRequired["capo_ec2.types.resource_id_list.ResourceIdList"]
    """<p>The IDs of the resources, separated by spaces.</p> <p>Constraints: Up to 1000 resource IDs. We recommend breaking up this request into smaller batches.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The tags to delete. Specify a tag key and an optional tag value to delete specific tags. If you specify a tag key without a tag value, we delete any tag with this key regardless of its value. If you specify a tag key with an empty string as the tag value, we delete the tag only if its value is an empty string.</p> <p>If you omit this parameter, we delete all user-defined tags for the specified resources. We do not delete Amazon Web Services-generated tags (tags that have the <code>aws:</code> prefix).</p> <p>Constraints: Up to 1000 tags.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteTagsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "resources" in value:
        import capo_ec2.types.resource_id_list

        capo_ec2.types.resource_id_list.serialize_ec2_query(
            value["resources"], pairs, f"{key_prefix}ResourceId"
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}Tag"
        )


def deserialize_ec2_query(el: Element) -> DeleteTagsRequest:
    out: DeleteTagsRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("dryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    if el.find("resourceId") is not None:
        import capo_ec2.types.resource_id_list

        out["resources"] = capo_ec2.types.resource_id_list.deserialize_ec2_query(
            el, "resourceId"
        )
    if el.find("tag") is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(el, "tag")
    return out
