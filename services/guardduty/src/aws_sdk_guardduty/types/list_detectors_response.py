"""Generated from Smithy shape ``com.amazonaws.guardduty#ListDetectorsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.detector_ids
    import aws_sdk_guardduty.types.string


class ListDetectorsResponse(TypedDict):
    detector_ids: NotRequired["aws_sdk_guardduty.types.detector_ids.DetectorIds"]
    """<p>A list of detector IDs.</p>"""
    next_token: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The pagination parameter to be used on the next list operation to retrieve more items.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDetectorsResponse) -> dict:
    out: dict = {}
    if "detector_ids" in value:
        import aws_sdk_guardduty.types.detector_ids

        out["detectorIds"] = aws_sdk_guardduty.types.detector_ids.serialize_json(
            value["detector_ids"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDetectorsResponse:
    out: ListDetectorsResponse = {}  # type: ignore[typeddict-item]
    if "detectorIds" in data:
        import aws_sdk_guardduty.types.detector_ids

        out["detector_ids"] = aws_sdk_guardduty.types.detector_ids.deserialize_json(
            data["detectorIds"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
