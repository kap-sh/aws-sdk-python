"""Generated from Smithy shape ``com.amazonaws.wellarchitected#CreateWorkloadInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.client_request_token
    import capo_wellarchitected.types.notes
    import capo_wellarchitected.types.review_template_arns
    import capo_wellarchitected.types.tag_map
    import capo_wellarchitected.types.workload_account_ids
    import capo_wellarchitected.types.workload_applications
    import capo_wellarchitected.types.workload_architectural_design
    import capo_wellarchitected.types.workload_aws_regions
    import capo_wellarchitected.types.workload_description
    import capo_wellarchitected.types.workload_discovery_config
    import capo_wellarchitected.types.workload_environment
    import capo_wellarchitected.types.workload_industry
    import capo_wellarchitected.types.workload_industry_type
    import capo_wellarchitected.types.workload_jira_configuration_input
    import capo_wellarchitected.types.workload_lenses
    import capo_wellarchitected.types.workload_name
    import capo_wellarchitected.types.workload_non_aws_regions
    import capo_wellarchitected.types.workload_pillar_priorities
    import capo_wellarchitected.types.workload_profile_arns
    import capo_wellarchitected.types.workload_review_owner


class CreateWorkloadInput(TypedDict, closed=True):
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
    industry_type: NotRequired[
        "capo_wellarchitected.types.workload_industry_type.WorkloadIndustryType"
    ]
    industry: NotRequired[
        "capo_wellarchitected.types.workload_industry.WorkloadIndustry"
    ]
    lenses: NotRequired["capo_wellarchitected.types.workload_lenses.WorkloadLenses"]
    notes: NotRequired["capo_wellarchitected.types.notes.Notes"]
    client_request_token: NotRequired[
        "capo_wellarchitected.types.client_request_token.ClientRequestToken"
    ]
    tags: NotRequired["capo_wellarchitected.types.tag_map.TagMap"]
    """<p>The tags to be associated with the workload.</p>"""
    discovery_config: NotRequired[
        "capo_wellarchitected.types.workload_discovery_config.WorkloadDiscoveryConfig"
    ]
    """<p>Well-Architected discovery configuration settings associated to the workload.</p>"""
    applications: NotRequired[
        "capo_wellarchitected.types.workload_applications.WorkloadApplications"
    ]
    """<p>List of AppRegistry application ARNs associated to the workload.</p>"""
    profile_arns: NotRequired[
        "capo_wellarchitected.types.workload_profile_arns.WorkloadProfileArns"
    ]
    """<p>The list of profile ARNs associated with the workload.</p>"""
    review_template_arns: NotRequired[
        "capo_wellarchitected.types.review_template_arns.ReviewTemplateArns"
    ]
    """<p>The list of review template ARNs to associate with the workload.</p>"""
    jira_configuration: NotRequired[
        "capo_wellarchitected.types.workload_jira_configuration_input.WorkloadJiraConfigurationInput"
    ]
    """<p>Jira configuration settings when creating a workload.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkloadInput) -> dict:
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
    if "industry_type" in value:
        out["IndustryType"] = value["industry_type"]
    if "industry" in value:
        out["Industry"] = value["industry"]
    if "lenses" in value:
        import capo_wellarchitected.types.workload_lenses

        out["Lenses"] = capo_wellarchitected.types.workload_lenses.serialize_json(
            value["lenses"]
        )
    if "notes" in value:
        out["Notes"] = value["notes"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
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
    if "profile_arns" in value:
        import capo_wellarchitected.types.workload_profile_arns

        out["ProfileArns"] = (
            capo_wellarchitected.types.workload_profile_arns.serialize_json(
                value["profile_arns"]
            )
        )
    if "review_template_arns" in value:
        import capo_wellarchitected.types.review_template_arns

        out["ReviewTemplateArns"] = (
            capo_wellarchitected.types.review_template_arns.serialize_json(
                value["review_template_arns"]
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


def deserialize_json(data: dict) -> CreateWorkloadInput:
    out: CreateWorkloadInput = {}  # type: ignore[typeddict-item]
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
    if "IndustryType" in data:
        out["industry_type"] = data["IndustryType"]
    if "Industry" in data:
        out["industry"] = data["Industry"]
    if "Lenses" in data:
        import capo_wellarchitected.types.workload_lenses

        out["lenses"] = capo_wellarchitected.types.workload_lenses.deserialize_json(
            data["Lenses"]
        )
    if "Notes" in data:
        out["notes"] = data["Notes"]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
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
    if "ProfileArns" in data:
        import capo_wellarchitected.types.workload_profile_arns

        out["profile_arns"] = (
            capo_wellarchitected.types.workload_profile_arns.deserialize_json(
                data["ProfileArns"]
            )
        )
    if "ReviewTemplateArns" in data:
        import capo_wellarchitected.types.review_template_arns

        out["review_template_arns"] = (
            capo_wellarchitected.types.review_template_arns.deserialize_json(
                data["ReviewTemplateArns"]
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
