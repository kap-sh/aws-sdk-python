"""Generated from Smithy shape ``com.amazonaws.guardduty#GetTrustedEntitySetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.detector_id
    import aws_sdk_guardduty.types.string


class GetTrustedEntitySetRequest(TypedDict, closed=True):
    detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId"
    """<p>The unique ID of the GuardDuty detector associated with this trusted entity set.</p>"""
    trusted_entity_set_id: "aws_sdk_guardduty.types.string.String"
    """<p>The unique ID that helps GuardDuty identify the trusted entity set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTrustedEntitySetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTrustedEntitySetRequest:
    out: GetTrustedEntitySetRequest = {}  # type: ignore[typeddict-item]
    return out
