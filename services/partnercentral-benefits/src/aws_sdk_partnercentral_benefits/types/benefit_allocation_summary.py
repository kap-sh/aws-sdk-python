"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#BenefitAllocationSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_partnercentral_benefits.types.benefit_allocation_id
    import aws_sdk_partnercentral_benefits.types.benefit_allocation_name
    import aws_sdk_partnercentral_benefits.types.benefit_allocation_status
    import aws_sdk_partnercentral_benefits.types.benefit_application_id
    import aws_sdk_partnercentral_benefits.types.benefit_id
    import aws_sdk_partnercentral_benefits.types.benefit_ids
    import aws_sdk_partnercentral_benefits.types.catalog_name
    import aws_sdk_partnercentral_benefits.types.fulfillment_types
    import aws_sdk_partnercentral_benefits.types.timestamp


class BenefitAllocationSummary(TypedDict):
    id: NotRequired[
        "aws_sdk_partnercentral_benefits.types.benefit_allocation_id.BenefitAllocationId"
    ]
    """<p>The unique identifier of the benefit allocation.</p>"""
    catalog: NotRequired[
        "aws_sdk_partnercentral_benefits.types.catalog_name.CatalogName"
    ]
    """<p>The catalog identifier that the benefit allocation belongs to.</p>"""
    arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the benefit allocation.</p>"""
    status: NotRequired[
        "aws_sdk_partnercentral_benefits.types.benefit_allocation_status.BenefitAllocationStatus"
    ]
    """<p>The current status of the benefit allocation.</p>"""
    status_reason: NotRequired["str"]
    """<p>Additional information explaining the current status of the benefit allocation.</p>"""
    name: NotRequired[
        "aws_sdk_partnercentral_benefits.types.benefit_allocation_name.BenefitAllocationName"
    ]
    """<p>The human-readable name of the benefit allocation.</p>"""
    benefit_id: NotRequired[
        "aws_sdk_partnercentral_benefits.types.benefit_id.BenefitId"
    ]
    """<p>The identifier of the benefit that this allocation is based on.</p>"""
    benefit_application_id: NotRequired[
        "aws_sdk_partnercentral_benefits.types.benefit_application_id.BenefitApplicationId"
    ]
    """<p>The identifier of the benefit application that resulted in this allocation.</p>"""
    fulfillment_types: NotRequired[
        "aws_sdk_partnercentral_benefits.types.fulfillment_types.FulfillmentTypes"
    ]
    """<p>The fulfillment types used for this benefit allocation.</p>"""
    created_at: NotRequired["aws_sdk_partnercentral_benefits.types.timestamp.Timestamp"]
    """<p>The timestamp when the benefit allocation was created.</p>"""
    expires_at: NotRequired["aws_sdk_partnercentral_benefits.types.timestamp.Timestamp"]
    """<p>The timestamp when the benefit allocation expires.</p>"""
    applicable_benefit_ids: NotRequired[
        "aws_sdk_partnercentral_benefits.types.benefit_ids.BenefitIds"
    ]
    """<p>The identifiers of the benefits applicable for this allocation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BenefitAllocationSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "catalog" in value:
        out["Catalog"] = value["catalog"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "status" in value:
        import aws_sdk_partnercentral_benefits.types.benefit_allocation_status

        out["Status"] = (
            aws_sdk_partnercentral_benefits.types.benefit_allocation_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "status_reason" in value:
        out["StatusReason"] = value["status_reason"]
    if "name" in value:
        out["Name"] = value["name"]
    if "benefit_id" in value:
        out["BenefitId"] = value["benefit_id"]
    if "benefit_application_id" in value:
        out["BenefitApplicationId"] = value["benefit_application_id"]
    if "fulfillment_types" in value:
        import aws_sdk_partnercentral_benefits.types.fulfillment_types

        out["FulfillmentTypes"] = (
            aws_sdk_partnercentral_benefits.types.fulfillment_types.serialize_aws_json_1_0(
                value["fulfillment_types"]
            )
        )
    if "created_at" in value:
        import aws_sdk_partnercentral_benefits.types.timestamp

        out["CreatedAt"] = (
            aws_sdk_partnercentral_benefits.types.timestamp.serialize_aws_json_1_0(
                value["created_at"]
            )
        )
    if "expires_at" in value:
        import aws_sdk_partnercentral_benefits.types.timestamp

        out["ExpiresAt"] = (
            aws_sdk_partnercentral_benefits.types.timestamp.serialize_aws_json_1_0(
                value["expires_at"]
            )
        )
    if "applicable_benefit_ids" in value:
        import aws_sdk_partnercentral_benefits.types.benefit_ids

        out["ApplicableBenefitIds"] = (
            aws_sdk_partnercentral_benefits.types.benefit_ids.serialize_aws_json_1_0(
                value["applicable_benefit_ids"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BenefitAllocationSummary:
    out: BenefitAllocationSummary = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Status" in data:
        import aws_sdk_partnercentral_benefits.types.benefit_allocation_status

        out["status"] = (
            aws_sdk_partnercentral_benefits.types.benefit_allocation_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    if "StatusReason" in data:
        out["status_reason"] = data["StatusReason"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "BenefitId" in data:
        out["benefit_id"] = data["BenefitId"]
    if "BenefitApplicationId" in data:
        out["benefit_application_id"] = data["BenefitApplicationId"]
    if "FulfillmentTypes" in data:
        import aws_sdk_partnercentral_benefits.types.fulfillment_types

        out["fulfillment_types"] = (
            aws_sdk_partnercentral_benefits.types.fulfillment_types.deserialize_aws_json_1_0(
                data["FulfillmentTypes"]
            )
        )
    if "CreatedAt" in data:
        import aws_sdk_partnercentral_benefits.types.timestamp

        out["created_at"] = (
            aws_sdk_partnercentral_benefits.types.timestamp.deserialize_aws_json_1_0(
                data["CreatedAt"]
            )
        )
    if "ExpiresAt" in data:
        import aws_sdk_partnercentral_benefits.types.timestamp

        out["expires_at"] = (
            aws_sdk_partnercentral_benefits.types.timestamp.deserialize_aws_json_1_0(
                data["ExpiresAt"]
            )
        )
    if "ApplicableBenefitIds" in data:
        import aws_sdk_partnercentral_benefits.types.benefit_ids

        out["applicable_benefit_ids"] = (
            aws_sdk_partnercentral_benefits.types.benefit_ids.deserialize_aws_json_1_0(
                data["ApplicableBenefitIds"]
            )
        )
    return out
