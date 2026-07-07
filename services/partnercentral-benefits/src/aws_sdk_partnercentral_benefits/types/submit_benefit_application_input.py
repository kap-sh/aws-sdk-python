"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#SubmitBenefitApplicationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_partnercentral_benefits.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_benefits.types.benefit_application_identifier
    import aws_sdk_partnercentral_benefits.types.catalog_name


class SubmitBenefitApplicationInput(TypedDict, closed=True):
    catalog: "aws_sdk_partnercentral_benefits.types.catalog_name.CatalogName"
    """<p>The catalog identifier that specifies which benefit catalog the application belongs to.</p>"""
    identifier: "aws_sdk_partnercentral_benefits.types.benefit_application_identifier.BenefitApplicationIdentifier"
    """<p>The unique identifier of the benefit application to submit.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SubmitBenefitApplicationInput) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["Identifier"] = value["identifier"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SubmitBenefitApplicationInput:
    out: SubmitBenefitApplicationInput = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("SubmitBenefitApplicationInput.catalog required")
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    else:
        raise DeserializationError("SubmitBenefitApplicationInput.identifier required")
    return out
