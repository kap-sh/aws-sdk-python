"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#EffectivePolicyValues``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.disaster_recovery_source
    import capo_resiliencehubv2.types.slo_source
    import capo_resiliencehubv2.types.target_source


class EffectivePolicyValues(TypedDict, closed=True):
    availability_slo: NotRequired["capo_resiliencehubv2.types.slo_source.SloSource"]
    """<p>The effective availability SLO value for the service.</p>"""
    multi_az_rto: NotRequired["capo_resiliencehubv2.types.target_source.TargetSource"]
    """<p>The effective multi-AZ RTO value for the service, in minutes.</p>"""
    multi_az_rpo: NotRequired["capo_resiliencehubv2.types.target_source.TargetSource"]
    """<p>The effective multi-AZ RPO value for the service, in minutes.</p>"""
    multi_az_dr_approach: NotRequired[
        "capo_resiliencehubv2.types.disaster_recovery_source.DisasterRecoverySource"
    ]
    """<p>The effective multi-AZ disaster recovery approach for the service.</p>"""
    multi_region_rto: NotRequired[
        "capo_resiliencehubv2.types.target_source.TargetSource"
    ]
    """<p>The effective multi-Region RTO value for the service, in minutes.</p>"""
    multi_region_rpo: NotRequired[
        "capo_resiliencehubv2.types.target_source.TargetSource"
    ]
    """<p>The effective multi-Region RPO value for the service, in minutes.</p>"""
    multi_region_dr_approach: NotRequired[
        "capo_resiliencehubv2.types.disaster_recovery_source.DisasterRecoverySource"
    ]
    """<p>The effective multi-Region disaster recovery approach for the service.</p>"""
    data_recovery_time_between_backups: NotRequired[
        "capo_resiliencehubv2.types.target_source.TargetSource"
    ]
    """<p>The effective data recovery time between backups value for the service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EffectivePolicyValues) -> dict:
    out: dict = {}
    if "availability_slo" in value:
        import capo_resiliencehubv2.types.slo_source

        out["availabilitySlo"] = capo_resiliencehubv2.types.slo_source.serialize_json(
            value["availability_slo"]
        )
    if "multi_az_rto" in value:
        import capo_resiliencehubv2.types.target_source

        out["multiAzRto"] = capo_resiliencehubv2.types.target_source.serialize_json(
            value["multi_az_rto"]
        )
    if "multi_az_rpo" in value:
        import capo_resiliencehubv2.types.target_source

        out["multiAzRpo"] = capo_resiliencehubv2.types.target_source.serialize_json(
            value["multi_az_rpo"]
        )
    if "multi_az_dr_approach" in value:
        import capo_resiliencehubv2.types.disaster_recovery_source

        out["multiAzDrApproach"] = (
            capo_resiliencehubv2.types.disaster_recovery_source.serialize_json(
                value["multi_az_dr_approach"]
            )
        )
    if "multi_region_rto" in value:
        import capo_resiliencehubv2.types.target_source

        out["multiRegionRto"] = capo_resiliencehubv2.types.target_source.serialize_json(
            value["multi_region_rto"]
        )
    if "multi_region_rpo" in value:
        import capo_resiliencehubv2.types.target_source

        out["multiRegionRpo"] = capo_resiliencehubv2.types.target_source.serialize_json(
            value["multi_region_rpo"]
        )
    if "multi_region_dr_approach" in value:
        import capo_resiliencehubv2.types.disaster_recovery_source

        out["multiRegionDrApproach"] = (
            capo_resiliencehubv2.types.disaster_recovery_source.serialize_json(
                value["multi_region_dr_approach"]
            )
        )
    if "data_recovery_time_between_backups" in value:
        import capo_resiliencehubv2.types.target_source

        out["dataRecoveryTimeBetweenBackups"] = (
            capo_resiliencehubv2.types.target_source.serialize_json(
                value["data_recovery_time_between_backups"]
            )
        )
    return out


def deserialize_json(data: dict) -> EffectivePolicyValues:
    out: EffectivePolicyValues = {}  # type: ignore[typeddict-item]
    if "availabilitySlo" in data:
        import capo_resiliencehubv2.types.slo_source

        out["availability_slo"] = (
            capo_resiliencehubv2.types.slo_source.deserialize_json(
                data["availabilitySlo"]
            )
        )
    if "multiAzRto" in data:
        import capo_resiliencehubv2.types.target_source

        out["multi_az_rto"] = capo_resiliencehubv2.types.target_source.deserialize_json(
            data["multiAzRto"]
        )
    if "multiAzRpo" in data:
        import capo_resiliencehubv2.types.target_source

        out["multi_az_rpo"] = capo_resiliencehubv2.types.target_source.deserialize_json(
            data["multiAzRpo"]
        )
    if "multiAzDrApproach" in data:
        import capo_resiliencehubv2.types.disaster_recovery_source

        out["multi_az_dr_approach"] = (
            capo_resiliencehubv2.types.disaster_recovery_source.deserialize_json(
                data["multiAzDrApproach"]
            )
        )
    if "multiRegionRto" in data:
        import capo_resiliencehubv2.types.target_source

        out["multi_region_rto"] = (
            capo_resiliencehubv2.types.target_source.deserialize_json(
                data["multiRegionRto"]
            )
        )
    if "multiRegionRpo" in data:
        import capo_resiliencehubv2.types.target_source

        out["multi_region_rpo"] = (
            capo_resiliencehubv2.types.target_source.deserialize_json(
                data["multiRegionRpo"]
            )
        )
    if "multiRegionDrApproach" in data:
        import capo_resiliencehubv2.types.disaster_recovery_source

        out["multi_region_dr_approach"] = (
            capo_resiliencehubv2.types.disaster_recovery_source.deserialize_json(
                data["multiRegionDrApproach"]
            )
        )
    if "dataRecoveryTimeBetweenBackups" in data:
        import capo_resiliencehubv2.types.target_source

        out["data_recovery_time_between_backups"] = (
            capo_resiliencehubv2.types.target_source.deserialize_json(
                data["dataRecoveryTimeBetweenBackups"]
            )
        )
    return out
