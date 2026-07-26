"""Generated from Smithy shape ``com.amazonaws.fsx#DetachAndDeleteS3AccessPointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.s3_access_point_attachment_lifecycle
    import capo_fsx.types.s3_access_point_attachment_name


class DetachAndDeleteS3AccessPointResponse(TypedDict, closed=True):
    lifecycle: NotRequired[
        "capo_fsx.types.s3_access_point_attachment_lifecycle.S3AccessPointAttachmentLifecycle"
    ]
    """<p>The lifecycle status of the S3 access point attachment.</p>"""
    name: NotRequired[
        "capo_fsx.types.s3_access_point_attachment_name.S3AccessPointAttachmentName"
    ]
    """<p>The name of the S3 access point attachment being deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetachAndDeleteS3AccessPointResponse) -> dict:
    out: dict = {}
    if "lifecycle" in value:
        import capo_fsx.types.s3_access_point_attachment_lifecycle

        out["Lifecycle"] = (
            capo_fsx.types.s3_access_point_attachment_lifecycle.serialize_aws_json_1_1(
                value["lifecycle"]
            )
        )
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DetachAndDeleteS3AccessPointResponse:
    out: DetachAndDeleteS3AccessPointResponse = {}  # type: ignore[typeddict-item]
    if "Lifecycle" in data:
        import capo_fsx.types.s3_access_point_attachment_lifecycle

        out["lifecycle"] = (
            capo_fsx.types.s3_access_point_attachment_lifecycle.deserialize_aws_json_1_1(
                data["Lifecycle"]
            )
        )
    if "Name" in data:
        out["name"] = data["Name"]
    return out
