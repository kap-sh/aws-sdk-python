"""Generated from Smithy shape ``com.amazonaws.ec2#CreateTagsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.resource_id_list
    import aws_sdk_ec2.types.tag_list


class CreateTagsRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    resources: NotRequired["aws_sdk_ec2.types.resource_id_list.ResourceIdList"]
    """<p>The IDs of the resources, separated by spaces.</p> <p>Constraints: Up to 1000 resource IDs. We recommend breaking up this request into smaller batches.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags. The <code>value</code> parameter is required, but if you don't want the tag to have a value, specify the parameter with no value, and we set the value to an empty string.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateTagsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "resources" in value:
        import aws_sdk_ec2.types.resource_id_list

        aws_sdk_ec2.types.resource_id_list.serialize_ec2_query(
            value["resources"], pairs, f"{prefix}.Resources"
        )
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )


def deserialize_ec2_query(el: Element) -> CreateTagsRequest:
    out: CreateTagsRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    if el.find("Resources") is not None:
        import aws_sdk_ec2.types.resource_id_list

        out["resources"] = aws_sdk_ec2.types.resource_id_list.deserialize_ec2_query(
            el, "Resources"
        )
    if el.find("Tags") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "Tags")
    return out
