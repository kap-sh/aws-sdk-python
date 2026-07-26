"""Generated from Smithy shape ``com.amazonaws.wellarchitected#LensReview``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.jira_selected_question_configuration
    import capo_wellarchitected.types.lens_alias
    import capo_wellarchitected.types.lens_arn
    import capo_wellarchitected.types.lens_name
    import capo_wellarchitected.types.lens_status
    import capo_wellarchitected.types.lens_version
    import capo_wellarchitected.types.next_token
    import capo_wellarchitected.types.notes
    import capo_wellarchitected.types.pillar_review_summaries
    import capo_wellarchitected.types.risk_counts
    import capo_wellarchitected.types.timestamp
    import capo_wellarchitected.types.workload_profiles


class LensReview(TypedDict, closed=True):
    lens_alias: NotRequired["capo_wellarchitected.types.lens_alias.LensAlias"]
    lens_arn: NotRequired["capo_wellarchitected.types.lens_arn.LensArn"]
    """<p>The ARN for the lens.</p>"""
    lens_version: NotRequired["capo_wellarchitected.types.lens_version.LensVersion"]
    """<p>The version of the lens.</p>"""
    lens_name: NotRequired["capo_wellarchitected.types.lens_name.LensName"]
    lens_status: NotRequired["capo_wellarchitected.types.lens_status.LensStatus"]
    """<p>The status of the lens.</p>"""
    pillar_review_summaries: NotRequired[
        "capo_wellarchitected.types.pillar_review_summaries.PillarReviewSummaries"
    ]
    jira_configuration: NotRequired[
        "capo_wellarchitected.types.jira_selected_question_configuration.JiraSelectedQuestionConfiguration"
    ]
    """<p>Jira configuration status of the Lens review.</p>"""
    updated_at: NotRequired["capo_wellarchitected.types.timestamp.Timestamp"]
    notes: NotRequired["capo_wellarchitected.types.notes.Notes"]
    risk_counts: NotRequired["capo_wellarchitected.types.risk_counts.RiskCounts"]
    next_token: NotRequired["capo_wellarchitected.types.next_token.NextToken"]
    profiles: NotRequired[
        "capo_wellarchitected.types.workload_profiles.WorkloadProfiles"
    ]
    """<p>The profiles associated with the workload.</p>"""
    prioritized_risk_counts: NotRequired[
        "capo_wellarchitected.types.risk_counts.RiskCounts"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: LensReview) -> dict:
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
    if "pillar_review_summaries" in value:
        import capo_wellarchitected.types.pillar_review_summaries

        out["PillarReviewSummaries"] = (
            capo_wellarchitected.types.pillar_review_summaries.serialize_json(
                value["pillar_review_summaries"]
            )
        )
    if "jira_configuration" in value:
        import capo_wellarchitected.types.jira_selected_question_configuration

        out["JiraConfiguration"] = (
            capo_wellarchitected.types.jira_selected_question_configuration.serialize_json(
                value["jira_configuration"]
            )
        )
    if "updated_at" in value:
        import capo_wellarchitected.types.timestamp

        out["UpdatedAt"] = capo_wellarchitected.types.timestamp.serialize_json(
            value["updated_at"]
        )
    if "notes" in value:
        out["Notes"] = value["notes"]
    if "risk_counts" in value:
        import capo_wellarchitected.types.risk_counts

        out["RiskCounts"] = capo_wellarchitected.types.risk_counts.serialize_json(
            value["risk_counts"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
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


def deserialize_json(data: dict) -> LensReview:
    out: LensReview = {}  # type: ignore[typeddict-item]
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
    if "PillarReviewSummaries" in data:
        import capo_wellarchitected.types.pillar_review_summaries

        out["pillar_review_summaries"] = (
            capo_wellarchitected.types.pillar_review_summaries.deserialize_json(
                data["PillarReviewSummaries"]
            )
        )
    if "JiraConfiguration" in data:
        import capo_wellarchitected.types.jira_selected_question_configuration

        out["jira_configuration"] = (
            capo_wellarchitected.types.jira_selected_question_configuration.deserialize_json(
                data["JiraConfiguration"]
            )
        )
    if "UpdatedAt" in data:
        import capo_wellarchitected.types.timestamp

        out["updated_at"] = capo_wellarchitected.types.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    if "Notes" in data:
        out["notes"] = data["Notes"]
    if "RiskCounts" in data:
        import capo_wellarchitected.types.risk_counts

        out["risk_counts"] = capo_wellarchitected.types.risk_counts.deserialize_json(
            data["RiskCounts"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
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
