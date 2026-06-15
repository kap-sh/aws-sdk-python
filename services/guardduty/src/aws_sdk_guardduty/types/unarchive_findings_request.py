"""Generated from Smithy shape ``com.amazonaws.guardduty#UnarchiveFindingsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.detector_id
    import aws_sdk_guardduty.types.finding_ids


class UnarchiveFindingsRequest(TypedDict):
    detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId"
    r"""<p>The ID of the detector associated with the findings to unarchive.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>"""
    finding_ids: NotRequired["aws_sdk_guardduty.types.finding_ids.FindingIds"]
    """<p>The IDs of the findings to unarchive.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnarchiveFindingsRequest) -> dict:
    out: dict = {}
    if "finding_ids" in value:
        import aws_sdk_guardduty.types.finding_ids

        out["findingIds"] = aws_sdk_guardduty.types.finding_ids.serialize_json(
            value["finding_ids"]
        )
    return out


def deserialize_json(data: dict) -> UnarchiveFindingsRequest:
    out: UnarchiveFindingsRequest = {}  # type: ignore[typeddict-item]
    if "findingIds" in data:
        import aws_sdk_guardduty.types.finding_ids

        out["finding_ids"] = aws_sdk_guardduty.types.finding_ids.deserialize_json(
            data["findingIds"]
        )
    return out
