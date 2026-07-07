"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#CancelBenefitApplicationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_partnercentral_benefits.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_benefits.types.benefit_application_identifier
    import aws_sdk_partnercentral_benefits.types.catalog_name


class CancelBenefitApplicationInput(TypedDict, closed=True):
    catalog: "aws_sdk_partnercentral_benefits.types.catalog_name.CatalogName"
    """<p>The catalog identifier that specifies which benefit catalog the application belongs to.</p>"""
    client_token: "str"
    """<p>A unique, case-sensitive identifier to ensure idempotent processing of the cancellation request.</p>"""
    identifier: "aws_sdk_partnercentral_benefits.types.benefit_application_identifier.BenefitApplicationIdentifier"
    """<p>The unique identifier of the benefit application to cancel.</p>"""
    reason: NotRequired["str"]
    """<p>A descriptive reason explaining why the benefit application is being cancelled.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CancelBenefitApplicationInput) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["ClientToken"] = value["client_token"]
    out["Identifier"] = value["identifier"]
    if "reason" in value:
        out["Reason"] = value["reason"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CancelBenefitApplicationInput:
    out: CancelBenefitApplicationInput = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("CancelBenefitApplicationInput.catalog required")
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    else:
        raise DeserializationError(
            "CancelBenefitApplicationInput.client_token required"
        )
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    else:
        raise DeserializationError("CancelBenefitApplicationInput.identifier required")
    if "Reason" in data:
        out["reason"] = data["Reason"]
    return out
