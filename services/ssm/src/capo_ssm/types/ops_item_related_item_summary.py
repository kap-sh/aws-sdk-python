"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemRelatedItemSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.date_time
    import capo_ssm.types.ops_item_id
    import capo_ssm.types.ops_item_identity
    import capo_ssm.types.ops_item_related_item_association_id
    import capo_ssm.types.ops_item_related_item_association_resource_type
    import capo_ssm.types.ops_item_related_item_association_resource_uri
    import capo_ssm.types.ops_item_related_item_association_type


class OpsItemRelatedItemSummary(TypedDict, closed=True):
    ops_item_id: NotRequired["capo_ssm.types.ops_item_id.OpsItemId"]
    """<p>The OpsItem ID.</p>"""
    association_id: NotRequired[
        "capo_ssm.types.ops_item_related_item_association_id.OpsItemRelatedItemAssociationId"
    ]
    """<p>The association ID.</p>"""
    resource_type: NotRequired[
        "capo_ssm.types.ops_item_related_item_association_resource_type.OpsItemRelatedItemAssociationResourceType"
    ]
    """<p>The resource type.</p>"""
    association_type: NotRequired[
        "capo_ssm.types.ops_item_related_item_association_type.OpsItemRelatedItemAssociationType"
    ]
    """<p>The association type.</p>"""
    resource_uri: NotRequired[
        "capo_ssm.types.ops_item_related_item_association_resource_uri.OpsItemRelatedItemAssociationResourceUri"
    ]
    """<p>The Amazon Resource Name (ARN) of the related-item resource.</p>"""
    created_by: NotRequired["capo_ssm.types.ops_item_identity.OpsItemIdentity"]
    created_time: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The time the related-item association was created.</p>"""
    last_modified_by: NotRequired["capo_ssm.types.ops_item_identity.OpsItemIdentity"]
    last_modified_time: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The time the related-item association was last updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsItemRelatedItemSummary) -> dict:
    out: dict = {}
    if "ops_item_id" in value:
        out["OpsItemId"] = value["ops_item_id"]
    if "association_id" in value:
        out["AssociationId"] = value["association_id"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "association_type" in value:
        out["AssociationType"] = value["association_type"]
    if "resource_uri" in value:
        out["ResourceUri"] = value["resource_uri"]
    if "created_by" in value:
        import capo_ssm.types.ops_item_identity

        out["CreatedBy"] = capo_ssm.types.ops_item_identity.serialize_aws_json_1_1(
            value["created_by"]
        )
    if "created_time" in value:
        import capo_ssm.types.date_time

        out["CreatedTime"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["created_time"]
        )
    if "last_modified_by" in value:
        import capo_ssm.types.ops_item_identity

        out["LastModifiedBy"] = capo_ssm.types.ops_item_identity.serialize_aws_json_1_1(
            value["last_modified_by"]
        )
    if "last_modified_time" in value:
        import capo_ssm.types.date_time

        out["LastModifiedTime"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["last_modified_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OpsItemRelatedItemSummary:
    out: OpsItemRelatedItemSummary = {}  # type: ignore[typeddict-item]
    if "OpsItemId" in data:
        out["ops_item_id"] = data["OpsItemId"]
    if "AssociationId" in data:
        out["association_id"] = data["AssociationId"]
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    if "AssociationType" in data:
        out["association_type"] = data["AssociationType"]
    if "ResourceUri" in data:
        out["resource_uri"] = data["ResourceUri"]
    if "CreatedBy" in data:
        import capo_ssm.types.ops_item_identity

        out["created_by"] = capo_ssm.types.ops_item_identity.deserialize_aws_json_1_1(
            data["CreatedBy"]
        )
    if "CreatedTime" in data:
        import capo_ssm.types.date_time

        out["created_time"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["CreatedTime"]
        )
    if "LastModifiedBy" in data:
        import capo_ssm.types.ops_item_identity

        out["last_modified_by"] = (
            capo_ssm.types.ops_item_identity.deserialize_aws_json_1_1(
                data["LastModifiedBy"]
            )
        )
    if "LastModifiedTime" in data:
        import capo_ssm.types.date_time

        out["last_modified_time"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["LastModifiedTime"]
        )
    return out
