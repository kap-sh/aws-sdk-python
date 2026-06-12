"""Generated from Smithy shape ``com.amazonaws.taxsettings#GreeceAdditionalInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.contracting_authority_code

class GreeceAdditionalInfo(TypedDict):
    contracting_authority_code: NotRequired["aws_sdk_taxsettings.types.contracting_authority_code.ContractingAuthorityCode"]
    """<p>The code of contracting authority for e-invoicing.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: GreeceAdditionalInfo) -> dict:
    out: dict = {}
    if "contracting_authority_code" in value:
        out["contractingAuthorityCode"] = value["contracting_authority_code"]
    return out


def deserialize_json(data: dict) -> GreeceAdditionalInfo:
    out: GreeceAdditionalInfo = {}  # type: ignore[typeddict-item]
    if "contractingAuthorityCode" in data:
        out["contracting_authority_code"] = data["contractingAuthorityCode"]
    return out