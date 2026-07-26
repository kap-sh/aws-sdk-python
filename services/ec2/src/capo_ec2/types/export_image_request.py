"""Generated from Smithy shape ``com.amazonaws.ec2#ExportImageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.disk_image_format
    import capo_ec2.types.export_task_s3_location_request
    import capo_ec2.types.image_id
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list


class ExportImageRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>Token to enable idempotency for export image requests.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>A description of the image being exported. The maximum length is 255 characters.</p>"""
    disk_image_format: NotRequired["capo_ec2.types.disk_image_format.DiskImageFormat"]
    """<p>The disk image format.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    image_id: NotRequired["capo_ec2.types.image_id.ImageId"]
    """<p>The ID of the image.</p>"""
    s3_export_location: NotRequired[
        "capo_ec2.types.export_task_s3_location_request.ExportTaskS3LocationRequest"
    ]
    """<p>The Amazon S3 bucket for the destination image. The destination bucket must exist.</p>"""
    role_name: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the role that grants VM Import/Export permission to export images to your Amazon S3 bucket. If this parameter is not specified, the default role is named 'vmimport'.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the export image task during creation.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ExportImageRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "client_token" in value:
        pairs.append((f"{prefix}.ClientToken", str(value["client_token"])))
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "disk_image_format" in value:
        import capo_ec2.types.disk_image_format

        capo_ec2.types.disk_image_format.serialize_ec2_query(
            value["disk_image_format"], pairs, f"{prefix}.DiskImageFormat"
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "image_id" in value:
        pairs.append((f"{prefix}.ImageId", str(value["image_id"])))
    if "s3_export_location" in value:
        import capo_ec2.types.export_task_s3_location_request

        capo_ec2.types.export_task_s3_location_request.serialize_ec2_query(
            value["s3_export_location"], pairs, f"{prefix}.S3ExportLocation"
        )
    if "role_name" in value:
        pairs.append((f"{prefix}.RoleName", str(value["role_name"])))
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{prefix}.TagSpecifications"
        )


def deserialize_ec2_query(el: Element) -> ExportImageRequest:
    out: ExportImageRequest = {}  # type: ignore[typeddict-item]
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_disk_image_format = el.find("DiskImageFormat")
    if child_disk_image_format is not None:
        import capo_ec2.types.disk_image_format

        out["disk_image_format"] = (
            capo_ec2.types.disk_image_format.deserialize_ec2_query(
                child_disk_image_format
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_image_id = el.find("ImageId")
    if child_image_id is not None:
        out["image_id"] = str(child_image_id.text or "")
    child_s3_export_location = el.find("S3ExportLocation")
    if child_s3_export_location is not None:
        import capo_ec2.types.export_task_s3_location_request

        out["s3_export_location"] = (
            capo_ec2.types.export_task_s3_location_request.deserialize_ec2_query(
                child_s3_export_location
            )
        )
    child_role_name = el.find("RoleName")
    if child_role_name is not None:
        out["role_name"] = str(child_role_name.text or "")
    if el.find("TagSpecifications") is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                el, "TagSpecifications"
            )
        )
    return out
