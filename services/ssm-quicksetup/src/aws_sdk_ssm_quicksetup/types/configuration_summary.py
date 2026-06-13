"""Generated from Smithy shape ``com.amazonaws.ssmquicksetup#ConfigurationSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_ssm_quicksetup.types.configuration_parameters_map
    import aws_sdk_ssm_quicksetup.types.status_summaries_list


class ConfigurationSummary(TypedDict):
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
    region: NotRequired["str"]
    """<p>The Amazon Web Services Region where the configuration was deployed.</p>"""
    account: NotRequired["str"]
    """<p>The ID of the Amazon Web Services account where the configuration was deployed.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The datetime stamp when the configuration was created.</p>"""
    first_class_parameters: NotRequired[
        "aws_sdk_ssm_quicksetup.types.configuration_parameters_map.ConfigurationParametersMap"
    ]
    """<p>The common parameters and values for the configuration definition.</p>"""
    status_summaries: NotRequired[
        "aws_sdk_ssm_quicksetup.types.status_summaries_list.StatusSummariesList"
    ]
    """<p>A summary of the state of the configuration manager. This includes deployment statuses, association statuses, drift statuses, health checks, and more.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationSummary) -> dict:
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
    if "region" in value:
        out["Region"] = value["region"]
    if "account" in value:
        out["Account"] = value["account"]
    if "created_at" in value:
        import aws_sdk_ssm_quicksetup.types._prelude.timestamp

        out["CreatedAt"] = (
            aws_sdk_ssm_quicksetup.types._prelude.timestamp.serialize_json(
                value["created_at"]
            )
        )
    if "first_class_parameters" in value:
        import aws_sdk_ssm_quicksetup.types.configuration_parameters_map

        out["FirstClassParameters"] = (
            aws_sdk_ssm_quicksetup.types.configuration_parameters_map.serialize_json(
                value["first_class_parameters"]
            )
        )
    if "status_summaries" in value:
        import aws_sdk_ssm_quicksetup.types.status_summaries_list

        out["StatusSummaries"] = (
            aws_sdk_ssm_quicksetup.types.status_summaries_list.serialize_json(
                value["status_summaries"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConfigurationSummary:
    out: ConfigurationSummary = {}  # type: ignore[typeddict-item]
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
    if "Region" in data:
        out["region"] = data["Region"]
    if "Account" in data:
        out["account"] = data["Account"]
    if "CreatedAt" in data:
        import aws_sdk_ssm_quicksetup.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_ssm_quicksetup.types._prelude.timestamp.deserialize_json(
                data["CreatedAt"]
            )
        )
    if "FirstClassParameters" in data:
        import aws_sdk_ssm_quicksetup.types.configuration_parameters_map

        out["first_class_parameters"] = (
            aws_sdk_ssm_quicksetup.types.configuration_parameters_map.deserialize_json(
                data["FirstClassParameters"]
            )
        )
    if "StatusSummaries" in data:
        import aws_sdk_ssm_quicksetup.types.status_summaries_list

        out["status_summaries"] = (
            aws_sdk_ssm_quicksetup.types.status_summaries_list.deserialize_json(
                data["StatusSummaries"]
            )
        )
    return out
