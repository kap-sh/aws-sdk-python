"""Generated from Smithy shape ``com.amazonaws.fsx#S3AccessPointAttachment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fsx.types.creation_time
    import aws_sdk_fsx.types.lifecycle_transition_reason
    import aws_sdk_fsx.types.s3_access_point
    import aws_sdk_fsx.types.s3_access_point_attachment_lifecycle
    import aws_sdk_fsx.types.s3_access_point_attachment_name
    import aws_sdk_fsx.types.s3_access_point_attachment_type
    import aws_sdk_fsx.types.s3_access_point_ontap_configuration
    import aws_sdk_fsx.types.s3_access_point_open_zfs_configuration


class S3AccessPointAttachment(TypedDict, closed=True):
    lifecycle: NotRequired[
        "aws_sdk_fsx.types.s3_access_point_attachment_lifecycle.S3AccessPointAttachmentLifecycle"
    ]
    """<p>The lifecycle status of the S3 access point attachment. The lifecycle can have the following values:</p> <ul> <li> <p>AVAILABLE - the S3 access point attachment is available for use</p> </li> <li> <p>CREATING - Amazon FSx is creating the S3 access point and attachment</p> </li> <li> <p>DELETING - Amazon FSx is deleting the S3 access point and attachment</p> </li> <li> <p>FAILED - The S3 access point attachment is in a failed state. Delete and detach the S3 access point attachment, and create a new one.</p> </li> <li> <p>UPDATING - Amazon FSx is updating the S3 access point attachment</p> </li> </ul>"""
    lifecycle_transition_reason: NotRequired[
        "aws_sdk_fsx.types.lifecycle_transition_reason.LifecycleTransitionReason"
    ]
    creation_time: NotRequired["aws_sdk_fsx.types.creation_time.CreationTime"]
    name: NotRequired[
        "aws_sdk_fsx.types.s3_access_point_attachment_name.S3AccessPointAttachmentName"
    ]
    """<p>The name of the S3 access point attachment; also used for the name of the S3 access point.</p>"""
    type: NotRequired[
        "aws_sdk_fsx.types.s3_access_point_attachment_type.S3AccessPointAttachmentType"
    ]
    """<p>The type of Amazon FSx volume that the S3 access point is attached to. </p>"""
    open_zfs_configuration: NotRequired[
        "aws_sdk_fsx.types.s3_access_point_open_zfs_configuration.S3AccessPointOpenZFSConfiguration"
    ]
    """<p>The OpenZFSConfiguration of the S3 access point attachment.</p>"""
    ontap_configuration: NotRequired[
        "aws_sdk_fsx.types.s3_access_point_ontap_configuration.S3AccessPointOntapConfiguration"
    ]
    """<p>The ONTAP configuration of the S3 access point attachment.</p>"""
    s3_access_point: NotRequired["aws_sdk_fsx.types.s3_access_point.S3AccessPoint"]
    """<p>The S3 access point configuration of the S3 access point attachment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3AccessPointAttachment) -> dict:
    out: dict = {}
    if "lifecycle" in value:
        import aws_sdk_fsx.types.s3_access_point_attachment_lifecycle

        out["Lifecycle"] = (
            aws_sdk_fsx.types.s3_access_point_attachment_lifecycle.serialize_aws_json_1_1(
                value["lifecycle"]
            )
        )
    if "lifecycle_transition_reason" in value:
        import aws_sdk_fsx.types.lifecycle_transition_reason

        out["LifecycleTransitionReason"] = (
            aws_sdk_fsx.types.lifecycle_transition_reason.serialize_aws_json_1_1(
                value["lifecycle_transition_reason"]
            )
        )
    if "creation_time" in value:
        import aws_sdk_fsx.types.creation_time

        out["CreationTime"] = aws_sdk_fsx.types.creation_time.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "type" in value:
        import aws_sdk_fsx.types.s3_access_point_attachment_type

        out["Type"] = (
            aws_sdk_fsx.types.s3_access_point_attachment_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "open_zfs_configuration" in value:
        import aws_sdk_fsx.types.s3_access_point_open_zfs_configuration

        out["OpenZFSConfiguration"] = (
            aws_sdk_fsx.types.s3_access_point_open_zfs_configuration.serialize_aws_json_1_1(
                value["open_zfs_configuration"]
            )
        )
    if "ontap_configuration" in value:
        import aws_sdk_fsx.types.s3_access_point_ontap_configuration

        out["OntapConfiguration"] = (
            aws_sdk_fsx.types.s3_access_point_ontap_configuration.serialize_aws_json_1_1(
                value["ontap_configuration"]
            )
        )
    if "s3_access_point" in value:
        import aws_sdk_fsx.types.s3_access_point

        out["S3AccessPoint"] = aws_sdk_fsx.types.s3_access_point.serialize_aws_json_1_1(
            value["s3_access_point"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> S3AccessPointAttachment:
    out: S3AccessPointAttachment = {}  # type: ignore[typeddict-item]
    if "Lifecycle" in data:
        import aws_sdk_fsx.types.s3_access_point_attachment_lifecycle

        out["lifecycle"] = (
            aws_sdk_fsx.types.s3_access_point_attachment_lifecycle.deserialize_aws_json_1_1(
                data["Lifecycle"]
            )
        )
    if "LifecycleTransitionReason" in data:
        import aws_sdk_fsx.types.lifecycle_transition_reason

        out["lifecycle_transition_reason"] = (
            aws_sdk_fsx.types.lifecycle_transition_reason.deserialize_aws_json_1_1(
                data["LifecycleTransitionReason"]
            )
        )
    if "CreationTime" in data:
        import aws_sdk_fsx.types.creation_time

        out["creation_time"] = aws_sdk_fsx.types.creation_time.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "Type" in data:
        import aws_sdk_fsx.types.s3_access_point_attachment_type

        out["type"] = (
            aws_sdk_fsx.types.s3_access_point_attachment_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if "OpenZFSConfiguration" in data:
        import aws_sdk_fsx.types.s3_access_point_open_zfs_configuration

        out["open_zfs_configuration"] = (
            aws_sdk_fsx.types.s3_access_point_open_zfs_configuration.deserialize_aws_json_1_1(
                data["OpenZFSConfiguration"]
            )
        )
    if "OntapConfiguration" in data:
        import aws_sdk_fsx.types.s3_access_point_ontap_configuration

        out["ontap_configuration"] = (
            aws_sdk_fsx.types.s3_access_point_ontap_configuration.deserialize_aws_json_1_1(
                data["OntapConfiguration"]
            )
        )
    if "S3AccessPoint" in data:
        import aws_sdk_fsx.types.s3_access_point

        out["s3_access_point"] = (
            aws_sdk_fsx.types.s3_access_point.deserialize_aws_json_1_1(
                data["S3AccessPoint"]
            )
        )
    return out
