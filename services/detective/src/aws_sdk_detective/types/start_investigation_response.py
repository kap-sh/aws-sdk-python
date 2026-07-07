"""Generated from Smithy shape ``com.amazonaws.detective#StartInvestigationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_detective.types.investigation_id


class StartInvestigationResponse(TypedDict, closed=True):
    investigation_id: NotRequired[
        "aws_sdk_detective.types.investigation_id.InvestigationId"
    ]
    """<p>The investigation ID of the investigation report.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartInvestigationResponse) -> dict:
    out: dict = {}
    if "investigation_id" in value:
        out["InvestigationId"] = value["investigation_id"]
    return out


def deserialize_json(data: dict) -> StartInvestigationResponse:
    out: StartInvestigationResponse = {}  # type: ignore[typeddict-item]
    if "InvestigationId" in data:
        out["investigation_id"] = data["InvestigationId"]
    return out
