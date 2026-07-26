"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#GetBenefitAllocationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_benefits.types.benefit_allocation_arn
    import capo_partnercentral_benefits.types.benefit_allocation_id
    import capo_partnercentral_benefits.types.benefit_allocation_status
    import capo_partnercentral_benefits.types.benefit_application_id
    import capo_partnercentral_benefits.types.benefit_id
    import capo_partnercentral_benefits.types.benefit_identifiers
    import capo_partnercentral_benefits.types.catalog_name
    import capo_partnercentral_benefits.types.fulfillment_details
    import capo_partnercentral_benefits.types.fulfillment_type
    import capo_partnercentral_benefits.types.timestamp


class GetBenefitAllocationOutput(TypedDict, closed=True):
    id: NotRequired[
        "capo_partnercentral_benefits.types.benefit_allocation_id.BenefitAllocationId"
    ]
    """<p>The unique identifier of the benefit allocation.</p>"""
    catalog: NotRequired["capo_partnercentral_benefits.types.catalog_name.CatalogName"]
    """<p>The catalog identifier that the benefit allocation belongs to.</p>"""
    arn: NotRequired[
        "capo_partnercentral_benefits.types.benefit_allocation_arn.BenefitAllocationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the benefit allocation.</p>"""
    name: NotRequired["str"]
    """<p>The human-readable name of the benefit allocation.</p>"""
    description: NotRequired["str"]
    """<p>A detailed description of the benefit allocation.</p>"""
    status: NotRequired[
        "capo_partnercentral_benefits.types.benefit_allocation_status.BenefitAllocationStatus"
    ]
    """<p>The current status of the benefit allocation (e.g., active, expired, consumed).</p>"""
    status_reason: NotRequired["str"]
    """<p>Additional information explaining the current status of the benefit allocation.</p>"""
    benefit_application_id: NotRequired[
        "capo_partnercentral_benefits.types.benefit_application_id.BenefitApplicationId"
    ]
    """<p>The identifier of the benefit application that resulted in this allocation.</p>"""
    benefit_id: NotRequired["capo_partnercentral_benefits.types.benefit_id.BenefitId"]
    """<p>The identifier of the benefit that this allocation is based on.</p>"""
    fulfillment_type: NotRequired[
        "capo_partnercentral_benefits.types.fulfillment_type.FulfillmentType"
    ]
    """<p>The fulfillment type used for this benefit allocation.</p>"""
    applicable_benefit_ids: NotRequired[
        "capo_partnercentral_benefits.types.benefit_identifiers.BenefitIdentifiers"
    ]
    """<p>A list of benefit identifiers that this allocation can be applied to.</p>"""
    fulfillment_detail: NotRequired[
        "capo_partnercentral_benefits.types.fulfillment_details.FulfillmentDetails"
    ]
    """<p>Detailed information about how the benefit allocation is fulfilled.</p>"""
    created_at: NotRequired["capo_partnercentral_benefits.types.timestamp.Timestamp"]
    """<p>The timestamp when the benefit allocation was created.</p>"""
    updated_at: NotRequired["capo_partnercentral_benefits.types.timestamp.Timestamp"]
    """<p>The timestamp when the benefit allocation was last updated.</p>"""
    starts_at: NotRequired["capo_partnercentral_benefits.types.timestamp.Timestamp"]
    """<p>The timestamp when the benefit allocation becomes active and usable.</p>"""
    expires_at: NotRequired["capo_partnercentral_benefits.types.timestamp.Timestamp"]
    """<p>The timestamp when the benefit allocation expires and is no longer usable.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetBenefitAllocationOutput) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "catalog" in value:
        out["Catalog"] = value["catalog"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "status" in value:
        import capo_partnercentral_benefits.types.benefit_allocation_status

        out["Status"] = (
            capo_partnercentral_benefits.types.benefit_allocation_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "status_reason" in value:
        out["StatusReason"] = value["status_reason"]
    if "benefit_application_id" in value:
        out["BenefitApplicationId"] = value["benefit_application_id"]
    if "benefit_id" in value:
        out["BenefitId"] = value["benefit_id"]
    if "fulfillment_type" in value:
        import capo_partnercentral_benefits.types.fulfillment_type

        out["FulfillmentType"] = (
            capo_partnercentral_benefits.types.fulfillment_type.serialize_aws_json_1_0(
                value["fulfillment_type"]
            )
        )
    if "applicable_benefit_ids" in value:
        import capo_partnercentral_benefits.types.benefit_identifiers

        out["ApplicableBenefitIds"] = (
            capo_partnercentral_benefits.types.benefit_identifiers.serialize_aws_json_1_0(
                value["applicable_benefit_ids"]
            )
        )
    if "fulfillment_detail" in value:
        import capo_partnercentral_benefits.types.fulfillment_details

        out["FulfillmentDetail"] = (
            capo_partnercentral_benefits.types.fulfillment_details.serialize_aws_json_1_0(
                value["fulfillment_detail"]
            )
        )
    if "created_at" in value:
        import capo_partnercentral_benefits.types.timestamp

        out["CreatedAt"] = (
            capo_partnercentral_benefits.types.timestamp.serialize_aws_json_1_0(
                value["created_at"]
            )
        )
    if "updated_at" in value:
        import capo_partnercentral_benefits.types.timestamp

        out["UpdatedAt"] = (
            capo_partnercentral_benefits.types.timestamp.serialize_aws_json_1_0(
                value["updated_at"]
            )
        )
    if "starts_at" in value:
        import capo_partnercentral_benefits.types.timestamp

        out["StartsAt"] = (
            capo_partnercentral_benefits.types.timestamp.serialize_aws_json_1_0(
                value["starts_at"]
            )
        )
    if "expires_at" in value:
        import capo_partnercentral_benefits.types.timestamp

        out["ExpiresAt"] = (
            capo_partnercentral_benefits.types.timestamp.serialize_aws_json_1_0(
                value["expires_at"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetBenefitAllocationOutput:
    out: GetBenefitAllocationOutput = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Status" in data:
        import capo_partnercentral_benefits.types.benefit_allocation_status

        out["status"] = (
            capo_partnercentral_benefits.types.benefit_allocation_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    if "StatusReason" in data:
        out["status_reason"] = data["StatusReason"]
    if "BenefitApplicationId" in data:
        out["benefit_application_id"] = data["BenefitApplicationId"]
    if "BenefitId" in data:
        out["benefit_id"] = data["BenefitId"]
    if "FulfillmentType" in data:
        import capo_partnercentral_benefits.types.fulfillment_type

        out["fulfillment_type"] = (
            capo_partnercentral_benefits.types.fulfillment_type.deserialize_aws_json_1_0(
                data["FulfillmentType"]
            )
        )
    if "ApplicableBenefitIds" in data:
        import capo_partnercentral_benefits.types.benefit_identifiers

        out["applicable_benefit_ids"] = (
            capo_partnercentral_benefits.types.benefit_identifiers.deserialize_aws_json_1_0(
                data["ApplicableBenefitIds"]
            )
        )
    if "FulfillmentDetail" in data:
        import capo_partnercentral_benefits.types.fulfillment_details

        out["fulfillment_detail"] = (
            capo_partnercentral_benefits.types.fulfillment_details.deserialize_aws_json_1_0(
                data["FulfillmentDetail"]
            )
        )
    if "CreatedAt" in data:
        import capo_partnercentral_benefits.types.timestamp

        out["created_at"] = (
            capo_partnercentral_benefits.types.timestamp.deserialize_aws_json_1_0(
                data["CreatedAt"]
            )
        )
    if "UpdatedAt" in data:
        import capo_partnercentral_benefits.types.timestamp

        out["updated_at"] = (
            capo_partnercentral_benefits.types.timestamp.deserialize_aws_json_1_0(
                data["UpdatedAt"]
            )
        )
    if "StartsAt" in data:
        import capo_partnercentral_benefits.types.timestamp

        out["starts_at"] = (
            capo_partnercentral_benefits.types.timestamp.deserialize_aws_json_1_0(
                data["StartsAt"]
            )
        )
    if "ExpiresAt" in data:
        import capo_partnercentral_benefits.types.timestamp

        out["expires_at"] = (
            capo_partnercentral_benefits.types.timestamp.deserialize_aws_json_1_0(
                data["ExpiresAt"]
            )
        )
    return out
