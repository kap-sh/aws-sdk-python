"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#GetResourceSnapshotResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.aws_account
    import capo_partnercentral_selling.types.aws_account_id_or_alias_list
    import capo_partnercentral_selling.types.catalog_identifier
    import capo_partnercentral_selling.types.date_time
    import capo_partnercentral_selling.types.engagement_identifier
    import capo_partnercentral_selling.types.resource_arn
    import capo_partnercentral_selling.types.resource_identifier
    import capo_partnercentral_selling.types.resource_snapshot_payload
    import capo_partnercentral_selling.types.resource_snapshot_revision
    import capo_partnercentral_selling.types.resource_template_name
    import capo_partnercentral_selling.types.resource_type


class GetResourceSnapshotResponse(TypedDict, closed=True):
    catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p>The catalog in which the snapshot was created. Matches the Catalog specified in the request.</p>"""
    arn: NotRequired["capo_partnercentral_selling.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the resource snapshot.</p>"""
    created_by: NotRequired["capo_partnercentral_selling.types.aws_account.AwsAccount"]
    """<p>The AWS account ID of the principal (user or role) who created the snapshot. This helps in tracking the origin of the snapshot. </p>"""
    created_at: NotRequired["capo_partnercentral_selling.types.date_time.DateTime"]
    r"""<p>The timestamp when the snapshot was created, in ISO 8601 format (e.g., \"2023-06-01T14:30:00Z\"). This allows for precise tracking of when the snapshot was taken. </p>"""
    engagement_id: NotRequired[
        "capo_partnercentral_selling.types.engagement_identifier.EngagementIdentifier"
    ]
    """<p>The identifier of the engagement associated with this snapshot. Matches the EngagementIdentifier specified in the request. </p>"""
    resource_type: NotRequired[
        "capo_partnercentral_selling.types.resource_type.ResourceType"
    ]
    """<p>The type of the resource that was snapshotted. Matches the ResourceType specified in the request.</p>"""
    resource_id: NotRequired[
        "capo_partnercentral_selling.types.resource_identifier.ResourceIdentifier"
    ]
    """<p>The identifier of the specific resource that was snapshotted. Matches the ResourceIdentifier specified in the request.</p>"""
    resource_snapshot_template_name: NotRequired[
        "capo_partnercentral_selling.types.resource_template_name.ResourceTemplateName"
    ]
    """<p>The name of the view used for this snapshot. This is the same as the template name.</p>"""
    revision: NotRequired[
        "capo_partnercentral_selling.types.resource_snapshot_revision.ResourceSnapshotRevision"
    ]
    """<p>The revision number of this snapshot. This is a positive integer that is sequential and unique within the context of a resource view.</p>"""
    payload: NotRequired[
        "capo_partnercentral_selling.types.resource_snapshot_payload.ResourceSnapshotPayload"
    ]
    target_member_accounts: NotRequired[
        "capo_partnercentral_selling.types.aws_account_id_or_alias_list.AwsAccountIdOrAliasList"
    ]
    """<p>Target member accounts associated with the resource snapshot.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetResourceSnapshotResponse) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "created_by" in value:
        out["CreatedBy"] = value["created_by"]
    if "created_at" in value:
        import capo_partnercentral_selling.types.date_time

        out["CreatedAt"] = (
            capo_partnercentral_selling.types.date_time.serialize_aws_json_1_0(
                value["created_at"]
            )
        )
    if "engagement_id" in value:
        out["EngagementId"] = value["engagement_id"]
    if "resource_type" in value:
        import capo_partnercentral_selling.types.resource_type

        out["ResourceType"] = (
            capo_partnercentral_selling.types.resource_type.serialize_aws_json_1_0(
                value["resource_type"]
            )
        )
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "resource_snapshot_template_name" in value:
        out["ResourceSnapshotTemplateName"] = value["resource_snapshot_template_name"]
    if "revision" in value:
        out["Revision"] = value["revision"]
    if "payload" in value:
        import capo_partnercentral_selling.types.resource_snapshot_payload

        out["Payload"] = (
            capo_partnercentral_selling.types.resource_snapshot_payload.serialize_aws_json_1_0(
                value["payload"]
            )
        )
    if "target_member_accounts" in value:
        import capo_partnercentral_selling.types.aws_account_id_or_alias_list

        out["TargetMemberAccounts"] = (
            capo_partnercentral_selling.types.aws_account_id_or_alias_list.serialize_aws_json_1_0(
                value["target_member_accounts"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetResourceSnapshotResponse:
    out: GetResourceSnapshotResponse = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("GetResourceSnapshotResponse.catalog required")
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "CreatedBy" in data:
        out["created_by"] = data["CreatedBy"]
    if "CreatedAt" in data:
        import capo_partnercentral_selling.types.date_time

        out["created_at"] = (
            capo_partnercentral_selling.types.date_time.deserialize_aws_json_1_0(
                data["CreatedAt"]
            )
        )
    if "EngagementId" in data:
        out["engagement_id"] = data["EngagementId"]
    if "ResourceType" in data:
        import capo_partnercentral_selling.types.resource_type

        out["resource_type"] = (
            capo_partnercentral_selling.types.resource_type.deserialize_aws_json_1_0(
                data["ResourceType"]
            )
        )
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    if "ResourceSnapshotTemplateName" in data:
        out["resource_snapshot_template_name"] = data["ResourceSnapshotTemplateName"]
    if "Revision" in data:
        out["revision"] = data["Revision"]
    if "Payload" in data:
        import capo_partnercentral_selling.types.resource_snapshot_payload

        out["payload"] = (
            capo_partnercentral_selling.types.resource_snapshot_payload.deserialize_aws_json_1_0(
                data["Payload"]
            )
        )
    if "TargetMemberAccounts" in data:
        import capo_partnercentral_selling.types.aws_account_id_or_alias_list

        out["target_member_accounts"] = (
            capo_partnercentral_selling.types.aws_account_id_or_alias_list.deserialize_aws_json_1_0(
                data["TargetMemberAccounts"]
            )
        )
    return out
