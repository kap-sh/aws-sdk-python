"""Generated from Smithy shape ``com.amazonaws.guardduty#GetDetectorRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.detector_id


class GetDetectorRequest(TypedDict):
    detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId"
    r"""<p>The unique ID of the detector that you want to get.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDetectorRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDetectorRequest:
    out: GetDetectorRequest = {}  # type: ignore[typeddict-item]
    return out
