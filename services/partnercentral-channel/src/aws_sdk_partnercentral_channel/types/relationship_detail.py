"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#RelationshipDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_partnercentral_channel.types.account_id
    import aws_sdk_partnercentral_channel.types.arn
    import aws_sdk_partnercentral_channel.types.association_type
    import aws_sdk_partnercentral_channel.types.catalog
    import aws_sdk_partnercentral_channel.types.date_time
    import aws_sdk_partnercentral_channel.types.program_management_account_id
    import aws_sdk_partnercentral_channel.types.relationship_display_name
    import aws_sdk_partnercentral_channel.types.relationship_id
    import aws_sdk_partnercentral_channel.types.resale_account_model
    import aws_sdk_partnercentral_channel.types.revision
    import aws_sdk_partnercentral_channel.types.sector


class RelationshipDetail(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_partnercentral_channel.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the relationship.</p>"""
    id: NotRequired[
        "aws_sdk_partnercentral_channel.types.relationship_id.RelationshipId"
    ]
    """<p>The unique identifier of the relationship.</p>"""
    revision: NotRequired["aws_sdk_partnercentral_channel.types.revision.Revision"]
    """<p>The current revision number of the relationship.</p>"""
    catalog: NotRequired["aws_sdk_partnercentral_channel.types.catalog.Catalog"]
    """<p>The catalog identifier associated with the relationship.</p>"""
    association_type: NotRequired[
        "aws_sdk_partnercentral_channel.types.association_type.AssociationType"
    ]
    """<p>The type of association for the relationship.</p>"""
    program_management_account_id: NotRequired[
        "aws_sdk_partnercentral_channel.types.program_management_account_id.ProgramManagementAccountId"
    ]
    """<p>The identifier of the program management account.</p>"""
    associated_account_id: NotRequired[
        "aws_sdk_partnercentral_channel.types.account_id.AccountId"
    ]
    """<p>The AWS account ID associated in this relationship.</p>"""
    display_name: NotRequired[
        "aws_sdk_partnercentral_channel.types.relationship_display_name.RelationshipDisplayName"
    ]
    """<p>The display name of the relationship.</p>"""
    resale_account_model: NotRequired[
        "aws_sdk_partnercentral_channel.types.resale_account_model.ResaleAccountModel"
    ]
    """<p>The resale account model for the relationship.</p>"""
    sector: NotRequired["aws_sdk_partnercentral_channel.types.sector.Sector"]
    """<p>The business sector for the relationship.</p>"""
    created_at: NotRequired["aws_sdk_partnercentral_channel.types.date_time.DateTime"]
    """<p>The timestamp when the relationship was created.</p>"""
    updated_at: NotRequired["aws_sdk_partnercentral_channel.types.date_time.DateTime"]
    """<p>The timestamp when the relationship was last updated.</p>"""
    start_date: NotRequired["aws_sdk_partnercentral_channel.types.date_time.DateTime"]
    """<p>The start date of the relationship.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RelationshipDetail) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "id" in value:
        out["id"] = value["id"]
    if "revision" in value:
        out["revision"] = value["revision"]
    if "catalog" in value:
        out["catalog"] = value["catalog"]
    if "association_type" in value:
        import aws_sdk_partnercentral_channel.types.association_type

        out["associationType"] = (
            aws_sdk_partnercentral_channel.types.association_type.serialize_aws_json_1_0(
                value["association_type"]
            )
        )
    if "program_management_account_id" in value:
        out["programManagementAccountId"] = value["program_management_account_id"]
    if "associated_account_id" in value:
        out["associatedAccountId"] = value["associated_account_id"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "resale_account_model" in value:
        import aws_sdk_partnercentral_channel.types.resale_account_model

        out["resaleAccountModel"] = (
            aws_sdk_partnercentral_channel.types.resale_account_model.serialize_aws_json_1_0(
                value["resale_account_model"]
            )
        )
    if "sector" in value:
        import aws_sdk_partnercentral_channel.types.sector

        out["sector"] = (
            aws_sdk_partnercentral_channel.types.sector.serialize_aws_json_1_0(
                value["sector"]
            )
        )
    if "created_at" in value:
        import aws_sdk_partnercentral_channel.types.date_time

        out["createdAt"] = (
            aws_sdk_partnercentral_channel.types.date_time.serialize_aws_json_1_0(
                value["created_at"]
            )
        )
    if "updated_at" in value:
        import aws_sdk_partnercentral_channel.types.date_time

        out["updatedAt"] = (
            aws_sdk_partnercentral_channel.types.date_time.serialize_aws_json_1_0(
                value["updated_at"]
            )
        )
    if "start_date" in value:
        import aws_sdk_partnercentral_channel.types.date_time

        out["startDate"] = (
            aws_sdk_partnercentral_channel.types.date_time.serialize_aws_json_1_0(
                value["start_date"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RelationshipDetail:
    out: RelationshipDetail = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "id" in data:
        out["id"] = data["id"]
    if "revision" in data:
        out["revision"] = data["revision"]
    if "catalog" in data:
        out["catalog"] = data["catalog"]
    if "associationType" in data:
        import aws_sdk_partnercentral_channel.types.association_type

        out["association_type"] = (
            aws_sdk_partnercentral_channel.types.association_type.deserialize_aws_json_1_0(
                data["associationType"]
            )
        )
    if "programManagementAccountId" in data:
        out["program_management_account_id"] = data["programManagementAccountId"]
    if "associatedAccountId" in data:
        out["associated_account_id"] = data["associatedAccountId"]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "resaleAccountModel" in data:
        import aws_sdk_partnercentral_channel.types.resale_account_model

        out["resale_account_model"] = (
            aws_sdk_partnercentral_channel.types.resale_account_model.deserialize_aws_json_1_0(
                data["resaleAccountModel"]
            )
        )
    if "sector" in data:
        import aws_sdk_partnercentral_channel.types.sector

        out["sector"] = (
            aws_sdk_partnercentral_channel.types.sector.deserialize_aws_json_1_0(
                data["sector"]
            )
        )
    if "createdAt" in data:
        import aws_sdk_partnercentral_channel.types.date_time

        out["created_at"] = (
            aws_sdk_partnercentral_channel.types.date_time.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    if "updatedAt" in data:
        import aws_sdk_partnercentral_channel.types.date_time

        out["updated_at"] = (
            aws_sdk_partnercentral_channel.types.date_time.deserialize_aws_json_1_0(
                data["updatedAt"]
            )
        )
    if "startDate" in data:
        import aws_sdk_partnercentral_channel.types.date_time

        out["start_date"] = (
            aws_sdk_partnercentral_channel.types.date_time.deserialize_aws_json_1_0(
                data["startDate"]
            )
        )
    return out
