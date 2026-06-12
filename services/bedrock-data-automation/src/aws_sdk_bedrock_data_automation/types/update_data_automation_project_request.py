"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#UpdateDataAutomationProjectRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.custom_output_configuration
    import aws_sdk_bedrock_data_automation.types.data_automation_library_configuration
    import aws_sdk_bedrock_data_automation.types.data_automation_project_arn
    import aws_sdk_bedrock_data_automation.types.data_automation_project_description
    import aws_sdk_bedrock_data_automation.types.data_automation_project_stage
    import aws_sdk_bedrock_data_automation.types.encryption_configuration
    import aws_sdk_bedrock_data_automation.types.override_configuration
    import aws_sdk_bedrock_data_automation.types.standard_output_configuration


class UpdateDataAutomationProjectRequest(TypedDict):
    project_arn: "aws_sdk_bedrock_data_automation.types.data_automation_project_arn.DataAutomationProjectArn"
    """ARN generated at the server side when a DataAutomationProject is created"""
    project_stage: NotRequired[
        "aws_sdk_bedrock_data_automation.types.data_automation_project_stage.DataAutomationProjectStage"
    ]
    project_description: NotRequired[
        "aws_sdk_bedrock_data_automation.types.data_automation_project_description.DataAutomationProjectDescription"
    ]
    standard_output_configuration: "aws_sdk_bedrock_data_automation.types.standard_output_configuration.StandardOutputConfiguration"
    custom_output_configuration: NotRequired[
        "aws_sdk_bedrock_data_automation.types.custom_output_configuration.CustomOutputConfiguration"
    ]
    override_configuration: NotRequired[
        "aws_sdk_bedrock_data_automation.types.override_configuration.OverrideConfiguration"
    ]
    data_automation_library_configuration: NotRequired[
        "aws_sdk_bedrock_data_automation.types.data_automation_library_configuration.DataAutomationLibraryConfiguration"
    ]
    encryption_configuration: NotRequired[
        "aws_sdk_bedrock_data_automation.types.encryption_configuration.EncryptionConfiguration"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataAutomationProjectRequest) -> dict:
    out: dict = {}
    if "project_stage" in value:
        import aws_sdk_bedrock_data_automation.types.data_automation_project_stage

        out["projectStage"] = (
            aws_sdk_bedrock_data_automation.types.data_automation_project_stage.serialize_json(
                value["project_stage"]
            )
        )
    if "project_description" in value:
        out["projectDescription"] = value["project_description"]
    import aws_sdk_bedrock_data_automation.types.standard_output_configuration

    out["standardOutputConfiguration"] = (
        aws_sdk_bedrock_data_automation.types.standard_output_configuration.serialize_json(
            value["standard_output_configuration"]
        )
    )
    if "custom_output_configuration" in value:
        import aws_sdk_bedrock_data_automation.types.custom_output_configuration

        out["customOutputConfiguration"] = (
            aws_sdk_bedrock_data_automation.types.custom_output_configuration.serialize_json(
                value["custom_output_configuration"]
            )
        )
    if "override_configuration" in value:
        import aws_sdk_bedrock_data_automation.types.override_configuration

        out["overrideConfiguration"] = (
            aws_sdk_bedrock_data_automation.types.override_configuration.serialize_json(
                value["override_configuration"]
            )
        )
    if "data_automation_library_configuration" in value:
        import aws_sdk_bedrock_data_automation.types.data_automation_library_configuration

        out["dataAutomationLibraryConfiguration"] = (
            aws_sdk_bedrock_data_automation.types.data_automation_library_configuration.serialize_json(
                value["data_automation_library_configuration"]
            )
        )
    if "encryption_configuration" in value:
        import aws_sdk_bedrock_data_automation.types.encryption_configuration

        out["encryptionConfiguration"] = (
            aws_sdk_bedrock_data_automation.types.encryption_configuration.serialize_json(
                value["encryption_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateDataAutomationProjectRequest:
    out: UpdateDataAutomationProjectRequest = {}  # type: ignore[typeddict-item]
    if "projectStage" in data:
        import aws_sdk_bedrock_data_automation.types.data_automation_project_stage

        out["project_stage"] = (
            aws_sdk_bedrock_data_automation.types.data_automation_project_stage.deserialize_json(
                data["projectStage"]
            )
        )
    if "projectDescription" in data:
        out["project_description"] = data["projectDescription"]
    if "standardOutputConfiguration" in data:
        import aws_sdk_bedrock_data_automation.types.standard_output_configuration

        out["standard_output_configuration"] = (
            aws_sdk_bedrock_data_automation.types.standard_output_configuration.deserialize_json(
                data["standardOutputConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateDataAutomationProjectRequest.standard_output_configuration required"
        )
    if "customOutputConfiguration" in data:
        import aws_sdk_bedrock_data_automation.types.custom_output_configuration

        out["custom_output_configuration"] = (
            aws_sdk_bedrock_data_automation.types.custom_output_configuration.deserialize_json(
                data["customOutputConfiguration"]
            )
        )
    if "overrideConfiguration" in data:
        import aws_sdk_bedrock_data_automation.types.override_configuration

        out["override_configuration"] = (
            aws_sdk_bedrock_data_automation.types.override_configuration.deserialize_json(
                data["overrideConfiguration"]
            )
        )
    if "dataAutomationLibraryConfiguration" in data:
        import aws_sdk_bedrock_data_automation.types.data_automation_library_configuration

        out["data_automation_library_configuration"] = (
            aws_sdk_bedrock_data_automation.types.data_automation_library_configuration.deserialize_json(
                data["dataAutomationLibraryConfiguration"]
            )
        )
    if "encryptionConfiguration" in data:
        import aws_sdk_bedrock_data_automation.types.encryption_configuration

        out["encryption_configuration"] = (
            aws_sdk_bedrock_data_automation.types.encryption_configuration.deserialize_json(
                data["encryptionConfiguration"]
            )
        )
    return out
