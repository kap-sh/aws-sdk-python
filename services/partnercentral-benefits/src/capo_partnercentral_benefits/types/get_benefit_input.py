"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#GetBenefitInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_partnercentral_benefits.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_benefits.types.catalog_name


class GetBenefitInput(TypedDict, closed=True):
    catalog: "capo_partnercentral_benefits.types.catalog_name.CatalogName"
    """<p>The catalog identifier that specifies which benefit catalog to query.</p>"""
    identifier: "str"
    """<p>The unique identifier of the benefit to retrieve.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetBenefitInput) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["Identifier"] = value["identifier"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetBenefitInput:
    out: GetBenefitInput = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("GetBenefitInput.catalog required")
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    else:
        raise DeserializationError("GetBenefitInput.identifier required")
    return out
