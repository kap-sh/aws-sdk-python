"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#UpdatePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.availability_slo
    import capo_resiliencehubv2.types.data_recovery_targets
    import capo_resiliencehubv2.types.long_description
    import capo_resiliencehubv2.types.multi_az_targets
    import capo_resiliencehubv2.types.multi_region_targets


class UpdatePolicyRequest(TypedDict, closed=True):
    policy_arn: "capo_resiliencehubv2.types.arn.Arn"
    description: NotRequired[
        "capo_resiliencehubv2.types.long_description.LongDescription"
    ]
    availability_slo: NotRequired[
        "capo_resiliencehubv2.types.availability_slo.AvailabilitySlo"
    ]
    """<p>The updated availability SLO for the policy.</p>"""
    multi_az: NotRequired["capo_resiliencehubv2.types.multi_az_targets.MultiAzTargets"]
    """<p>The updated multi-AZ disaster recovery targets for the policy.</p>"""
    multi_region: NotRequired[
        "capo_resiliencehubv2.types.multi_region_targets.MultiRegionTargets"
    ]
    """<p>The updated multi-Region disaster recovery targets for the policy.</p>"""
    data_recovery: NotRequired[
        "capo_resiliencehubv2.types.data_recovery_targets.DataRecoveryTargets"
    ]
    """<p>The updated data recovery targets for the policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePolicyRequest) -> dict:
    out: dict = {}
    out["policyArn"] = value["policy_arn"]
    if "description" in value:
        out["description"] = value["description"]
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
    return out


def deserialize_json(data: dict) -> UpdatePolicyRequest:
    out: UpdatePolicyRequest = {}  # type: ignore[typeddict-item]
    if "policyArn" in data:
        out["policy_arn"] = data["policyArn"]
    else:
        raise DeserializationError("UpdatePolicyRequest.policy_arn required")
    if "description" in data:
        out["description"] = data["description"]
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
    return out
