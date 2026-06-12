"""Generated from Smithy shape ``com.amazonaws.guardduty#DeleteTrustedEntitySetRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.detector_id
    import aws_sdk_guardduty.types.string


class DeleteTrustedEntitySetRequest(TypedDict):
    detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId"
    """<p>The unique ID of the detector associated with the trusted entity set resource.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>"""
    trusted_entity_set_id: "aws_sdk_guardduty.types.string.String"
    """<p>The unique ID that helps GuardDuty identify which trusted entity set needs to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTrustedEntitySetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteTrustedEntitySetRequest:
    out: DeleteTrustedEntitySetRequest = {}  # type: ignore[typeddict-item]
    return out
