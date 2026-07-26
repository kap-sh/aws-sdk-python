"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#MultiRegionTargets``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.multi_region_disaster_recovery_approach


class MultiRegionTargets(TypedDict, closed=True):
    rto_in_minutes: NotRequired["int"]
    """<p>The recovery time objective (RTO) target for multi-Region, in minutes.</p>"""
    rpo_in_minutes: NotRequired["int"]
    """<p>The recovery point objective (RPO) target for multi-Region, in minutes.</p>"""
    disaster_recovery_approach: NotRequired[
        "capo_resiliencehubv2.types.multi_region_disaster_recovery_approach.MultiRegionDisasterRecoveryApproach"
    ]
    """<p>The disaster recovery approach for multi-Region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MultiRegionTargets) -> dict:
    out: dict = {}
    if "rto_in_minutes" in value:
        out["rtoInMinutes"] = value["rto_in_minutes"]
    if "rpo_in_minutes" in value:
        out["rpoInMinutes"] = value["rpo_in_minutes"]
    if "disaster_recovery_approach" in value:
        import capo_resiliencehubv2.types.multi_region_disaster_recovery_approach

        out["disasterRecoveryApproach"] = (
            capo_resiliencehubv2.types.multi_region_disaster_recovery_approach.serialize_json(
                value["disaster_recovery_approach"]
            )
        )
    return out


def deserialize_json(data: dict) -> MultiRegionTargets:
    out: MultiRegionTargets = {}  # type: ignore[typeddict-item]
    if "rtoInMinutes" in data:
        out["rto_in_minutes"] = data["rtoInMinutes"]
    if "rpoInMinutes" in data:
        out["rpo_in_minutes"] = data["rpoInMinutes"]
    if "disasterRecoveryApproach" in data:
        import capo_resiliencehubv2.types.multi_region_disaster_recovery_approach

        out["disaster_recovery_approach"] = (
            capo_resiliencehubv2.types.multi_region_disaster_recovery_approach.deserialize_json(
                data["disasterRecoveryApproach"]
            )
        )
    return out
