"""Generated from Smithy shape ``com.amazonaws.guardduty#CreateThreatEntitySetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.string


class CreateThreatEntitySetResponse(TypedDict, closed=True):
    threat_entity_set_id: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The ID returned by GuardDuty after creation of the threat entity set resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateThreatEntitySetResponse) -> dict:
    out: dict = {}
    if "threat_entity_set_id" in value:
        out["threatEntitySetId"] = value["threat_entity_set_id"]
    return out


def deserialize_json(data: dict) -> CreateThreatEntitySetResponse:
    out: CreateThreatEntitySetResponse = {}  # type: ignore[typeddict-item]
    if "threatEntitySetId" in data:
        out["threat_entity_set_id"] = data["threatEntitySetId"]
    return out
