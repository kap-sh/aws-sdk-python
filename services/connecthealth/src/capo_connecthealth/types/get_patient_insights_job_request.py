"""Generated from Smithy shape ``com.amazonaws.connecthealth#GetPatientInsightsJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connecthealth.types.domain_id
    import capo_connecthealth.types.job_id


class GetPatientInsightsJobRequest(TypedDict, closed=True):
    domain_id: "capo_connecthealth.types.domain_id.DomainId"
    """<p/>"""
    job_id: "capo_connecthealth.types.job_id.JobId"
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPatientInsightsJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetPatientInsightsJobRequest:
    out: GetPatientInsightsJobRequest = {}  # type: ignore[typeddict-item]
    return out
