"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#PolicySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.availability_slo
    import capo_resiliencehubv2.types.data_recovery_targets
    import capo_resiliencehubv2.types.entity_name
    import capo_resiliencehubv2.types.multi_az_targets
    import capo_resiliencehubv2.types.multi_region_targets


class PolicySummary(TypedDict, closed=True):
    policy_arn: "capo_resiliencehubv2.types.arn.Arn"
    name: "capo_resiliencehubv2.types.entity_name.EntityName"
    availability_slo: NotRequired[
        "capo_resiliencehubv2.types.availability_slo.AvailabilitySlo"
    ]
    """<p>The availability SLO defined in the policy.</p>"""
    multi_az: NotRequired["capo_resiliencehubv2.types.multi_az_targets.MultiAzTargets"]
    """<p>The multi-AZ disaster recovery targets defined in the policy.</p>"""
    multi_region: NotRequired[
        "capo_resiliencehubv2.types.multi_region_targets.MultiRegionTargets"
    ]
    """<p>The multi-Region disaster recovery targets defined in the policy.</p>"""
    data_recovery: NotRequired[
        "capo_resiliencehubv2.types.data_recovery_targets.DataRecoveryTargets"
    ]
    """<p>The data recovery targets defined in the policy.</p>"""
    associated_service_count: NotRequired["int"]
    """<p>The number of services associated with this policy.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the policy was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the policy was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PolicySummary) -> dict:
    out: dict = {}
    out["policyArn"] = value["policy_arn"]
    out["name"] = value["name"]
    if "availability_slo" in value:
        import capo_resiliencehubv2.types.availability_slo

        out["availabilitySlo"] = (
            capo_resiliencehubv2.types.availability_slo.serialize_json(
                value["availability_slo"]
            )
        )
    if "multi_az" in value:
        import capo_resiliencehubv2.types.multi_az_targets

        out["multiAz"] = capo_resiliencehubv2.types.multi_az_targets.serialize_json(
            value["multi_az"]
        )
    if "multi_region" in value:
        import capo_resiliencehubv2.types.multi_region_targets

        out["multiRegion"] = (
            capo_resiliencehubv2.types.multi_region_targets.serialize_json(
                value["multi_region"]
            )
        )
    if "data_recovery" in value:
        import capo_resiliencehubv2.types.data_recovery_targets

        out["dataRecovery"] = (
            capo_resiliencehubv2.types.data_recovery_targets.serialize_json(
                value["data_recovery"]
            )
        )
    if "associated_service_count" in value:
        out["associatedServiceCount"] = value["associated_service_count"]
    if "created_at" in value:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["createdAt"] = capo_resiliencehubv2.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["updatedAt"] = capo_resiliencehubv2.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> PolicySummary:
    out: PolicySummary = {}  # type: ignore[typeddict-item]
    if "policyArn" in data:
        out["policy_arn"] = data["policyArn"]
    else:
        raise DeserializationError("PolicySummary.policy_arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("PolicySummary.name required")
    if "availabilitySlo" in data:
        import capo_resiliencehubv2.types.availability_slo

        out["availability_slo"] = (
            capo_resiliencehubv2.types.availability_slo.deserialize_json(
                data["availabilitySlo"]
            )
        )
    if "multiAz" in data:
        import capo_resiliencehubv2.types.multi_az_targets

        out["multi_az"] = capo_resiliencehubv2.types.multi_az_targets.deserialize_json(
            data["multiAz"]
        )
    if "multiRegion" in data:
        import capo_resiliencehubv2.types.multi_region_targets

        out["multi_region"] = (
            capo_resiliencehubv2.types.multi_region_targets.deserialize_json(
                data["multiRegion"]
            )
        )
    if "dataRecovery" in data:
        import capo_resiliencehubv2.types.data_recovery_targets

        out["data_recovery"] = (
            capo_resiliencehubv2.types.data_recovery_targets.deserialize_json(
                data["dataRecovery"]
            )
        )
    if "associatedServiceCount" in data:
        out["associated_service_count"] = data["associatedServiceCount"]
    if "createdAt" in data:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["created_at"] = (
            capo_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if "updatedAt" in data:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["updated_at"] = (
            capo_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    return out
