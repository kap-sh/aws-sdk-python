"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#GetFailureModeFindingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.uuid


class GetFailureModeFindingRequest(TypedDict, closed=True):
    finding_id: "capo_resiliencehubv2.types.uuid.Uuid"
    """<p>The unique identifier of the finding to retrieve.</p>"""
    service_arn: "capo_resiliencehubv2.types.arn.Arn"


# --- restJson1 ser/de ---
def serialize_json(value: GetFailureModeFindingRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetFailureModeFindingRequest:
    out: GetFailureModeFindingRequest = {}  # type: ignore[typeddict-item]
    return out
