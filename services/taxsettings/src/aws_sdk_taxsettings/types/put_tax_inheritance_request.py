"""Generated from Smithy shape ``com.amazonaws.taxsettings#PutTaxInheritanceRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.heritage_status

class PutTaxInheritanceRequest(TypedDict):
    heritage_status: NotRequired["aws_sdk_taxsettings.types.heritage_status.HeritageStatus"]
    """<p>The tax inheritance status. </p>"""

# --- restJson1 ser/de ---
def serialize_json(value: PutTaxInheritanceRequest) -> dict:
    out: dict = {}
    if "heritage_status" in value:
        import aws_sdk_taxsettings.types.heritage_status
        out["heritageStatus"] = aws_sdk_taxsettings.types.heritage_status.serialize_json(value["heritage_status"])
    return out


def deserialize_json(data: dict) -> PutTaxInheritanceRequest:
    out: PutTaxInheritanceRequest = {}  # type: ignore[typeddict-item]
    if "heritageStatus" in data:
        import aws_sdk_taxsettings.types.heritage_status
        out["heritage_status"] = aws_sdk_taxsettings.types.heritage_status.deserialize_json(data["heritageStatus"])
    return out