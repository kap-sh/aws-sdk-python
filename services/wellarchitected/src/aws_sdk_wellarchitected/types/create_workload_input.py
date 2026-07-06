"""Generated from Smithy shape ``com.amazonaws.wellarchitected#CreateWorkloadInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.client_request_token
    import aws_sdk_wellarchitected.types.notes
    import aws_sdk_wellarchitected.types.review_template_arns
    import aws_sdk_wellarchitected.types.tag_map
    import aws_sdk_wellarchitected.types.workload_account_ids
    import aws_sdk_wellarchitected.types.workload_applications
    import aws_sdk_wellarchitected.types.workload_architectural_design
    import aws_sdk_wellarchitected.types.workload_aws_regions
    import aws_sdk_wellarchitected.types.workload_description
    import aws_sdk_wellarchitected.types.workload_discovery_config
    import aws_sdk_wellarchitected.types.workload_environment
    import aws_sdk_wellarchitected.types.workload_industry
    import aws_sdk_wellarchitected.types.workload_industry_type
    import aws_sdk_wellarchitected.types.workload_jira_configuration_input
    import aws_sdk_wellarchitected.types.workload_lenses
    import aws_sdk_wellarchitected.types.workload_name
    import aws_sdk_wellarchitected.types.workload_non_aws_regions
    import aws_sdk_wellarchitected.types.workload_pillar_priorities
    import aws_sdk_wellarchitected.types.workload_profile_arns
    import aws_sdk_wellarchitected.types.workload_review_owner


class CreateWorkloadInput(TypedDict, closed=True):
    workload_name: NotRequired[
        "aws_sdk_wellarchitected.types.workload_name.WorkloadName"
    ]
    description: NotRequired[
        "aws_sdk_wellarchitected.types.workload_description.WorkloadDescription"
    ]
    environment: NotRequired[
        "aws_sdk_wellarchitected.types.workload_environment.WorkloadEnvironment"
    ]
    account_ids: NotRequired[
        "aws_sdk_wellarchitected.types.workload_account_ids.WorkloadAccountIds"
    ]
    aws_regions: NotRequired[
        "aws_sdk_wellarchitected.types.workload_aws_regions.WorkloadAwsRegions"
    ]
    non_aws_regions: NotRequired[
        "aws_sdk_wellarchitected.types.workload_non_aws_regions.WorkloadNonAwsRegions"
    ]
    pillar_priorities: NotRequired[
        "aws_sdk_wellarchitected.types.workload_pillar_priorities.WorkloadPillarPriorities"
    ]
    architectural_design: NotRequired[
        "aws_sdk_wellarchitected.types.workload_architectural_design.WorkloadArchitecturalDesign"
    ]
    review_owner: NotRequired[
        "aws_sdk_wellarchitected.types.workload_review_owner.WorkloadReviewOwner"
    ]
    industry_type: NotRequired[
        "aws_sdk_wellarchitected.types.workload_industry_type.WorkloadIndustryType"
    ]
    industry: NotRequired[
        "aws_sdk_wellarchitected.types.workload_industry.WorkloadIndustry"
    ]
    lenses: NotRequired["aws_sdk_wellarchitected.types.workload_lenses.WorkloadLenses"]
    notes: NotRequired["aws_sdk_wellarchitected.types.notes.Notes"]
    client_request_token: NotRequired[
        "aws_sdk_wellarchitected.types.client_request_token.ClientRequestToken"
    ]
    tags: NotRequired["aws_sdk_wellarchitected.types.tag_map.TagMap"]
    """<p>The tags to be associated with the workload.</p>"""
    discovery_config: NotRequired[
        "aws_sdk_wellarchitected.types.workload_discovery_config.WorkloadDiscoveryConfig"
    ]
    """<p>Well-Architected discovery configuration settings associated to the workload.</p>"""
    applications: NotRequired[
        "aws_sdk_wellarchitected.types.workload_applications.WorkloadApplications"
    ]
    """<p>List of AppRegistry application ARNs associated to the workload.</p>"""
    profile_arns: NotRequired[
        "aws_sdk_wellarchitected.types.workload_profile_arns.WorkloadProfileArns"
    ]
    """<p>The list of profile ARNs associated with the workload.</p>"""
    review_template_arns: NotRequired[
        "aws_sdk_wellarchitected.types.review_template_arns.ReviewTemplateArns"
    ]
    """<p>The list of review template ARNs to associate with the workload.</p>"""
    jira_configuration: NotRequired[
        "aws_sdk_wellarchitected.types.workload_jira_configuration_input.WorkloadJiraConfigurationInput"
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
        import aws_sdk_wellarchitected.types.workload_environment

        out["Environment"] = (
            aws_sdk_wellarchitected.types.workload_environment.serialize_json(
                value["environment"]
            )
        )
    if "account_ids" in value:
        import aws_sdk_wellarchitected.types.workload_account_ids

        out["AccountIds"] = (
            aws_sdk_wellarchitected.types.workload_account_ids.serialize_json(
                value["account_ids"]
            )
        )
    if "aws_regions" in value:
        import aws_sdk_wellarchitected.types.workload_aws_regions

        out["AwsRegions"] = (
            aws_sdk_wellarchitected.types.workload_aws_regions.serialize_json(
                value["aws_regions"]
            )
        )
    if "non_aws_regions" in value:
        import aws_sdk_wellarchitected.types.workload_non_aws_regions

        out["NonAwsRegions"] = (
            aws_sdk_wellarchitected.types.workload_non_aws_regions.serialize_json(
                value["non_aws_regions"]
            )
        )
    if "pillar_priorities" in value:
        import aws_sdk_wellarchitected.types.workload_pillar_priorities

        out["PillarPriorities"] = (
            aws_sdk_wellarchitected.types.workload_pillar_priorities.serialize_json(
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
        import aws_sdk_wellarchitected.types.workload_lenses

        out["Lenses"] = aws_sdk_wellarchitected.types.workload_lenses.serialize_json(
            value["lenses"]
        )
    if "notes" in value:
        out["Notes"] = value["notes"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "tags" in value:
        import aws_sdk_wellarchitected.types.tag_map

        out["Tags"] = aws_sdk_wellarchitected.types.tag_map.serialize_json(
            value["tags"]
        )
    if "discovery_config" in value:
        import aws_sdk_wellarchitected.types.workload_discovery_config

        out["DiscoveryConfig"] = (
            aws_sdk_wellarchitected.types.workload_discovery_config.serialize_json(
                value["discovery_config"]
            )
        )
    if "applications" in value:
        import aws_sdk_wellarchitected.types.workload_applications

        out["Applications"] = (
            aws_sdk_wellarchitected.types.workload_applications.serialize_json(
                value["applications"]
            )
        )
    if "profile_arns" in value:
        import aws_sdk_wellarchitected.types.workload_profile_arns

        out["ProfileArns"] = (
            aws_sdk_wellarchitected.types.workload_profile_arns.serialize_json(
                value["profile_arns"]
            )
        )
    if "review_template_arns" in value:
        import aws_sdk_wellarchitected.types.review_template_arns

        out["ReviewTemplateArns"] = (
            aws_sdk_wellarchitected.types.review_template_arns.serialize_json(
                value["review_template_arns"]
            )
        )
    if "jira_configuration" in value:
        import aws_sdk_wellarchitected.types.workload_jira_configuration_input

        out["JiraConfiguration"] = (
            aws_sdk_wellarchitected.types.workload_jira_configuration_input.serialize_json(
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
        import aws_sdk_wellarchitected.types.workload_environment

        out["environment"] = (
            aws_sdk_wellarchitected.types.workload_environment.deserialize_json(
                data["Environment"]
            )
        )
    if "AccountIds" in data:
        import aws_sdk_wellarchitected.types.workload_account_ids

        out["account_ids"] = (
            aws_sdk_wellarchitected.types.workload_account_ids.deserialize_json(
                data["AccountIds"]
            )
        )
    if "AwsRegions" in data:
        import aws_sdk_wellarchitected.types.workload_aws_regions

        out["aws_regions"] = (
            aws_sdk_wellarchitected.types.workload_aws_regions.deserialize_json(
                data["AwsRegions"]
            )
        )
    if "NonAwsRegions" in data:
        import aws_sdk_wellarchitected.types.workload_non_aws_regions

        out["non_aws_regions"] = (
            aws_sdk_wellarchitected.types.workload_non_aws_regions.deserialize_json(
                data["NonAwsRegions"]
            )
        )
    if "PillarPriorities" in data:
        import aws_sdk_wellarchitected.types.workload_pillar_priorities

        out["pillar_priorities"] = (
            aws_sdk_wellarchitected.types.workload_pillar_priorities.deserialize_json(
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
        import aws_sdk_wellarchitected.types.workload_lenses

        out["lenses"] = aws_sdk_wellarchitected.types.workload_lenses.deserialize_json(
            data["Lenses"]
        )
    if "Notes" in data:
        out["notes"] = data["Notes"]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    if "Tags" in data:
        import aws_sdk_wellarchitected.types.tag_map

        out["tags"] = aws_sdk_wellarchitected.types.tag_map.deserialize_json(
            data["Tags"]
        )
    if "DiscoveryConfig" in data:
        import aws_sdk_wellarchitected.types.workload_discovery_config

        out["discovery_config"] = (
            aws_sdk_wellarchitected.types.workload_discovery_config.deserialize_json(
                data["DiscoveryConfig"]
            )
        )
    if "Applications" in data:
        import aws_sdk_wellarchitected.types.workload_applications

        out["applications"] = (
            aws_sdk_wellarchitected.types.workload_applications.deserialize_json(
                data["Applications"]
            )
        )
    if "ProfileArns" in data:
        import aws_sdk_wellarchitected.types.workload_profile_arns

        out["profile_arns"] = (
            aws_sdk_wellarchitected.types.workload_profile_arns.deserialize_json(
                data["ProfileArns"]
            )
        )
    if "ReviewTemplateArns" in data:
        import aws_sdk_wellarchitected.types.review_template_arns

        out["review_template_arns"] = (
            aws_sdk_wellarchitected.types.review_template_arns.deserialize_json(
                data["ReviewTemplateArns"]
            )
        )
    if "JiraConfiguration" in data:
        import aws_sdk_wellarchitected.types.workload_jira_configuration_input

        out["jira_configuration"] = (
            aws_sdk_wellarchitected.types.workload_jira_configuration_input.deserialize_json(
                data["JiraConfiguration"]
            )
        )
    return out
