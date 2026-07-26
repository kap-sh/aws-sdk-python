"""Generated from Smithy shape ``com.amazonaws.wellarchitected#Workload``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.aws_account_id
    import capo_wellarchitected.types.is_review_owner_update_acknowledged
    import capo_wellarchitected.types.notes
    import capo_wellarchitected.types.risk_counts
    import capo_wellarchitected.types.share_invitation_id
    import capo_wellarchitected.types.tag_map
    import capo_wellarchitected.types.timestamp
    import capo_wellarchitected.types.workload_account_ids
    import capo_wellarchitected.types.workload_applications
    import capo_wellarchitected.types.workload_architectural_design
    import capo_wellarchitected.types.workload_arn
    import capo_wellarchitected.types.workload_aws_regions
    import capo_wellarchitected.types.workload_description
    import capo_wellarchitected.types.workload_discovery_config
    import capo_wellarchitected.types.workload_environment
    import capo_wellarchitected.types.workload_id
    import capo_wellarchitected.types.workload_improvement_status
    import capo_wellarchitected.types.workload_industry
    import capo_wellarchitected.types.workload_industry_type
    import capo_wellarchitected.types.workload_jira_configuration_output
    import capo_wellarchitected.types.workload_lenses
    import capo_wellarchitected.types.workload_name
    import capo_wellarchitected.types.workload_non_aws_regions
    import capo_wellarchitected.types.workload_pillar_priorities
    import capo_wellarchitected.types.workload_profiles
    import capo_wellarchitected.types.workload_review_owner


class Workload(TypedDict, closed=True):
    workload_id: NotRequired["capo_wellarchitected.types.workload_id.WorkloadId"]
    workload_arn: NotRequired["capo_wellarchitected.types.workload_arn.WorkloadArn"]
    workload_name: NotRequired["capo_wellarchitected.types.workload_name.WorkloadName"]
    description: NotRequired[
        "capo_wellarchitected.types.workload_description.WorkloadDescription"
    ]
    environment: NotRequired[
        "capo_wellarchitected.types.workload_environment.WorkloadEnvironment"
    ]
    updated_at: NotRequired["capo_wellarchitected.types.timestamp.Timestamp"]
    account_ids: NotRequired[
        "capo_wellarchitected.types.workload_account_ids.WorkloadAccountIds"
    ]
    aws_regions: NotRequired[
        "capo_wellarchitected.types.workload_aws_regions.WorkloadAwsRegions"
    ]
    non_aws_regions: NotRequired[
        "capo_wellarchitected.types.workload_non_aws_regions.WorkloadNonAwsRegions"
    ]
    architectural_design: NotRequired[
        "capo_wellarchitected.types.workload_architectural_design.WorkloadArchitecturalDesign"
    ]
    review_owner: NotRequired[
        "capo_wellarchitected.types.workload_review_owner.WorkloadReviewOwner"
    ]
    review_restriction_date: NotRequired[
        "capo_wellarchitected.types.timestamp.Timestamp"
    ]
    is_review_owner_update_acknowledged: NotRequired[
        "capo_wellarchitected.types.is_review_owner_update_acknowledged.IsReviewOwnerUpdateAcknowledged"
    ]
    """<p>Flag indicating whether the workload owner has acknowledged that the <i>Review owner</i> field is required.</p> <p>If a <b>Review owner</b> is not added to the workload within 60 days of acknowledgement, access to the workload is restricted until an owner is added.</p>"""
    industry_type: NotRequired[
        "capo_wellarchitected.types.workload_industry_type.WorkloadIndustryType"
    ]
    industry: NotRequired[
        "capo_wellarchitected.types.workload_industry.WorkloadIndustry"
    ]
    notes: NotRequired["capo_wellarchitected.types.notes.Notes"]
    improvement_status: NotRequired[
        "capo_wellarchitected.types.workload_improvement_status.WorkloadImprovementStatus"
    ]
    risk_counts: NotRequired["capo_wellarchitected.types.risk_counts.RiskCounts"]
    pillar_priorities: NotRequired[
        "capo_wellarchitected.types.workload_pillar_priorities.WorkloadPillarPriorities"
    ]
    lenses: NotRequired["capo_wellarchitected.types.workload_lenses.WorkloadLenses"]
    owner: NotRequired["capo_wellarchitected.types.aws_account_id.AwsAccountId"]
    share_invitation_id: NotRequired[
        "capo_wellarchitected.types.share_invitation_id.ShareInvitationId"
    ]
    """<p>The ID assigned to the share invitation.</p>"""
    tags: NotRequired["capo_wellarchitected.types.tag_map.TagMap"]
    """<p>The tags associated with the workload.</p>"""
    discovery_config: NotRequired[
        "capo_wellarchitected.types.workload_discovery_config.WorkloadDiscoveryConfig"
    ]
    """<p>Discovery configuration associated to the workload.</p>"""
    applications: NotRequired[
        "capo_wellarchitected.types.workload_applications.WorkloadApplications"
    ]
    """<p>List of AppRegistry application ARNs associated to the workload.</p>"""
    profiles: NotRequired[
        "capo_wellarchitected.types.workload_profiles.WorkloadProfiles"
    ]
    """<p>Profile associated with a workload.</p>"""
    prioritized_risk_counts: NotRequired[
        "capo_wellarchitected.types.risk_counts.RiskCounts"
    ]
    jira_configuration: NotRequired[
        "capo_wellarchitected.types.workload_jira_configuration_output.WorkloadJiraConfigurationOutput"
    ]
    """<p>Jira configuration for a specific workload.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Workload) -> dict:
    out: dict = {}
    if "workload_id" in value:
        out["WorkloadId"] = value["workload_id"]
    if "workload_arn" in value:
        out["WorkloadArn"] = value["workload_arn"]
    if "workload_name" in value:
        out["WorkloadName"] = value["workload_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "environment" in value:
        import capo_wellarchitected.types.workload_environment

        out["Environment"] = (
            capo_wellarchitected.types.workload_environment.serialize_json(
                value["environment"]
            )
        )
    if "updated_at" in value:
        import capo_wellarchitected.types.timestamp

        out["UpdatedAt"] = capo_wellarchitected.types.timestamp.serialize_json(
            value["updated_at"]
        )
    if "account_ids" in value:
        import capo_wellarchitected.types.workload_account_ids

        out["AccountIds"] = (
            capo_wellarchitected.types.workload_account_ids.serialize_json(
                value["account_ids"]
            )
        )
    if "aws_regions" in value:
        import capo_wellarchitected.types.workload_aws_regions

        out["AwsRegions"] = (
            capo_wellarchitected.types.workload_aws_regions.serialize_json(
                value["aws_regions"]
            )
        )
    if "non_aws_regions" in value:
        import capo_wellarchitected.types.workload_non_aws_regions

        out["NonAwsRegions"] = (
            capo_wellarchitected.types.workload_non_aws_regions.serialize_json(
                value["non_aws_regions"]
            )
        )
    if "architectural_design" in value:
        out["ArchitecturalDesign"] = value["architectural_design"]
    if "review_owner" in value:
        out["ReviewOwner"] = value["review_owner"]
    if "review_restriction_date" in value:
        import capo_wellarchitected.types.timestamp

        out["ReviewRestrictionDate"] = (
            capo_wellarchitected.types.timestamp.serialize_json(
                value["review_restriction_date"]
            )
        )
    if "is_review_owner_update_acknowledged" in value:
        out["IsReviewOwnerUpdateAcknowledged"] = value[
            "is_review_owner_update_acknowledged"
        ]
    if "industry_type" in value:
        out["IndustryType"] = value["industry_type"]
    if "industry" in value:
        out["Industry"] = value["industry"]
    if "notes" in value:
        out["Notes"] = value["notes"]
    if "improvement_status" in value:
        import capo_wellarchitected.types.workload_improvement_status

        out["ImprovementStatus"] = (
            capo_wellarchitected.types.workload_improvement_status.serialize_json(
                value["improvement_status"]
            )
        )
    if "risk_counts" in value:
        import capo_wellarchitected.types.risk_counts

        out["RiskCounts"] = capo_wellarchitected.types.risk_counts.serialize_json(
            value["risk_counts"]
        )
    if "pillar_priorities" in value:
        import capo_wellarchitected.types.workload_pillar_priorities

        out["PillarPriorities"] = (
            capo_wellarchitected.types.workload_pillar_priorities.serialize_json(
                value["pillar_priorities"]
            )
        )
    if "lenses" in value:
        import capo_wellarchitected.types.workload_lenses

        out["Lenses"] = capo_wellarchitected.types.workload_lenses.serialize_json(
            value["lenses"]
        )
    if "owner" in value:
        out["Owner"] = value["owner"]
    if "share_invitation_id" in value:
        out["ShareInvitationId"] = value["share_invitation_id"]
    if "tags" in value:
        import capo_wellarchitected.types.tag_map

        out["Tags"] = capo_wellarchitected.types.tag_map.serialize_json(value["tags"])
    if "discovery_config" in value:
        import capo_wellarchitected.types.workload_discovery_config

        out["DiscoveryConfig"] = (
            capo_wellarchitected.types.workload_discovery_config.serialize_json(
                value["discovery_config"]
            )
        )
    if "applications" in value:
        import capo_wellarchitected.types.workload_applications

        out["Applications"] = (
            capo_wellarchitected.types.workload_applications.serialize_json(
                value["applications"]
            )
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
    if "jira_configuration" in value:
        import capo_wellarchitected.types.workload_jira_configuration_output

        out["JiraConfiguration"] = (
            capo_wellarchitected.types.workload_jira_configuration_output.serialize_json(
                value["jira_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> Workload:
    out: Workload = {}  # type: ignore[typeddict-item]
    if "WorkloadId" in data:
        out["workload_id"] = data["WorkloadId"]
    if "WorkloadArn" in data:
        out["workload_arn"] = data["WorkloadArn"]
    if "WorkloadName" in data:
        out["workload_name"] = data["WorkloadName"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Environment" in data:
        import capo_wellarchitected.types.workload_environment

        out["environment"] = (
            capo_wellarchitected.types.workload_environment.deserialize_json(
                data["Environment"]
            )
        )
    if "UpdatedAt" in data:
        import capo_wellarchitected.types.timestamp

        out["updated_at"] = capo_wellarchitected.types.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    if "AccountIds" in data:
        import capo_wellarchitected.types.workload_account_ids

        out["account_ids"] = (
            capo_wellarchitected.types.workload_account_ids.deserialize_json(
                data["AccountIds"]
            )
        )
    if "AwsRegions" in data:
        import capo_wellarchitected.types.workload_aws_regions

        out["aws_regions"] = (
            capo_wellarchitected.types.workload_aws_regions.deserialize_json(
                data["AwsRegions"]
            )
        )
    if "NonAwsRegions" in data:
        import capo_wellarchitected.types.workload_non_aws_regions

        out["non_aws_regions"] = (
            capo_wellarchitected.types.workload_non_aws_regions.deserialize_json(
                data["NonAwsRegions"]
            )
        )
    if "ArchitecturalDesign" in data:
        out["architectural_design"] = data["ArchitecturalDesign"]
    if "ReviewOwner" in data:
        out["review_owner"] = data["ReviewOwner"]
    if "ReviewRestrictionDate" in data:
        import capo_wellarchitected.types.timestamp

        out["review_restriction_date"] = (
            capo_wellarchitected.types.timestamp.deserialize_json(
                data["ReviewRestrictionDate"]
            )
        )
    if "IsReviewOwnerUpdateAcknowledged" in data:
        out["is_review_owner_update_acknowledged"] = data[
            "IsReviewOwnerUpdateAcknowledged"
        ]
    if "IndustryType" in data:
        out["industry_type"] = data["IndustryType"]
    if "Industry" in data:
        out["industry"] = data["Industry"]
    if "Notes" in data:
        out["notes"] = data["Notes"]
    if "ImprovementStatus" in data:
        import capo_wellarchitected.types.workload_improvement_status

        out["improvement_status"] = (
            capo_wellarchitected.types.workload_improvement_status.deserialize_json(
                data["ImprovementStatus"]
            )
        )
    if "RiskCounts" in data:
        import capo_wellarchitected.types.risk_counts

        out["risk_counts"] = capo_wellarchitected.types.risk_counts.deserialize_json(
            data["RiskCounts"]
        )
    if "PillarPriorities" in data:
        import capo_wellarchitected.types.workload_pillar_priorities

        out["pillar_priorities"] = (
            capo_wellarchitected.types.workload_pillar_priorities.deserialize_json(
                data["PillarPriorities"]
            )
        )
    if "Lenses" in data:
        import capo_wellarchitected.types.workload_lenses

        out["lenses"] = capo_wellarchitected.types.workload_lenses.deserialize_json(
            data["Lenses"]
        )
    if "Owner" in data:
        out["owner"] = data["Owner"]
    if "ShareInvitationId" in data:
        out["share_invitation_id"] = data["ShareInvitationId"]
    if "Tags" in data:
        import capo_wellarchitected.types.tag_map

        out["tags"] = capo_wellarchitected.types.tag_map.deserialize_json(data["Tags"])
    if "DiscoveryConfig" in data:
        import capo_wellarchitected.types.workload_discovery_config

        out["discovery_config"] = (
            capo_wellarchitected.types.workload_discovery_config.deserialize_json(
                data["DiscoveryConfig"]
            )
        )
    if "Applications" in data:
        import capo_wellarchitected.types.workload_applications

        out["applications"] = (
            capo_wellarchitected.types.workload_applications.deserialize_json(
                data["Applications"]
            )
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
    if "JiraConfiguration" in data:
        import capo_wellarchitected.types.workload_jira_configuration_output

        out["jira_configuration"] = (
            capo_wellarchitected.types.workload_jira_configuration_output.deserialize_json(
                data["JiraConfiguration"]
            )
        )
    return out
