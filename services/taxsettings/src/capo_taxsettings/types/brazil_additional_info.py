"""Generated from Smithy shape ``com.amazonaws.taxsettings#BrazilAdditionalInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_taxsettings.types.ccm_code
    import capo_taxsettings.types.legal_nature_code


class BrazilAdditionalInfo(TypedDict, closed=True):
    ccm_code: NotRequired["capo_taxsettings.types.ccm_code.CcmCode"]
    """<p>The Cadastro de Contribuintes Mobiliários (CCM) code for your TRN in Brazil. This only applies for a CNPJ tax type for the São Paulo municipality.</p>"""
    legal_nature_code: NotRequired[
        "capo_taxsettings.types.legal_nature_code.LegalNatureCode"
    ]
    """<p>Legal nature of business, based on your TRN in Brazil. This only applies for a CNPJ tax type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BrazilAdditionalInfo) -> dict:
    out: dict = {}
    if "ccm_code" in value:
        out["ccmCode"] = value["ccm_code"]
    if "legal_nature_code" in value:
        out["legalNatureCode"] = value["legal_nature_code"]
    return out


def deserialize_json(data: dict) -> BrazilAdditionalInfo:
    out: BrazilAdditionalInfo = {}  # type: ignore[typeddict-item]
    if "ccmCode" in data:
        out["ccm_code"] = data["ccmCode"]
    if "legalNatureCode" in data:
        out["legal_nature_code"] = data["legalNatureCode"]
    return out
