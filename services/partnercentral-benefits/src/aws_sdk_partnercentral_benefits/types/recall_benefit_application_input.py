"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#RecallBenefitApplicationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_partnercentral_benefits.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_benefits.types.benefit_application_identifier
    import aws_sdk_partnercentral_benefits.types.catalog_name


class RecallBenefitApplicationInput(TypedDict, closed=True):
    catalog: "aws_sdk_partnercentral_benefits.types.catalog_name.CatalogName"
    """<p>The catalog identifier that specifies which benefit catalog the application belongs to.</p>"""
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier to ensure idempotent processing of the recall request.</p>"""
    identifier: "aws_sdk_partnercentral_benefits.types.benefit_application_identifier.BenefitApplicationIdentifier"
    """<p>The unique identifier of the benefit application to recall.</p>"""
    reason: "str"
    """<p>A descriptive reason explaining why the benefit application is being recalled.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RecallBenefitApplicationInput) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["Identifier"] = value["identifier"]
    out["Reason"] = value["reason"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RecallBenefitApplicationInput:
    out: RecallBenefitApplicationInput = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("RecallBenefitApplicationInput.catalog required")
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    else:
        raise DeserializationError("RecallBenefitApplicationInput.identifier required")
    if "Reason" in data:
        out["reason"] = data["Reason"]
    else:
        raise DeserializationError("RecallBenefitApplicationInput.reason required")
    return out
