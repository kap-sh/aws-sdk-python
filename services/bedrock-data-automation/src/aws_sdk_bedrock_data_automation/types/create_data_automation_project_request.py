"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#CreateDataAutomationProjectRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.client_token
    import aws_sdk_bedrock_data_automation.types.custom_output_configuration
    import aws_sdk_bedrock_data_automation.types.data_automation_library_configuration
    import aws_sdk_bedrock_data_automation.types.data_automation_project_description
    import aws_sdk_bedrock_data_automation.types.data_automation_project_name
    import aws_sdk_bedrock_data_automation.types.data_automation_project_stage
    import aws_sdk_bedrock_data_automation.types.data_automation_project_type
    import aws_sdk_bedrock_data_automation.types.encryption_configuration
    import aws_sdk_bedrock_data_automation.types.override_configuration
    import aws_sdk_bedrock_data_automation.types.standard_output_configuration
    import aws_sdk_bedrock_data_automation.types.tag_list


class CreateDataAutomationProjectRequest(TypedDict, closed=True):
    project_name: "aws_sdk_bedrock_data_automation.types.data_automation_project_name.DataAutomationProjectName"
    project_description: NotRequired[
        "aws_sdk_bedrock_data_automation.types.data_automation_project_description.DataAutomationProjectDescription"
    ]
    project_stage: NotRequired[
        "aws_sdk_bedrock_data_automation.types.data_automation_project_stage.DataAutomationProjectStage"
    ]
    project_type: "aws_sdk_bedrock_data_automation.types.data_automation_project_type.DataAutomationProjectType"
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
    client_token: NotRequired[
        "aws_sdk_bedrock_data_automation.types.client_token.ClientToken"
    ]
    encryption_configuration: NotRequired[
        "aws_sdk_bedrock_data_automation.types.encryption_configuration.EncryptionConfiguration"
    ]
    tags: NotRequired["aws_sdk_bedrock_data_automation.types.tag_list.TagList"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataAutomationProjectRequest) -> dict:
    out: dict = {}
    out["projectName"] = value["project_name"]
    if "project_description" in value:
        out["projectDescription"] = value["project_description"]
    if "project_stage" in value:
        import aws_sdk_bedrock_data_automation.types.data_automation_project_stage

        out["projectStage"] = (
            aws_sdk_bedrock_data_automation.types.data_automation_project_stage.serialize_json(
                value["project_stage"]
            )
        )
    import aws_sdk_bedrock_data_automation.types.data_automation_project_type

    out["projectType"] = (
        aws_sdk_bedrock_data_automation.types.data_automation_project_type.serialize_json(
            value.get("project_type", "ASYNC")
        )
    )
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
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "encryption_configuration" in value:
        import aws_sdk_bedrock_data_automation.types.encryption_configuration

        out["encryptionConfiguration"] = (
            aws_sdk_bedrock_data_automation.types.encryption_configuration.serialize_json(
                value["encryption_configuration"]
            )
        )
    if "tags" in value:
        import aws_sdk_bedrock_data_automation.types.tag_list

        out["tags"] = aws_sdk_bedrock_data_automation.types.tag_list.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateDataAutomationProjectRequest:
    out: CreateDataAutomationProjectRequest = {}  # type: ignore[typeddict-item]
    if "projectName" in data:
        out["project_name"] = data["projectName"]
    else:
        raise DeserializationError(
            "CreateDataAutomationProjectRequest.project_name required"
        )
    if "projectDescription" in data:
        out["project_description"] = data["projectDescription"]
    if "projectStage" in data:
        import aws_sdk_bedrock_data_automation.types.data_automation_project_stage

        out["project_stage"] = (
            aws_sdk_bedrock_data_automation.types.data_automation_project_stage.deserialize_json(
                data["projectStage"]
            )
        )
    if "projectType" in data:
        import aws_sdk_bedrock_data_automation.types.data_automation_project_type

        out["project_type"] = (
            aws_sdk_bedrock_data_automation.types.data_automation_project_type.deserialize_json(
                data["projectType"]
            )
        )
    else:
        out["project_type"] = "ASYNC"
    if "standardOutputConfiguration" in data:
        import aws_sdk_bedrock_data_automation.types.standard_output_configuration

        out["standard_output_configuration"] = (
            aws_sdk_bedrock_data_automation.types.standard_output_configuration.deserialize_json(
                data["standardOutputConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateDataAutomationProjectRequest.standard_output_configuration required"
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
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "encryptionConfiguration" in data:
        import aws_sdk_bedrock_data_automation.types.encryption_configuration

        out["encryption_configuration"] = (
            aws_sdk_bedrock_data_automation.types.encryption_configuration.deserialize_json(
                data["encryptionConfiguration"]
            )
        )
    if "tags" in data:
        import aws_sdk_bedrock_data_automation.types.tag_list

        out["tags"] = aws_sdk_bedrock_data_automation.types.tag_list.deserialize_json(
            data["tags"]
        )
    return out
