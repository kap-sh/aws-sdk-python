"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#EffectivePolicyValues``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.disaster_recovery_source
    import aws_sdk_resiliencehubv2.types.slo_source
    import aws_sdk_resiliencehubv2.types.target_source


class EffectivePolicyValues(TypedDict):
    availability_slo: NotRequired["aws_sdk_resiliencehubv2.types.slo_source.SloSource"]
    """<p>The effective availability SLO value for the service.</p>"""
    multi_az_rto: NotRequired[
        "aws_sdk_resiliencehubv2.types.target_source.TargetSource"
    ]
    """<p>The effective multi-AZ RTO value for the service, in minutes.</p>"""
    multi_az_rpo: NotRequired[
        "aws_sdk_resiliencehubv2.types.target_source.TargetSource"
    ]
    """<p>The effective multi-AZ RPO value for the service, in minutes.</p>"""
    multi_az_dr_approach: NotRequired[
        "aws_sdk_resiliencehubv2.types.disaster_recovery_source.DisasterRecoverySource"
    ]
    """<p>The effective multi-AZ disaster recovery approach for the service.</p>"""
    multi_region_rto: NotRequired[
        "aws_sdk_resiliencehubv2.types.target_source.TargetSource"
    ]
    """<p>The effective multi-Region RTO value for the service, in minutes.</p>"""
    multi_region_rpo: NotRequired[
        "aws_sdk_resiliencehubv2.types.target_source.TargetSource"
    ]
    """<p>The effective multi-Region RPO value for the service, in minutes.</p>"""
    multi_region_dr_approach: NotRequired[
        "aws_sdk_resiliencehubv2.types.disaster_recovery_source.DisasterRecoverySource"
    ]
    """<p>The effective multi-Region disaster recovery approach for the service.</p>"""
    data_recovery_time_between_backups: NotRequired[
        "aws_sdk_resiliencehubv2.types.target_source.TargetSource"
    ]
    """<p>The effective data recovery time between backups value for the service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EffectivePolicyValues) -> dict:
    out: dict = {}
    if "availability_slo" in value:
        import aws_sdk_resiliencehubv2.types.slo_source

        out["availabilitySlo"] = (
            aws_sdk_resiliencehubv2.types.slo_source.serialize_json(
                value["availability_slo"]
            )
        )
    if "multi_az_rto" in value:
        import aws_sdk_resiliencehubv2.types.target_source

        out["multiAzRto"] = aws_sdk_resiliencehubv2.types.target_source.serialize_json(
            value["multi_az_rto"]
        )
    if "multi_az_rpo" in value:
        import aws_sdk_resiliencehubv2.types.target_source

        out["multiAzRpo"] = aws_sdk_resiliencehubv2.types.target_source.serialize_json(
            value["multi_az_rpo"]
        )
    if "multi_az_dr_approach" in value:
        import aws_sdk_resiliencehubv2.types.disaster_recovery_source

        out["multiAzDrApproach"] = (
            aws_sdk_resiliencehubv2.types.disaster_recovery_source.serialize_json(
                value["multi_az_dr_approach"]
            )
        )
    if "multi_region_rto" in value:
        import aws_sdk_resiliencehubv2.types.target_source

        out["multiRegionRto"] = (
            aws_sdk_resiliencehubv2.types.target_source.serialize_json(
                value["multi_region_rto"]
            )
        )
    if "multi_region_rpo" in value:
        import aws_sdk_resiliencehubv2.types.target_source

        out["multiRegionRpo"] = (
            aws_sdk_resiliencehubv2.types.target_source.serialize_json(
                value["multi_region_rpo"]
            )
        )
    if "multi_region_dr_approach" in value:
        import aws_sdk_resiliencehubv2.types.disaster_recovery_source

        out["multiRegionDrApproach"] = (
            aws_sdk_resiliencehubv2.types.disaster_recovery_source.serialize_json(
                value["multi_region_dr_approach"]
            )
        )
    if "data_recovery_time_between_backups" in value:
        import aws_sdk_resiliencehubv2.types.target_source

        out["dataRecoveryTimeBetweenBackups"] = (
            aws_sdk_resiliencehubv2.types.target_source.serialize_json(
                value["data_recovery_time_between_backups"]
            )
        )
    return out


def deserialize_json(data: dict) -> EffectivePolicyValues:
    out: EffectivePolicyValues = {}  # type: ignore[typeddict-item]
    if "availabilitySlo" in data:
        import aws_sdk_resiliencehubv2.types.slo_source

        out["availability_slo"] = (
            aws_sdk_resiliencehubv2.types.slo_source.deserialize_json(
                data["availabilitySlo"]
            )
        )
    if "multiAzRto" in data:
        import aws_sdk_resiliencehubv2.types.target_source

        out["multi_az_rto"] = (
            aws_sdk_resiliencehubv2.types.target_source.deserialize_json(
                data["multiAzRto"]
            )
        )
    if "multiAzRpo" in data:
        import aws_sdk_resiliencehubv2.types.target_source

        out["multi_az_rpo"] = (
            aws_sdk_resiliencehubv2.types.target_source.deserialize_json(
                data["multiAzRpo"]
            )
        )
    if "multiAzDrApproach" in data:
        import aws_sdk_resiliencehubv2.types.disaster_recovery_source

        out["multi_az_dr_approach"] = (
            aws_sdk_resiliencehubv2.types.disaster_recovery_source.deserialize_json(
                data["multiAzDrApproach"]
            )
        )
    if "multiRegionRto" in data:
        import aws_sdk_resiliencehubv2.types.target_source

        out["multi_region_rto"] = (
            aws_sdk_resiliencehubv2.types.target_source.deserialize_json(
                data["multiRegionRto"]
            )
        )
    if "multiRegionRpo" in data:
        import aws_sdk_resiliencehubv2.types.target_source

        out["multi_region_rpo"] = (
            aws_sdk_resiliencehubv2.types.target_source.deserialize_json(
                data["multiRegionRpo"]
            )
        )
    if "multiRegionDrApproach" in data:
        import aws_sdk_resiliencehubv2.types.disaster_recovery_source

        out["multi_region_dr_approach"] = (
            aws_sdk_resiliencehubv2.types.disaster_recovery_source.deserialize_json(
                data["multiRegionDrApproach"]
            )
        )
    if "dataRecoveryTimeBetweenBackups" in data:
        import aws_sdk_resiliencehubv2.types.target_source

        out["data_recovery_time_between_backups"] = (
            aws_sdk_resiliencehubv2.types.target_source.deserialize_json(
                data["dataRecoveryTimeBetweenBackups"]
            )
        )
    return out
