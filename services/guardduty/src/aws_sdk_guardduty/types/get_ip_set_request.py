"""Generated from Smithy shape ``com.amazonaws.guardduty#GetIPSetRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.detector_id
    import aws_sdk_guardduty.types.string


class GetIPSetRequest(TypedDict):
    detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId"
    """<p>The unique ID of the detector that is associated with the IPSet.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>"""
    ip_set_id: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The unique ID of the IPSet to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIPSetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetIPSetRequest:
    out: GetIPSetRequest = {}  # type: ignore[typeddict-item]
    return out
