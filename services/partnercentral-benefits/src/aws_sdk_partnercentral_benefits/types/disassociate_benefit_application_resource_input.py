"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#DisassociateBenefitApplicationResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_partnercentral_benefits.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_benefits.types.arn
    import aws_sdk_partnercentral_benefits.types.benefit_application_identifier
    import aws_sdk_partnercentral_benefits.types.catalog_name


class DisassociateBenefitApplicationResourceInput(TypedDict, closed=True):
    catalog: "aws_sdk_partnercentral_benefits.types.catalog_name.CatalogName"
    """<p>The catalog identifier that specifies which benefit catalog the application belongs to.</p>"""
    benefit_application_identifier: "aws_sdk_partnercentral_benefits.types.benefit_application_identifier.BenefitApplicationIdentifier"
    """<p>The unique identifier of the benefit application to disassociate the resource from.</p>"""
    resource_arn: "aws_sdk_partnercentral_benefits.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the AWS resource to disassociate from the benefit application.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DisassociateBenefitApplicationResourceInput) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["BenefitApplicationIdentifier"] = value["benefit_application_identifier"]
    out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DisassociateBenefitApplicationResourceInput:
    out: DisassociateBenefitApplicationResourceInput = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError(
            "DisassociateBenefitApplicationResourceInput.catalog required"
        )
    if "BenefitApplicationIdentifier" in data:
        out["benefit_application_identifier"] = data["BenefitApplicationIdentifier"]
    else:
        raise DeserializationError(
            "DisassociateBenefitApplicationResourceInput.benefit_application_identifier required"
        )
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError(
            "DisassociateBenefitApplicationResourceInput.resource_arn required"
        )
    return out
