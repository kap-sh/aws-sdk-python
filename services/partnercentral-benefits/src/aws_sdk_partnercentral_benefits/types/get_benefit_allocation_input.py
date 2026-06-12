"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#GetBenefitAllocationInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_partnercentral_benefits.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_benefits.types.benefit_allocation_identifier
    import aws_sdk_partnercentral_benefits.types.catalog_name


class GetBenefitAllocationInput(TypedDict):
    catalog: "aws_sdk_partnercentral_benefits.types.catalog_name.CatalogName"
    """<p>The catalog identifier that specifies which benefit catalog to query.</p>"""
    identifier: "aws_sdk_partnercentral_benefits.types.benefit_allocation_identifier.BenefitAllocationIdentifier"
    """<p>The unique identifier of the benefit allocation to retrieve.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetBenefitAllocationInput) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["Identifier"] = value["identifier"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetBenefitAllocationInput:
    out: GetBenefitAllocationInput = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("GetBenefitAllocationInput.catalog required")
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    else:
        raise DeserializationError("GetBenefitAllocationInput.identifier required")
    return out
