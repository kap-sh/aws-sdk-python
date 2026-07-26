"""Generated from Smithy shape ``com.amazonaws.guardduty#ListDetectorsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.detector_ids
    import capo_guardduty.types.string


class ListDetectorsResponse(TypedDict, closed=True):
    detector_ids: NotRequired["capo_guardduty.types.detector_ids.DetectorIds"]
    """<p>A list of detector IDs.</p>"""
    next_token: NotRequired["capo_guardduty.types.string.String"]
    """<p>The pagination parameter to be used on the next list operation to retrieve more items.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDetectorsResponse) -> dict:
    out: dict = {}
    if "detector_ids" in value:
        import capo_guardduty.types.detector_ids

        out["detectorIds"] = capo_guardduty.types.detector_ids.serialize_json(
            value["detector_ids"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDetectorsResponse:
    out: ListDetectorsResponse = {}  # type: ignore[typeddict-item]
    if "detectorIds" in data:
        import capo_guardduty.types.detector_ids

        out["detector_ids"] = capo_guardduty.types.detector_ids.deserialize_json(
            data["detectorIds"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
