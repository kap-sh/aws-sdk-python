"""Generated from Smithy shape ``com.amazonaws.ssmquicksetup#ConfigurationManagerSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm_quicksetup.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm_quicksetup.types.configuration_definition_summaries_list
    import capo_ssm_quicksetup.types.status_summaries_list


class ConfigurationManagerSummary(TypedDict, closed=True):
    manager_arn: "str"
    """<p>The ARN of the Quick Setup configuration.</p>"""
    description: NotRequired["str"]
    """<p>The description of the configuration.</p>"""
    name: NotRequired["str"]
    """<p>The name of the configuration</p>"""
    status_summaries: NotRequired[
        "capo_ssm_quicksetup.types.status_summaries_list.StatusSummariesList"
    ]
    """<p>Summaries of the state of the configuration manager. These summaries include an aggregate of the statuses from the configuration definition associated with the configuration manager. This includes deployment statuses, association statuses, drift statuses, health checks, and more.</p>"""
    configuration_definition_summaries: NotRequired[
        "capo_ssm_quicksetup.types.configuration_definition_summaries_list.ConfigurationDefinitionSummariesList"
    ]
    """<p>A summary of the Quick Setup configuration definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationManagerSummary) -> dict:
    out: dict = {}
    out["ManagerArn"] = value["manager_arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "name" in value:
        out["Name"] = value["name"]
    if "status_summaries" in value:
        import capo_ssm_quicksetup.types.status_summaries_list

        out["StatusSummaries"] = (
            capo_ssm_quicksetup.types.status_summaries_list.serialize_json(
                value["status_summaries"]
            )
        )
    if "configuration_definition_summaries" in value:
        import capo_ssm_quicksetup.types.configuration_definition_summaries_list

        out["ConfigurationDefinitionSummaries"] = (
            capo_ssm_quicksetup.types.configuration_definition_summaries_list.serialize_json(
                value["configuration_definition_summaries"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConfigurationManagerSummary:
    out: ConfigurationManagerSummary = {}  # type: ignore[typeddict-item]
    if "ManagerArn" in data:
        out["manager_arn"] = data["ManagerArn"]
    else:
        raise DeserializationError("ConfigurationManagerSummary.manager_arn required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "StatusSummaries" in data:
        import capo_ssm_quicksetup.types.status_summaries_list

        out["status_summaries"] = (
            capo_ssm_quicksetup.types.status_summaries_list.deserialize_json(
                data["StatusSummaries"]
            )
        )
    if "ConfigurationDefinitionSummaries" in data:
        import capo_ssm_quicksetup.types.configuration_definition_summaries_list

        out["configuration_definition_summaries"] = (
            capo_ssm_quicksetup.types.configuration_definition_summaries_list.deserialize_json(
                data["ConfigurationDefinitionSummaries"]
            )
        )
    return out
