"""Generated from Smithy shape ``com.amazonaws.wellarchitected#LensReviewSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.lens_alias
    import capo_wellarchitected.types.lens_arn
    import capo_wellarchitected.types.lens_name
    import capo_wellarchitected.types.lens_status
    import capo_wellarchitected.types.lens_version
    import capo_wellarchitected.types.risk_counts
    import capo_wellarchitected.types.timestamp
    import capo_wellarchitected.types.workload_profiles


class LensReviewSummary(TypedDict, closed=True):
    lens_alias: NotRequired["capo_wellarchitected.types.lens_alias.LensAlias"]
    lens_arn: NotRequired["capo_wellarchitected.types.lens_arn.LensArn"]
    """<p>The ARN for the lens.</p>"""
    lens_version: NotRequired["capo_wellarchitected.types.lens_version.LensVersion"]
    """<p>The version of the lens.</p>"""
    lens_name: NotRequired["capo_wellarchitected.types.lens_name.LensName"]
    lens_status: NotRequired["capo_wellarchitected.types.lens_status.LensStatus"]
    """<p>The status of the lens.</p>"""
    updated_at: NotRequired["capo_wellarchitected.types.timestamp.Timestamp"]
    risk_counts: NotRequired["capo_wellarchitected.types.risk_counts.RiskCounts"]
    profiles: NotRequired[
        "capo_wellarchitected.types.workload_profiles.WorkloadProfiles"
    ]
    """<p>The profiles associated with the workload.</p>"""
    prioritized_risk_counts: NotRequired[
        "capo_wellarchitected.types.risk_counts.RiskCounts"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: LensReviewSummary) -> dict:
    out: dict = {}
    if "lens_alias" in value:
        out["LensAlias"] = value["lens_alias"]
    if "lens_arn" in value:
        out["LensArn"] = value["lens_arn"]
    if "lens_version" in value:
        out["LensVersion"] = value["lens_version"]
    if "lens_name" in value:
        out["LensName"] = value["lens_name"]
    if "lens_status" in value:
        import capo_wellarchitected.types.lens_status

        out["LensStatus"] = capo_wellarchitected.types.lens_status.serialize_json(
            value["lens_status"]
        )
    if "updated_at" in value:
        import capo_wellarchitected.types.timestamp

        out["UpdatedAt"] = capo_wellarchitected.types.timestamp.serialize_json(
            value["updated_at"]
        )
    if "risk_counts" in value:
        import capo_wellarchitected.types.risk_counts

        out["RiskCounts"] = capo_wellarchitected.types.risk_counts.serialize_json(
            value["risk_counts"]
        )
    if "profiles" in value:
        import capo_wellarchitected.types.workload_profiles

        out["Profiles"] = capo_wellarchitected.types.workload_profiles.serialize_json(
            value["profiles"]
        )
    if "prioritized_risk_counts" in value:
        import capo_wellarchitected.types.risk_counts

        out["PrioritizedRiskCounts"] = (
            capo_wellarchitected.types.risk_counts.serialize_json(
                value["prioritized_risk_counts"]
            )
        )
    return out


def deserialize_json(data: dict) -> LensReviewSummary:
    out: LensReviewSummary = {}  # type: ignore[typeddict-item]
    if "LensAlias" in data:
        out["lens_alias"] = data["LensAlias"]
    if "LensArn" in data:
        out["lens_arn"] = data["LensArn"]
    if "LensVersion" in data:
        out["lens_version"] = data["LensVersion"]
    if "LensName" in data:
        out["lens_name"] = data["LensName"]
    if "LensStatus" in data:
        import capo_wellarchitected.types.lens_status

        out["lens_status"] = capo_wellarchitected.types.lens_status.deserialize_json(
            data["LensStatus"]
        )
    if "UpdatedAt" in data:
        import capo_wellarchitected.types.timestamp

        out["updated_at"] = capo_wellarchitected.types.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    if "RiskCounts" in data:
        import capo_wellarchitected.types.risk_counts

        out["risk_counts"] = capo_wellarchitected.types.risk_counts.deserialize_json(
            data["RiskCounts"]
        )
    if "Profiles" in data:
        import capo_wellarchitected.types.workload_profiles

        out["profiles"] = capo_wellarchitected.types.workload_profiles.deserialize_json(
            data["Profiles"]
        )
    if "PrioritizedRiskCounts" in data:
        import capo_wellarchitected.types.risk_counts

        out["prioritized_risk_counts"] = (
            capo_wellarchitected.types.risk_counts.deserialize_json(
                data["PrioritizedRiskCounts"]
            )
        )
    return out
