"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ServiceAchievabilityUpdatedMetadata``."""

from typing import TypedDict

from typing_extensions import NotRequired


class ServiceAchievabilityUpdatedMetadata(TypedDict):
    assessment_id: NotRequired["str"]
    """<p>The assessment identifier that triggered the update.</p>"""
    availability_slo: NotRequired["str"]
    """<p>The updated achievability status of the availability SLO.</p>"""
    multi_az_rto_rpo: NotRequired["str"]
    """<p>The updated achievability status of the multi-AZ RTO and RPO targets.</p>"""
    multi_region_rto_rpo: NotRequired["str"]
    """<p>The updated achievability status of the multi-Region RTO and RPO targets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceAchievabilityUpdatedMetadata) -> dict:
    out: dict = {}
    if "assessment_id" in value:
        out["assessmentId"] = value["assessment_id"]
    if "availability_slo" in value:
        out["availabilitySlo"] = value["availability_slo"]
    if "multi_az_rto_rpo" in value:
        out["multiAzRtoRpo"] = value["multi_az_rto_rpo"]
    if "multi_region_rto_rpo" in value:
        out["multiRegionRtoRpo"] = value["multi_region_rto_rpo"]
    return out


def deserialize_json(data: dict) -> ServiceAchievabilityUpdatedMetadata:
    out: ServiceAchievabilityUpdatedMetadata = {}  # type: ignore[typeddict-item]
    if "assessmentId" in data:
        out["assessment_id"] = data["assessmentId"]
    if "availabilitySlo" in data:
        out["availability_slo"] = data["availabilitySlo"]
    if "multiAzRtoRpo" in data:
        out["multi_az_rto_rpo"] = data["multiAzRtoRpo"]
    if "multiRegionRtoRpo" in data:
        out["multi_region_rto_rpo"] = data["multiRegionRtoRpo"]
    return out
