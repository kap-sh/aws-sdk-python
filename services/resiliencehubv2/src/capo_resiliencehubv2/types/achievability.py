"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#Achievability``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.achievability_status


class Achievability(TypedDict, closed=True):
    availability_slo: NotRequired[
        "capo_resiliencehubv2.types.achievability_status.AchievabilityStatus"
    ]
    """<p>The achievability status of the availability SLO target for the service.</p>"""
    multi_az_rto_rpo: NotRequired[
        "capo_resiliencehubv2.types.achievability_status.AchievabilityStatus"
    ]
    """<p>The achievability status of the multi-AZ RTO and RPO targets for the service.</p>"""
    multi_region_rto_rpo: NotRequired[
        "capo_resiliencehubv2.types.achievability_status.AchievabilityStatus"
    ]
    """<p>The achievability status of the multi-Region RTO and RPO targets for the service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Achievability) -> dict:
    out: dict = {}
    if "availability_slo" in value:
        import capo_resiliencehubv2.types.achievability_status

        out["availabilitySlo"] = (
            capo_resiliencehubv2.types.achievability_status.serialize_json(
                value["availability_slo"]
            )
        )
    if "multi_az_rto_rpo" in value:
        import capo_resiliencehubv2.types.achievability_status

        out["multiAzRtoRpo"] = (
            capo_resiliencehubv2.types.achievability_status.serialize_json(
                value["multi_az_rto_rpo"]
            )
        )
    if "multi_region_rto_rpo" in value:
        import capo_resiliencehubv2.types.achievability_status

        out["multiRegionRtoRpo"] = (
            capo_resiliencehubv2.types.achievability_status.serialize_json(
                value["multi_region_rto_rpo"]
            )
        )
    return out


def deserialize_json(data: dict) -> Achievability:
    out: Achievability = {}  # type: ignore[typeddict-item]
    if "availabilitySlo" in data:
        import capo_resiliencehubv2.types.achievability_status

        out["availability_slo"] = (
            capo_resiliencehubv2.types.achievability_status.deserialize_json(
                data["availabilitySlo"]
            )
        )
    if "multiAzRtoRpo" in data:
        import capo_resiliencehubv2.types.achievability_status

        out["multi_az_rto_rpo"] = (
            capo_resiliencehubv2.types.achievability_status.deserialize_json(
                data["multiAzRtoRpo"]
            )
        )
    if "multiRegionRtoRpo" in data:
        import capo_resiliencehubv2.types.achievability_status

        out["multi_region_rto_rpo"] = (
            capo_resiliencehubv2.types.achievability_status.deserialize_json(
                data["multiRegionRtoRpo"]
            )
        )
    return out
