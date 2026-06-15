"""Generated from Smithy shape ``com.amazonaws.guardduty#DescribePublishingDestinationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.detector_id
    import aws_sdk_guardduty.types.string


class DescribePublishingDestinationRequest(TypedDict):
    detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId"
    r"""<p>The unique ID of the detector associated with the publishing destination to retrieve.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>"""
    destination_id: "aws_sdk_guardduty.types.string.String"
    """<p>The ID of the publishing destination to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribePublishingDestinationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribePublishingDestinationRequest:
    out: DescribePublishingDestinationRequest = {}  # type: ignore[typeddict-item]
    return out
