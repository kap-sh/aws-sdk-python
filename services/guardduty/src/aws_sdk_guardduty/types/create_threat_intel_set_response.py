"""Generated from Smithy shape ``com.amazonaws.guardduty#CreateThreatIntelSetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.string


class CreateThreatIntelSetResponse(TypedDict, closed=True):
    threat_intel_set_id: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The ID of the ThreatIntelSet resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateThreatIntelSetResponse) -> dict:
    out: dict = {}
    if "threat_intel_set_id" in value:
        out["threatIntelSetId"] = value["threat_intel_set_id"]
    return out


def deserialize_json(data: dict) -> CreateThreatIntelSetResponse:
    out: CreateThreatIntelSetResponse = {}  # type: ignore[typeddict-item]
    if "threatIntelSetId" in data:
        out["threat_intel_set_id"] = data["threatIntelSetId"]
    return out
