"""Generated from Smithy shape ``com.amazonaws.guardduty#GetFilterRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.detector_id
    import aws_sdk_guardduty.types.string


class GetFilterRequest(TypedDict):
    detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId"
    r"""<p>The unique ID of the detector that is associated with this filter.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>"""
    filter_name: "aws_sdk_guardduty.types.string.String"
    """<p>The name of the filter you want to get.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFilterRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetFilterRequest:
    out: GetFilterRequest = {}  # type: ignore[typeddict-item]
    return out
