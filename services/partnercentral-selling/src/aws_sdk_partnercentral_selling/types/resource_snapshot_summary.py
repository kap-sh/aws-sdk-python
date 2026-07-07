"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ResourceSnapshotSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.aws_account
    import aws_sdk_partnercentral_selling.types.resource_identifier
    import aws_sdk_partnercentral_selling.types.resource_snapshot_arn
    import aws_sdk_partnercentral_selling.types.resource_snapshot_revision
    import aws_sdk_partnercentral_selling.types.resource_template_name
    import aws_sdk_partnercentral_selling.types.resource_type


class ResourceSnapshotSummary(TypedDict, closed=True):
    arn: NotRequired[
        "aws_sdk_partnercentral_selling.types.resource_snapshot_arn.ResourceSnapshotArn"
    ]
    """<p> The Amazon Resource Name (ARN) of the snapshot. This globally unique identifier can be used for cross-service references and in IAM policies. </p>"""
    revision: NotRequired[
        "aws_sdk_partnercentral_selling.types.resource_snapshot_revision.ResourceSnapshotRevision"
    ]
    """<p>The revision number of the snapshot. This integer value is incremented each time the snapshot is updated, allowing for version tracking of the resource snapshot. </p>"""
    resource_type: NotRequired[
        "aws_sdk_partnercentral_selling.types.resource_type.ResourceType"
    ]
    """<p>The type of resource snapshotted.</p>"""
    resource_id: NotRequired[
        "aws_sdk_partnercentral_selling.types.resource_identifier.ResourceIdentifier"
    ]
    """<p>The identifier of the specific resource snapshotted. The format might vary depending on the ResourceType. </p>"""
    resource_snapshot_template_name: NotRequired[
        "aws_sdk_partnercentral_selling.types.resource_template_name.ResourceTemplateName"
    ]
    """<p>The name of the template used to create the snapshot.</p>"""
    created_by: NotRequired[
        "aws_sdk_partnercentral_selling.types.aws_account.AwsAccount"
    ]
    """<p>The AWS account ID of the entity that owns the resource from which the snapshot was created.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceSnapshotSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "revision" in value:
        out["Revision"] = value["revision"]
    if "resource_type" in value:
        import aws_sdk_partnercentral_selling.types.resource_type

        out["ResourceType"] = (
            aws_sdk_partnercentral_selling.types.resource_type.serialize_aws_json_1_0(
                value["resource_type"]
            )
        )
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "resource_snapshot_template_name" in value:
        out["ResourceSnapshotTemplateName"] = value["resource_snapshot_template_name"]
    if "created_by" in value:
        out["CreatedBy"] = value["created_by"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ResourceSnapshotSummary:
    out: ResourceSnapshotSummary = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Revision" in data:
        out["revision"] = data["Revision"]
    if "ResourceType" in data:
        import aws_sdk_partnercentral_selling.types.resource_type

        out["resource_type"] = (
            aws_sdk_partnercentral_selling.types.resource_type.deserialize_aws_json_1_0(
                data["ResourceType"]
            )
        )
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    if "ResourceSnapshotTemplateName" in data:
        out["resource_snapshot_template_name"] = data["ResourceSnapshotTemplateName"]
    if "CreatedBy" in data:
        out["created_by"] = data["CreatedBy"]
    return out
