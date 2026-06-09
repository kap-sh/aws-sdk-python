"""Generated from Smithy shape ``com.amazonaws.ec2#CreateStoreImageTaskRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.image_id
    import aws_sdk_ec2.types.s3_object_tag_list
    import aws_sdk_ec2.types.string


class CreateStoreImageTaskRequest(TypedDict):
    image_id: NotRequired["aws_sdk_ec2.types.image_id.ImageId"]
    """<p>The ID of the AMI.</p>"""
    bucket: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the Amazon S3 bucket in which the AMI object will be stored. The bucket must be in the Region in which the request is being made. The AMI object appears in the bucket only after the upload task has completed. </p>"""
    s3_object_tags: NotRequired["aws_sdk_ec2.types.s3_object_tag_list.S3ObjectTagList"]
    """<p>The tags to apply to the AMI object that will be stored in the Amazon S3 bucket. </p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateStoreImageTaskRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "image_id" in value:
        pairs.append((f"{prefix}.ImageId", str(value["image_id"])))
    if "bucket" in value:
        pairs.append((f"{prefix}.Bucket", str(value["bucket"])))
    if "s3_object_tags" in value:
        import aws_sdk_ec2.types.s3_object_tag_list

        aws_sdk_ec2.types.s3_object_tag_list.serialize_ec2_query(
            value["s3_object_tags"], pairs, f"{prefix}.S3ObjectTags"
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> CreateStoreImageTaskRequest:
    out: CreateStoreImageTaskRequest = {}  # type: ignore[typeddict-item]
    child_image_id = el.find("ImageId")
    if child_image_id is not None:
        out["image_id"] = str(child_image_id.text or "")
    child_bucket = el.find("Bucket")
    if child_bucket is not None:
        out["bucket"] = str(child_bucket.text or "")
    if el.find("S3ObjectTags") is not None:
        import aws_sdk_ec2.types.s3_object_tag_list

        out["s3_object_tags"] = (
            aws_sdk_ec2.types.s3_object_tag_list.deserialize_ec2_query(
                el, "S3ObjectTags"
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
