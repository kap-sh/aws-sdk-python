"""Generated from Smithy shape ``com.amazonaws.fsx#CreateAndAttachS3AccessPointRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.client_request_token
    import aws_sdk_fsx.types.create_and_attach_s3_access_point_ontap_configuration
    import aws_sdk_fsx.types.create_and_attach_s3_access_point_open_zfs_configuration
    import aws_sdk_fsx.types.create_and_attach_s3_access_point_s3_configuration
    import aws_sdk_fsx.types.s3_access_point_attachment_name
    import aws_sdk_fsx.types.s3_access_point_attachment_type


class CreateAndAttachS3AccessPointRequest(TypedDict):
    client_request_token: NotRequired[
        "aws_sdk_fsx.types.client_request_token.ClientRequestToken"
    ]
    name: NotRequired[
        "aws_sdk_fsx.types.s3_access_point_attachment_name.S3AccessPointAttachmentName"
    ]
    """<p>The name you want to assign to this S3 access point.</p>"""
    type: NotRequired[
        "aws_sdk_fsx.types.s3_access_point_attachment_type.S3AccessPointAttachmentType"
    ]
    """<p>The type of S3 access point you want to create. Only <code>OpenZFS</code> is supported.</p>"""
    open_zfs_configuration: NotRequired[
        "aws_sdk_fsx.types.create_and_attach_s3_access_point_open_zfs_configuration.CreateAndAttachS3AccessPointOpenZFSConfiguration"
    ]
    """<p>Specifies the configuration to use when creating and attaching an S3 access point to an FSx for OpenZFS volume.</p>"""
    ontap_configuration: NotRequired[
        "aws_sdk_fsx.types.create_and_attach_s3_access_point_ontap_configuration.CreateAndAttachS3AccessPointOntapConfiguration"
    ]
    s3_access_point: NotRequired[
        "aws_sdk_fsx.types.create_and_attach_s3_access_point_s3_configuration.CreateAndAttachS3AccessPointS3Configuration"
    ]
    """<p>Specifies the virtual private cloud (VPC) configuration if you're creating an access point that is restricted to a VPC. For more information, see <a href=\"https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/access-points-vpc.html\">Creating access points restricted to a virtual private cloud</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAndAttachS3AccessPointRequest) -> dict:
    out: dict = {}
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
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
        import aws_sdk_fsx.types.create_and_attach_s3_access_point_open_zfs_configuration

        out["OpenZFSConfiguration"] = (
            aws_sdk_fsx.types.create_and_attach_s3_access_point_open_zfs_configuration.serialize_aws_json_1_1(
                value["open_zfs_configuration"]
            )
        )
    if "ontap_configuration" in value:
        import aws_sdk_fsx.types.create_and_attach_s3_access_point_ontap_configuration

        out["OntapConfiguration"] = (
            aws_sdk_fsx.types.create_and_attach_s3_access_point_ontap_configuration.serialize_aws_json_1_1(
                value["ontap_configuration"]
            )
        )
    if "s3_access_point" in value:
        import aws_sdk_fsx.types.create_and_attach_s3_access_point_s3_configuration

        out["S3AccessPoint"] = (
            aws_sdk_fsx.types.create_and_attach_s3_access_point_s3_configuration.serialize_aws_json_1_1(
                value["s3_access_point"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAndAttachS3AccessPointRequest:
    out: CreateAndAttachS3AccessPointRequest = {}  # type: ignore[typeddict-item]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
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
        import aws_sdk_fsx.types.create_and_attach_s3_access_point_open_zfs_configuration

        out["open_zfs_configuration"] = (
            aws_sdk_fsx.types.create_and_attach_s3_access_point_open_zfs_configuration.deserialize_aws_json_1_1(
                data["OpenZFSConfiguration"]
            )
        )
    if "OntapConfiguration" in data:
        import aws_sdk_fsx.types.create_and_attach_s3_access_point_ontap_configuration

        out["ontap_configuration"] = (
            aws_sdk_fsx.types.create_and_attach_s3_access_point_ontap_configuration.deserialize_aws_json_1_1(
                data["OntapConfiguration"]
            )
        )
    if "S3AccessPoint" in data:
        import aws_sdk_fsx.types.create_and_attach_s3_access_point_s3_configuration

        out["s3_access_point"] = (
            aws_sdk_fsx.types.create_and_attach_s3_access_point_s3_configuration.deserialize_aws_json_1_1(
                data["S3AccessPoint"]
            )
        )
    return out
