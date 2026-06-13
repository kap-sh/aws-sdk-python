"""Generated from Smithy shape ``com.amazonaws.ssmquicksetup#GetConfigurationManagerOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm_quicksetup.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_ssm_quicksetup.types.configuration_definitions_list
    import aws_sdk_ssm_quicksetup.types.status_summaries_list
    import aws_sdk_ssm_quicksetup.types.tags_map


class GetConfigurationManagerOutput(TypedDict):
    manager_arn: "str"
    """<p>The ARN of the configuration manager.</p>"""
    description: NotRequired["str"]
    """<p>The description of the configuration manager.</p>"""
    name: NotRequired["str"]
    """<p>The name of the configuration manager.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The datetime stamp when the configuration manager was created.</p>"""
    last_modified_at: NotRequired["datetime.datetime"]
    """<p>The datetime stamp when the configuration manager was last updated.</p>"""
    status_summaries: NotRequired[
        "aws_sdk_ssm_quicksetup.types.status_summaries_list.StatusSummariesList"
    ]
    """<p>A summary of the state of the configuration manager. This includes deployment statuses, association statuses, drift statuses, health checks, and more.</p>"""
    configuration_definitions: NotRequired[
        "aws_sdk_ssm_quicksetup.types.configuration_definitions_list.ConfigurationDefinitionsList"
    ]
    """<p>The configuration definitions association with the configuration manager.</p>"""
    tags: NotRequired["aws_sdk_ssm_quicksetup.types.tags_map.TagsMap"]
    """<p>Key-value pairs of metadata to assign to the configuration manager.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConfigurationManagerOutput) -> dict:
    out: dict = {}
    out["ManagerArn"] = value["manager_arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "name" in value:
        out["Name"] = value["name"]
    if "created_at" in value:
        import aws_sdk_ssm_quicksetup.types._prelude.timestamp

        out["CreatedAt"] = (
            aws_sdk_ssm_quicksetup.types._prelude.timestamp.serialize_json(
                value["created_at"]
            )
        )
    if "last_modified_at" in value:
        import aws_sdk_ssm_quicksetup.types._prelude.timestamp

        out["LastModifiedAt"] = (
            aws_sdk_ssm_quicksetup.types._prelude.timestamp.serialize_json(
                value["last_modified_at"]
            )
        )
    if "status_summaries" in value:
        import aws_sdk_ssm_quicksetup.types.status_summaries_list

        out["StatusSummaries"] = (
            aws_sdk_ssm_quicksetup.types.status_summaries_list.serialize_json(
                value["status_summaries"]
            )
        )
    if "configuration_definitions" in value:
        import aws_sdk_ssm_quicksetup.types.configuration_definitions_list

        out["ConfigurationDefinitions"] = (
            aws_sdk_ssm_quicksetup.types.configuration_definitions_list.serialize_json(
                value["configuration_definitions"]
            )
        )
    if "tags" in value:
        import aws_sdk_ssm_quicksetup.types.tags_map

        out["Tags"] = aws_sdk_ssm_quicksetup.types.tags_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> GetConfigurationManagerOutput:
    out: GetConfigurationManagerOutput = {}  # type: ignore[typeddict-item]
    if "ManagerArn" in data:
        out["manager_arn"] = data["ManagerArn"]
    else:
        raise DeserializationError("GetConfigurationManagerOutput.manager_arn required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "CreatedAt" in data:
        import aws_sdk_ssm_quicksetup.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_ssm_quicksetup.types._prelude.timestamp.deserialize_json(
                data["CreatedAt"]
            )
        )
    if "LastModifiedAt" in data:
        import aws_sdk_ssm_quicksetup.types._prelude.timestamp

        out["last_modified_at"] = (
            aws_sdk_ssm_quicksetup.types._prelude.timestamp.deserialize_json(
                data["LastModifiedAt"]
            )
        )
    if "StatusSummaries" in data:
        import aws_sdk_ssm_quicksetup.types.status_summaries_list

        out["status_summaries"] = (
            aws_sdk_ssm_quicksetup.types.status_summaries_list.deserialize_json(
                data["StatusSummaries"]
            )
        )
    if "ConfigurationDefinitions" in data:
        import aws_sdk_ssm_quicksetup.types.configuration_definitions_list

        out["configuration_definitions"] = (
            aws_sdk_ssm_quicksetup.types.configuration_definitions_list.deserialize_json(
                data["ConfigurationDefinitions"]
            )
        )
    if "Tags" in data:
        import aws_sdk_ssm_quicksetup.types.tags_map

        out["tags"] = aws_sdk_ssm_quicksetup.types.tags_map.deserialize_json(
            data["Tags"]
        )
    return out
