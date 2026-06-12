"""Generated from Smithy shape ``com.amazonaws.taxsettings#PutTaxExemptionResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.generic_string

class PutTaxExemptionResponse(TypedDict):
    case_id: NotRequired["aws_sdk_taxsettings.types.generic_string.GenericString"]
    """<p>The customer support case ID. </p>"""

# --- restJson1 ser/de ---
def serialize_json(value: PutTaxExemptionResponse) -> dict:
    out: dict = {}
    if "case_id" in value:
        out["caseId"] = value["case_id"]
    return out


def deserialize_json(data: dict) -> PutTaxExemptionResponse:
    out: PutTaxExemptionResponse = {}  # type: ignore[typeddict-item]
    if "caseId" in data:
        out["case_id"] = data["caseId"]
    return out