"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#AssociateBenefitApplicationResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_partnercentral_benefits.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_benefits.types.arn
    import capo_partnercentral_benefits.types.benefit_application_identifier
    import capo_partnercentral_benefits.types.catalog_name


class AssociateBenefitApplicationResourceInput(TypedDict, closed=True):
    catalog: "capo_partnercentral_benefits.types.catalog_name.CatalogName"
    """<p>The catalog identifier that specifies which benefit catalog the application belongs to.</p>"""
    benefit_application_identifier: "capo_partnercentral_benefits.types.benefit_application_identifier.BenefitApplicationIdentifier"
    """<p>The unique identifier of the benefit application to associate the resource with.</p>"""
    resource_arn: "capo_partnercentral_benefits.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the AWS resource to associate with the benefit application.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AssociateBenefitApplicationResourceInput) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["BenefitApplicationIdentifier"] = value["benefit_application_identifier"]
    out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AssociateBenefitApplicationResourceInput:
    out: AssociateBenefitApplicationResourceInput = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError(
            "AssociateBenefitApplicationResourceInput.catalog required"
        )
    if "BenefitApplicationIdentifier" in data:
        out["benefit_application_identifier"] = data["BenefitApplicationIdentifier"]
    else:
        raise DeserializationError(
            "AssociateBenefitApplicationResourceInput.benefit_application_identifier required"
        )
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError(
            "AssociateBenefitApplicationResourceInput.resource_arn required"
        )
    return out
