"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#MultiAzTargets``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.multi_az_disaster_recovery_approach


class MultiAzTargets(TypedDict):
    rto_in_minutes: NotRequired["int"]
    """<p>The recovery time objective (RTO) target for multi-AZ, in minutes.</p>"""
    rpo_in_minutes: NotRequired["int"]
    """<p>The recovery point objective (RPO) target for multi-AZ, in minutes.</p>"""
    disaster_recovery_approach: NotRequired[
        "aws_sdk_resiliencehubv2.types.multi_az_disaster_recovery_approach.MultiAzDisasterRecoveryApproach"
    ]
    """<p>The disaster recovery approach for multi-AZ.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MultiAzTargets) -> dict:
    out: dict = {}
    if "rto_in_minutes" in value:
        out["rtoInMinutes"] = value["rto_in_minutes"]
    if "rpo_in_minutes" in value:
        out["rpoInMinutes"] = value["rpo_in_minutes"]
    if "disaster_recovery_approach" in value:
        import aws_sdk_resiliencehubv2.types.multi_az_disaster_recovery_approach

        out["disasterRecoveryApproach"] = (
            aws_sdk_resiliencehubv2.types.multi_az_disaster_recovery_approach.serialize_json(
                value["disaster_recovery_approach"]
            )
        )
    return out


def deserialize_json(data: dict) -> MultiAzTargets:
    out: MultiAzTargets = {}  # type: ignore[typeddict-item]
    if "rtoInMinutes" in data:
        out["rto_in_minutes"] = data["rtoInMinutes"]
    if "rpoInMinutes" in data:
        out["rpo_in_minutes"] = data["rpoInMinutes"]
    if "disasterRecoveryApproach" in data:
        import aws_sdk_resiliencehubv2.types.multi_az_disaster_recovery_approach

        out["disaster_recovery_approach"] = (
            aws_sdk_resiliencehubv2.types.multi_az_disaster_recovery_approach.deserialize_json(
                data["disasterRecoveryApproach"]
            )
        )
    return out
