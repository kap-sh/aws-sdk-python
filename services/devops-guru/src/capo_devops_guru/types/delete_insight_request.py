"""Generated from Smithy shape ``com.amazonaws.devopsguru#DeleteInsightRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.insight_id


class DeleteInsightRequest(TypedDict, closed=True):
    id: "capo_devops_guru.types.insight_id.InsightId"
    """<p>The ID of the insight.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteInsightRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteInsightRequest:
    out: DeleteInsightRequest = {}  # type: ignore[typeddict-item]
    return out
