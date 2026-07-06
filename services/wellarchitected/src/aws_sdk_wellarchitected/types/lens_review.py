"""Generated from Smithy shape ``com.amazonaws.wellarchitected#LensReview``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.jira_selected_question_configuration
    import aws_sdk_wellarchitected.types.lens_alias
    import aws_sdk_wellarchitected.types.lens_arn
    import aws_sdk_wellarchitected.types.lens_name
    import aws_sdk_wellarchitected.types.lens_status
    import aws_sdk_wellarchitected.types.lens_version
    import aws_sdk_wellarchitected.types.next_token
    import aws_sdk_wellarchitected.types.notes
    import aws_sdk_wellarchitected.types.pillar_review_summaries
    import aws_sdk_wellarchitected.types.risk_counts
    import aws_sdk_wellarchitected.types.timestamp
    import aws_sdk_wellarchitected.types.workload_profiles


class LensReview(TypedDict, closed=True):
    lens_alias: NotRequired["aws_sdk_wellarchitected.types.lens_alias.LensAlias"]
    lens_arn: NotRequired["aws_sdk_wellarchitected.types.lens_arn.LensArn"]
    """<p>The ARN for the lens.</p>"""
    lens_version: NotRequired["aws_sdk_wellarchitected.types.lens_version.LensVersion"]
    """<p>The version of the lens.</p>"""
    lens_name: NotRequired["aws_sdk_wellarchitected.types.lens_name.LensName"]
    lens_status: NotRequired["aws_sdk_wellarchitected.types.lens_status.LensStatus"]
    """<p>The status of the lens.</p>"""
    pillar_review_summaries: NotRequired[
        "aws_sdk_wellarchitected.types.pillar_review_summaries.PillarReviewSummaries"
    ]
    jira_configuration: NotRequired[
        "aws_sdk_wellarchitected.types.jira_selected_question_configuration.JiraSelectedQuestionConfiguration"
    ]
    """<p>Jira configuration status of the Lens review.</p>"""
    updated_at: NotRequired["aws_sdk_wellarchitected.types.timestamp.Timestamp"]
    notes: NotRequired["aws_sdk_wellarchitected.types.notes.Notes"]
    risk_counts: NotRequired["aws_sdk_wellarchitected.types.risk_counts.RiskCounts"]
    next_token: NotRequired["aws_sdk_wellarchitected.types.next_token.NextToken"]
    profiles: NotRequired[
        "aws_sdk_wellarchitected.types.workload_profiles.WorkloadProfiles"
    ]
    """<p>The profiles associated with the workload.</p>"""
    prioritized_risk_counts: NotRequired[
        "aws_sdk_wellarchitected.types.risk_counts.RiskCounts"
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
        import aws_sdk_wellarchitected.types.lens_status

        out["LensStatus"] = aws_sdk_wellarchitected.types.lens_status.serialize_json(
            value["lens_status"]
        )
    if "pillar_review_summaries" in value:
        import aws_sdk_wellarchitected.types.pillar_review_summaries

        out["PillarReviewSummaries"] = (
            aws_sdk_wellarchitected.types.pillar_review_summaries.serialize_json(
                value["pillar_review_summaries"]
            )
        )
    if "jira_configuration" in value:
        import aws_sdk_wellarchitected.types.jira_selected_question_configuration

        out["JiraConfiguration"] = (
            aws_sdk_wellarchitected.types.jira_selected_question_configuration.serialize_json(
                value["jira_configuration"]
            )
        )
    if "updated_at" in value:
        import aws_sdk_wellarchitected.types.timestamp

        out["UpdatedAt"] = aws_sdk_wellarchitected.types.timestamp.serialize_json(
            value["updated_at"]
        )
    if "notes" in value:
        out["Notes"] = value["notes"]
    if "risk_counts" in value:
        import aws_sdk_wellarchitected.types.risk_counts

        out["RiskCounts"] = aws_sdk_wellarchitected.types.risk_counts.serialize_json(
            value["risk_counts"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
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
        import aws_sdk_wellarchitected.types.lens_status

        out["lens_status"] = aws_sdk_wellarchitected.types.lens_status.deserialize_json(
            data["LensStatus"]
        )
    if "PillarReviewSummaries" in data:
        import aws_sdk_wellarchitected.types.pillar_review_summaries

        out["pillar_review_summaries"] = (
            aws_sdk_wellarchitected.types.pillar_review_summaries.deserialize_json(
                data["PillarReviewSummaries"]
            )
        )
    if "JiraConfiguration" in data:
        import aws_sdk_wellarchitected.types.jira_selected_question_configuration

        out["jira_configuration"] = (
            aws_sdk_wellarchitected.types.jira_selected_question_configuration.deserialize_json(
                data["JiraConfiguration"]
            )
        )
    if "UpdatedAt" in data:
        import aws_sdk_wellarchitected.types.timestamp

        out["updated_at"] = aws_sdk_wellarchitected.types.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    if "Notes" in data:
        out["notes"] = data["Notes"]
    if "RiskCounts" in data:
        import aws_sdk_wellarchitected.types.risk_counts

        out["risk_counts"] = aws_sdk_wellarchitected.types.risk_counts.deserialize_json(
            data["RiskCounts"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
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
