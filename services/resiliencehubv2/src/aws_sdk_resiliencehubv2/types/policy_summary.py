"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#PolicySummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_resiliencehubv2.types.arn
    import aws_sdk_resiliencehubv2.types.availability_slo
    import aws_sdk_resiliencehubv2.types.data_recovery_targets
    import aws_sdk_resiliencehubv2.types.entity_name
    import aws_sdk_resiliencehubv2.types.multi_az_targets
    import aws_sdk_resiliencehubv2.types.multi_region_targets


class PolicySummary(TypedDict):
    policy_arn: "aws_sdk_resiliencehubv2.types.arn.Arn"
    name: "aws_sdk_resiliencehubv2.types.entity_name.EntityName"
    availability_slo: NotRequired[
        "aws_sdk_resiliencehubv2.types.availability_slo.AvailabilitySlo"
    ]
    """<p>The availability SLO defined in the policy.</p>"""
    multi_az: NotRequired[
        "aws_sdk_resiliencehubv2.types.multi_az_targets.MultiAzTargets"
    ]
    """<p>The multi-AZ disaster recovery targets defined in the policy.</p>"""
    multi_region: NotRequired[
        "aws_sdk_resiliencehubv2.types.multi_region_targets.MultiRegionTargets"
    ]
    """<p>The multi-Region disaster recovery targets defined in the policy.</p>"""
    data_recovery: NotRequired[
        "aws_sdk_resiliencehubv2.types.data_recovery_targets.DataRecoveryTargets"
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
        import aws_sdk_resiliencehubv2.types.availability_slo

        out["availabilitySlo"] = (
            aws_sdk_resiliencehubv2.types.availability_slo.serialize_json(
                value["availability_slo"]
            )
        )
    if "multi_az" in value:
        import aws_sdk_resiliencehubv2.types.multi_az_targets

        out["multiAz"] = aws_sdk_resiliencehubv2.types.multi_az_targets.serialize_json(
            value["multi_az"]
        )
    if "multi_region" in value:
        import aws_sdk_resiliencehubv2.types.multi_region_targets

        out["multiRegion"] = (
            aws_sdk_resiliencehubv2.types.multi_region_targets.serialize_json(
                value["multi_region"]
            )
        )
    if "data_recovery" in value:
        import aws_sdk_resiliencehubv2.types.data_recovery_targets

        out["dataRecovery"] = (
            aws_sdk_resiliencehubv2.types.data_recovery_targets.serialize_json(
                value["data_recovery"]
            )
        )
    if "associated_service_count" in value:
        out["associatedServiceCount"] = value["associated_service_count"]
    if "created_at" in value:
        import aws_sdk_resiliencehubv2.types._prelude.timestamp

        out["createdAt"] = (
            aws_sdk_resiliencehubv2.types._prelude.timestamp.serialize_json(
                value["created_at"]
            )
        )
    if "updated_at" in value:
        import aws_sdk_resiliencehubv2.types._prelude.timestamp

        out["updatedAt"] = (
            aws_sdk_resiliencehubv2.types._prelude.timestamp.serialize_json(
                value["updated_at"]
            )
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
        import aws_sdk_resiliencehubv2.types.availability_slo

        out["availability_slo"] = (
            aws_sdk_resiliencehubv2.types.availability_slo.deserialize_json(
                data["availabilitySlo"]
            )
        )
    if "multiAz" in data:
        import aws_sdk_resiliencehubv2.types.multi_az_targets

        out["multi_az"] = (
            aws_sdk_resiliencehubv2.types.multi_az_targets.deserialize_json(
                data["multiAz"]
            )
        )
    if "multiRegion" in data:
        import aws_sdk_resiliencehubv2.types.multi_region_targets

        out["multi_region"] = (
            aws_sdk_resiliencehubv2.types.multi_region_targets.deserialize_json(
                data["multiRegion"]
            )
        )
    if "dataRecovery" in data:
        import aws_sdk_resiliencehubv2.types.data_recovery_targets

        out["data_recovery"] = (
            aws_sdk_resiliencehubv2.types.data_recovery_targets.deserialize_json(
                data["dataRecovery"]
            )
        )
    if "associatedServiceCount" in data:
        out["associated_service_count"] = data["associatedServiceCount"]
    if "createdAt" in data:
        import aws_sdk_resiliencehubv2.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if "updatedAt" in data:
        import aws_sdk_resiliencehubv2.types._prelude.timestamp

        out["updated_at"] = (
            aws_sdk_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    return out
