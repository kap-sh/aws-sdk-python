"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#CreateRelationshipRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_channel.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_channel.types.account_id
    import capo_partnercentral_channel.types.association_type
    import capo_partnercentral_channel.types.catalog
    import capo_partnercentral_channel.types.client_token
    import capo_partnercentral_channel.types.program_management_account_identifier
    import capo_partnercentral_channel.types.relationship_display_name
    import capo_partnercentral_channel.types.resale_account_model
    import capo_partnercentral_channel.types.sector
    import capo_partnercentral_channel.types.support_plan
    import capo_partnercentral_channel.types.tag_list


class CreateRelationshipRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_channel.types.catalog.Catalog"
    """<p>The catalog identifier for the relationship.</p>"""
    association_type: (
        "capo_partnercentral_channel.types.association_type.AssociationType"
    )
    """<p>The type of association for the relationship (e.g., reseller, distributor).</p>"""
    program_management_account_identifier: "capo_partnercentral_channel.types.program_management_account_identifier.ProgramManagementAccountIdentifier"
    """<p>The identifier of the program management account for this relationship.</p>"""
    associated_account_id: "capo_partnercentral_channel.types.account_id.AccountId"
    """<p>The AWS account ID to associate in this relationship.</p>"""
    display_name: "capo_partnercentral_channel.types.relationship_display_name.RelationshipDisplayName"
    """<p>A human-readable name for the relationship.</p>"""
    resale_account_model: NotRequired[
        "capo_partnercentral_channel.types.resale_account_model.ResaleAccountModel"
    ]
    """<p>The resale account model for the relationship.</p>"""
    sector: "capo_partnercentral_channel.types.sector.Sector"
    """<p>The business sector for the relationship.</p>"""
    client_token: NotRequired[
        "capo_partnercentral_channel.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>"""
    tags: NotRequired["capo_partnercentral_channel.types.tag_list.TagList"]
    """<p>Key-value pairs to associate with the relationship.</p>"""
    requested_support_plan: NotRequired[
        "capo_partnercentral_channel.types.support_plan.SupportPlan"
    ]
    """<p>The support plan requested for this relationship.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateRelationshipRequest) -> dict:
    out: dict = {}
    out["catalog"] = value["catalog"]
    import capo_partnercentral_channel.types.association_type

    out["associationType"] = (
        capo_partnercentral_channel.types.association_type.serialize_aws_json_1_0(
            value["association_type"]
        )
    )
    out["programManagementAccountIdentifier"] = value[
        "program_management_account_identifier"
    ]
    out["associatedAccountId"] = value["associated_account_id"]
    out["displayName"] = value["display_name"]
    if "resale_account_model" in value:
        import capo_partnercentral_channel.types.resale_account_model

        out["resaleAccountModel"] = (
            capo_partnercentral_channel.types.resale_account_model.serialize_aws_json_1_0(
                value["resale_account_model"]
            )
        )
    import capo_partnercentral_channel.types.sector

    out["sector"] = capo_partnercentral_channel.types.sector.serialize_aws_json_1_0(
        value["sector"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_partnercentral_channel.types.tag_list

        out["tags"] = capo_partnercentral_channel.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    if "requested_support_plan" in value:
        import capo_partnercentral_channel.types.support_plan

        out["requestedSupportPlan"] = (
            capo_partnercentral_channel.types.support_plan.serialize_aws_json_1_0(
                value["requested_support_plan"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateRelationshipRequest:
    out: CreateRelationshipRequest = {}  # type: ignore[typeddict-item]
    if "catalog" in data:
        out["catalog"] = data["catalog"]
    else:
        raise DeserializationError("CreateRelationshipRequest.catalog required")
    if "associationType" in data:
        import capo_partnercentral_channel.types.association_type

        out["association_type"] = (
            capo_partnercentral_channel.types.association_type.deserialize_aws_json_1_0(
                data["associationType"]
            )
        )
    else:
        raise DeserializationError(
            "CreateRelationshipRequest.association_type required"
        )
    if "programManagementAccountIdentifier" in data:
        out["program_management_account_identifier"] = data[
            "programManagementAccountIdentifier"
        ]
    else:
        raise DeserializationError(
            "CreateRelationshipRequest.program_management_account_identifier required"
        )
    if "associatedAccountId" in data:
        out["associated_account_id"] = data["associatedAccountId"]
    else:
        raise DeserializationError(
            "CreateRelationshipRequest.associated_account_id required"
        )
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    else:
        raise DeserializationError("CreateRelationshipRequest.display_name required")
    if "resaleAccountModel" in data:
        import capo_partnercentral_channel.types.resale_account_model

        out["resale_account_model"] = (
            capo_partnercentral_channel.types.resale_account_model.deserialize_aws_json_1_0(
                data["resaleAccountModel"]
            )
        )
    if "sector" in data:
        import capo_partnercentral_channel.types.sector

        out["sector"] = (
            capo_partnercentral_channel.types.sector.deserialize_aws_json_1_0(
                data["sector"]
            )
        )
    else:
        raise DeserializationError("CreateRelationshipRequest.sector required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "tags" in data:
        import capo_partnercentral_channel.types.tag_list

        out["tags"] = (
            capo_partnercentral_channel.types.tag_list.deserialize_aws_json_1_0(
                data["tags"]
            )
        )
    if "requestedSupportPlan" in data:
        import capo_partnercentral_channel.types.support_plan

        out["requested_support_plan"] = (
            capo_partnercentral_channel.types.support_plan.deserialize_aws_json_1_0(
                data["requestedSupportPlan"]
            )
        )
    return out
