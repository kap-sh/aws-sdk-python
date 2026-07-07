"""Generated from Smithy shape ``com.amazonaws.wellarchitected#WorkloadSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.aws_account_id
    import aws_sdk_wellarchitected.types.risk_counts
    import aws_sdk_wellarchitected.types.timestamp
    import aws_sdk_wellarchitected.types.workload_arn
    import aws_sdk_wellarchitected.types.workload_id
    import aws_sdk_wellarchitected.types.workload_improvement_status
    import aws_sdk_wellarchitected.types.workload_lenses
    import aws_sdk_wellarchitected.types.workload_name
    import aws_sdk_wellarchitected.types.workload_profiles


class WorkloadSummary(TypedDict, closed=True):
    workload_id: NotRequired["aws_sdk_wellarchitected.types.workload_id.WorkloadId"]
    workload_arn: NotRequired["aws_sdk_wellarchitected.types.workload_arn.WorkloadArn"]
    workload_name: NotRequired[
        "aws_sdk_wellarchitected.types.workload_name.WorkloadName"
    ]
    owner: NotRequired["aws_sdk_wellarchitected.types.aws_account_id.AwsAccountId"]
    updated_at: NotRequired["aws_sdk_wellarchitected.types.timestamp.Timestamp"]
    lenses: NotRequired["aws_sdk_wellarchitected.types.workload_lenses.WorkloadLenses"]
    risk_counts: NotRequired["aws_sdk_wellarchitected.types.risk_counts.RiskCounts"]
    improvement_status: NotRequired[
        "aws_sdk_wellarchitected.types.workload_improvement_status.WorkloadImprovementStatus"
    ]
    profiles: NotRequired[
        "aws_sdk_wellarchitected.types.workload_profiles.WorkloadProfiles"
    ]
    """<p>Profile associated with a workload.</p>"""
    prioritized_risk_counts: NotRequired[
        "aws_sdk_wellarchitected.types.risk_counts.RiskCounts"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: WorkloadSummary) -> dict:
    out: dict = {}
    if "workload_id" in value:
        out["WorkloadId"] = value["workload_id"]
    if "workload_arn" in value:
        out["WorkloadArn"] = value["workload_arn"]
    if "workload_name" in value:
        out["WorkloadName"] = value["workload_name"]
    if "owner" in value:
        out["Owner"] = value["owner"]
    if "updated_at" in value:
        import aws_sdk_wellarchitected.types.timestamp

        out["UpdatedAt"] = aws_sdk_wellarchitected.types.timestamp.serialize_json(
            value["updated_at"]
        )
    if "lenses" in value:
        import aws_sdk_wellarchitected.types.workload_lenses

        out["Lenses"] = aws_sdk_wellarchitected.types.workload_lenses.serialize_json(
            value["lenses"]
        )
    if "risk_counts" in value:
        import aws_sdk_wellarchitected.types.risk_counts

        out["RiskCounts"] = aws_sdk_wellarchitected.types.risk_counts.serialize_json(
            value["risk_counts"]
        )
    if "improvement_status" in value:
        import aws_sdk_wellarchitected.types.workload_improvement_status

        out["ImprovementStatus"] = (
            aws_sdk_wellarchitected.types.workload_improvement_status.serialize_json(
                value["improvement_status"]
            )
        )
    if "profiles" in value:
        import aws_sdk_wellarchitected.types.workload_profiles

        out["Profiles"] = (
            aws_sdk_wellarchitected.types.workload_profiles.serialize_json(
                value["profiles"]
            )
        )
    if "prioritized_risk_counts" in value:
        import aws_sdk_wellarchitected.types.risk_counts

        out["PrioritizedRiskCounts"] = (
            aws_sdk_wellarchitected.types.risk_counts.serialize_json(
                value["prioritized_risk_counts"]
            )
        )
    return out


def deserialize_json(data: dict) -> WorkloadSummary:
    out: WorkloadSummary = {}  # type: ignore[typeddict-item]
    if "WorkloadId" in data:
        out["workload_id"] = data["WorkloadId"]
    if "WorkloadArn" in data:
        out["workload_arn"] = data["WorkloadArn"]
    if "WorkloadName" in data:
        out["workload_name"] = data["WorkloadName"]
    if "Owner" in data:
        out["owner"] = data["Owner"]
    if "UpdatedAt" in data:
        import aws_sdk_wellarchitected.types.timestamp

        out["updated_at"] = aws_sdk_wellarchitected.types.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    if "Lenses" in data:
        import aws_sdk_wellarchitected.types.workload_lenses

        out["lenses"] = aws_sdk_wellarchitected.types.workload_lenses.deserialize_json(
            data["Lenses"]
        )
    if "RiskCounts" in data:
        import aws_sdk_wellarchitected.types.risk_counts

        out["risk_counts"] = aws_sdk_wellarchitected.types.risk_counts.deserialize_json(
            data["RiskCounts"]
        )
    if "ImprovementStatus" in data:
        import aws_sdk_wellarchitected.types.workload_improvement_status

        out["improvement_status"] = (
            aws_sdk_wellarchitected.types.workload_improvement_status.deserialize_json(
                data["ImprovementStatus"]
            )
        )
    if "Profiles" in data:
        import aws_sdk_wellarchitected.types.workload_profiles

        out["profiles"] = (
            aws_sdk_wellarchitected.types.workload_profiles.deserialize_json(
                data["Profiles"]
            )
        )
    if "PrioritizedRiskCounts" in data:
        import aws_sdk_wellarchitected.types.risk_counts

        out["prioritized_risk_counts"] = (
            aws_sdk_wellarchitected.types.risk_counts.deserialize_json(
                data["PrioritizedRiskCounts"]
            )
        )
    return out
