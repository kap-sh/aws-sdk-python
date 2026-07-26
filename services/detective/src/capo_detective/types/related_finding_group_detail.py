"""Generated from Smithy shape ``com.amazonaws.detective#RelatedFindingGroupDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_detective.types.id


class RelatedFindingGroupDetail(TypedDict, closed=True):
    id: NotRequired["capo_detective.types.id.Id"]
    """<p>The unique identifier for the finding group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RelatedFindingGroupDetail) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    return out


def deserialize_json(data: dict) -> RelatedFindingGroupDetail:
    out: RelatedFindingGroupDetail = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    return out
