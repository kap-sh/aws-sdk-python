"""Generated from Smithy shape ``com.amazonaws.ssmquicksetup#GetConfigurationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_ssm_quicksetup.types.configuration_parameters_map
    import capo_ssm_quicksetup.types.status_summaries_list


class GetConfigurationOutput(TypedDict, closed=True):
    id: NotRequired["str"]
    """<p>A service generated identifier for the configuration.</p>"""
    manager_arn: NotRequired["str"]
    """<p>The ARN of the configuration manager.</p>"""
    configuration_definition_id: NotRequired["str"]
    """<p>The ID of the configuration definition.</p>"""
    type: NotRequired["str"]
    """<p>The type of the Quick Setup configuration.</p>"""
    type_version: NotRequired["str"]
    """<p>The version of the Quick Setup type used.</p>"""
    account: NotRequired["str"]
    """<p>The ID of the Amazon Web Services account where the configuration was deployed.</p>"""
    region: NotRequired["str"]
    """<p>The Amazon Web Services Region where the configuration was deployed.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The datetime stamp when the configuration manager was created.</p>"""
    last_modified_at: NotRequired["datetime.datetime"]
    """<p>The datetime stamp when the configuration manager was last updated.</p>"""
    status_summaries: NotRequired[
        "capo_ssm_quicksetup.types.status_summaries_list.StatusSummariesList"
    ]
    """<p>A summary of the state of the configuration manager. This includes deployment statuses, association statuses, drift statuses, health checks, and more.</p>"""
    parameters: NotRequired[
        "capo_ssm_quicksetup.types.configuration_parameters_map.ConfigurationParametersMap"
    ]
    """<p>The parameters for the configuration definition type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConfigurationOutput) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "manager_arn" in value:
        out["ManagerArn"] = value["manager_arn"]
    if "configuration_definition_id" in value:
        out["ConfigurationDefinitionId"] = value["configuration_definition_id"]
    if "type" in value:
        out["Type"] = value["type"]
    if "type_version" in value:
        out["TypeVersion"] = value["type_version"]
    if "account" in value:
        out["Account"] = value["account"]
    if "region" in value:
        out["Region"] = value["region"]
    if "created_at" in value:
        import capo_ssm_quicksetup.types._prelude.timestamp

        out["CreatedAt"] = capo_ssm_quicksetup.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "last_modified_at" in value:
        import capo_ssm_quicksetup.types._prelude.timestamp

        out["LastModifiedAt"] = (
            capo_ssm_quicksetup.types._prelude.timestamp.serialize_json(
                value["last_modified_at"]
            )
        )
    if "status_summaries" in value:
        import capo_ssm_quicksetup.types.status_summaries_list

        out["StatusSummaries"] = (
            capo_ssm_quicksetup.types.status_summaries_list.serialize_json(
                value["status_summaries"]
            )
        )
    if "parameters" in value:
        import capo_ssm_quicksetup.types.configuration_parameters_map

        out["Parameters"] = (
            capo_ssm_quicksetup.types.configuration_parameters_map.serialize_json(
                value["parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetConfigurationOutput:
    out: GetConfigurationOutput = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "ManagerArn" in data:
        out["manager_arn"] = data["ManagerArn"]
    if "ConfigurationDefinitionId" in data:
        out["configuration_definition_id"] = data["ConfigurationDefinitionId"]
    if "Type" in data:
        out["type"] = data["Type"]
    if "TypeVersion" in data:
        out["type_version"] = data["TypeVersion"]
    if "Account" in data:
        out["account"] = data["Account"]
    if "Region" in data:
        out["region"] = data["Region"]
    if "CreatedAt" in data:
        import capo_ssm_quicksetup.types._prelude.timestamp

        out["created_at"] = (
            capo_ssm_quicksetup.types._prelude.timestamp.deserialize_json(
                data["CreatedAt"]
            )
        )
    if "LastModifiedAt" in data:
        import capo_ssm_quicksetup.types._prelude.timestamp

        out["last_modified_at"] = (
            capo_ssm_quicksetup.types._prelude.timestamp.deserialize_json(
                data["LastModifiedAt"]
            )
        )
    if "StatusSummaries" in data:
        import capo_ssm_quicksetup.types.status_summaries_list

        out["status_summaries"] = (
            capo_ssm_quicksetup.types.status_summaries_list.deserialize_json(
                data["StatusSummaries"]
            )
        )
    if "Parameters" in data:
        import capo_ssm_quicksetup.types.configuration_parameters_map

        out["parameters"] = (
            capo_ssm_quicksetup.types.configuration_parameters_map.deserialize_json(
                data["Parameters"]
            )
        )
    return out
