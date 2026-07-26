"""Generated from Smithy shape ``com.amazonaws.wellarchitected#UpdateWorkloadInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.is_review_owner_update_acknowledged
    import capo_wellarchitected.types.notes
    import capo_wellarchitected.types.workload_account_ids
    import capo_wellarchitected.types.workload_applications
    import capo_wellarchitected.types.workload_architectural_design
    import capo_wellarchitected.types.workload_aws_regions
    import capo_wellarchitected.types.workload_description
    import capo_wellarchitected.types.workload_discovery_config
    import capo_wellarchitected.types.workload_environment
    import capo_wellarchitected.types.workload_id
    import capo_wellarchitected.types.workload_improvement_status
    import capo_wellarchitected.types.workload_industry
    import capo_wellarchitected.types.workload_industry_type
    import capo_wellarchitected.types.workload_jira_configuration_input
    import capo_wellarchitected.types.workload_name
    import capo_wellarchitected.types.workload_non_aws_regions
    import capo_wellarchitected.types.workload_pillar_priorities
    import capo_wellarchitected.types.workload_review_owner


class UpdateWorkloadInput(TypedDict, closed=True):
    workload_id: "capo_wellarchitected.types.workload_id.WorkloadId"
    workload_name: NotRequired["capo_wellarchitected.types.workload_name.WorkloadName"]
    description: NotRequired[
        "capo_wellarchitected.types.workload_description.WorkloadDescription"
    ]
    environment: NotRequired[
        "capo_wellarchitected.types.workload_environment.WorkloadEnvironment"
    ]
    account_ids: NotRequired[
        "capo_wellarchitected.types.workload_account_ids.WorkloadAccountIds"
    ]
    aws_regions: NotRequired[
        "capo_wellarchitected.types.workload_aws_regions.WorkloadAwsRegions"
    ]
    non_aws_regions: NotRequired[
        "capo_wellarchitected.types.workload_non_aws_regions.WorkloadNonAwsRegions"
    ]
    pillar_priorities: NotRequired[
        "capo_wellarchitected.types.workload_pillar_priorities.WorkloadPillarPriorities"
    ]
    architectural_design: NotRequired[
        "capo_wellarchitected.types.workload_architectural_design.WorkloadArchitecturalDesign"
    ]
    review_owner: NotRequired[
        "capo_wellarchitected.types.workload_review_owner.WorkloadReviewOwner"
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
    discovery_config: NotRequired[
        "capo_wellarchitected.types.workload_discovery_config.WorkloadDiscoveryConfig"
    ]
    """<p>Well-Architected discovery configuration settings to associate to the workload.</p>"""
    applications: NotRequired[
        "capo_wellarchitected.types.workload_applications.WorkloadApplications"
    ]
    """<p>List of AppRegistry application ARNs to associate to the workload.</p>"""
    jira_configuration: NotRequired[
        "capo_wellarchitected.types.workload_jira_configuration_input.WorkloadJiraConfigurationInput"
    ]
    """<p>Configuration of the Jira integration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWorkloadInput) -> dict:
    out: dict = {}
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
    if "pillar_priorities" in value:
        import capo_wellarchitected.types.workload_pillar_priorities

        out["PillarPriorities"] = (
            capo_wellarchitected.types.workload_pillar_priorities.serialize_json(
                value["pillar_priorities"]
            )
        )
    if "architectural_design" in value:
        out["ArchitecturalDesign"] = value["architectural_design"]
    if "review_owner" in value:
        out["ReviewOwner"] = value["review_owner"]
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
    if "jira_configuration" in value:
        import capo_wellarchitected.types.workload_jira_configuration_input

        out["JiraConfiguration"] = (
            capo_wellarchitected.types.workload_jira_configuration_input.serialize_json(
                value["jira_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateWorkloadInput:
    out: UpdateWorkloadInput = {}  # type: ignore[typeddict-item]
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
    if "PillarPriorities" in data:
        import capo_wellarchitected.types.workload_pillar_priorities

        out["pillar_priorities"] = (
            capo_wellarchitected.types.workload_pillar_priorities.deserialize_json(
                data["PillarPriorities"]
            )
        )
    if "ArchitecturalDesign" in data:
        out["architectural_design"] = data["ArchitecturalDesign"]
    if "ReviewOwner" in data:
        out["review_owner"] = data["ReviewOwner"]
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
    if "JiraConfiguration" in data:
        import capo_wellarchitected.types.workload_jira_configuration_input

        out["jira_configuration"] = (
            capo_wellarchitected.types.workload_jira_configuration_input.deserialize_json(
                data["JiraConfiguration"]
            )
        )
    return out
