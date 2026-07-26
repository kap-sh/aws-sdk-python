"""Generated from Smithy shape ``com.amazonaws.ec2#CreateRestoreImageTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.image_name_request
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list


class CreateRestoreImageTaskRequest(TypedDict, closed=True):
    bucket: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the Amazon S3 bucket that contains the stored AMI object.</p>"""
    object_key: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the stored AMI object in the bucket.</p>"""
    name: NotRequired["capo_ec2.types.image_name_request.ImageNameRequest"]
    """<p>The name for the restored AMI. The name must be unique for AMIs in the Region for this account. If you do not provide a name, the new AMI gets the same name as the original AMI.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the AMI and snapshots on restoration. You can tag the AMI, the snapshots, or both.</p> <ul> <li> <p>To tag the AMI, the value for <code>ResourceType</code> must be <code>image</code>.</p> </li> <li> <p>To tag the snapshots, the value for <code>ResourceType</code> must be <code>snapshot</code>. The same tag is applied to all of the snapshots that are created.</p> </li> </ul>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateRestoreImageTaskRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "bucket" in value:
        pairs.append((f"{prefix}.Bucket", str(value["bucket"])))
    if "object_key" in value:
        pairs.append((f"{prefix}.ObjectKey", str(value["object_key"])))
    if "name" in value:
        pairs.append((f"{prefix}.Name", str(value["name"])))
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{prefix}.TagSpecifications"
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> CreateRestoreImageTaskRequest:
    out: CreateRestoreImageTaskRequest = {}  # type: ignore[typeddict-item]
    child_bucket = el.find("Bucket")
    if child_bucket is not None:
        out["bucket"] = str(child_bucket.text or "")
    child_object_key = el.find("ObjectKey")
    if child_object_key is not None:
        out["object_key"] = str(child_object_key.text or "")
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    if el.find("TagSpecifications") is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                el, "TagSpecifications"
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
