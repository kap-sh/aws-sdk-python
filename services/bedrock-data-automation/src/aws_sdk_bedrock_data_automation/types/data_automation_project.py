"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DataAutomationProject``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.custom_output_configuration
    import aws_sdk_bedrock_data_automation.types.data_automation_library_configuration
    import aws_sdk_bedrock_data_automation.types.data_automation_project_arn
    import aws_sdk_bedrock_data_automation.types.data_automation_project_description
    import aws_sdk_bedrock_data_automation.types.data_automation_project_name
    import aws_sdk_bedrock_data_automation.types.data_automation_project_stage
    import aws_sdk_bedrock_data_automation.types.data_automation_project_status
    import aws_sdk_bedrock_data_automation.types.data_automation_project_type
    import aws_sdk_bedrock_data_automation.types.date_timestamp
    import aws_sdk_bedrock_data_automation.types.kms_encryption_context
    import aws_sdk_bedrock_data_automation.types.kms_key_id
    import aws_sdk_bedrock_data_automation.types.override_configuration
    import aws_sdk_bedrock_data_automation.types.standard_output_configuration


class DataAutomationProject(TypedDict, closed=True):
    project_arn: "aws_sdk_bedrock_data_automation.types.data_automation_project_arn.DataAutomationProjectArn"
    creation_time: "aws_sdk_bedrock_data_automation.types.date_timestamp.DateTimestamp"
    last_modified_time: (
        "aws_sdk_bedrock_data_automation.types.date_timestamp.DateTimestamp"
    )
    project_name: "aws_sdk_bedrock_data_automation.types.data_automation_project_name.DataAutomationProjectName"
    project_stage: NotRequired[
        "aws_sdk_bedrock_data_automation.types.data_automation_project_stage.DataAutomationProjectStage"
    ]
    project_type: NotRequired[
        "aws_sdk_bedrock_data_automation.types.data_automation_project_type.DataAutomationProjectType"
    ]
    project_description: NotRequired[
        "aws_sdk_bedrock_data_automation.types.data_automation_project_description.DataAutomationProjectDescription"
    ]
    standard_output_configuration: NotRequired[
        "aws_sdk_bedrock_data_automation.types.standard_output_configuration.StandardOutputConfiguration"
    ]
    custom_output_configuration: NotRequired[
        "aws_sdk_bedrock_data_automation.types.custom_output_configuration.CustomOutputConfiguration"
    ]
    override_configuration: NotRequired[
        "aws_sdk_bedrock_data_automation.types.override_configuration.OverrideConfiguration"
    ]
    data_automation_library_configuration: NotRequired[
        "aws_sdk_bedrock_data_automation.types.data_automation_library_configuration.DataAutomationLibraryConfiguration"
    ]
    status: "aws_sdk_bedrock_data_automation.types.data_automation_project_status.DataAutomationProjectStatus"
    kms_key_id: NotRequired["aws_sdk_bedrock_data_automation.types.kms_key_id.KmsKeyId"]
    kms_encryption_context: NotRequired[
        "aws_sdk_bedrock_data_automation.types.kms_encryption_context.KmsEncryptionContext"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DataAutomationProject) -> dict:
    out: dict = {}
    out["projectArn"] = value["project_arn"]
    import aws_sdk_bedrock_data_automation.types.date_timestamp

    out["creationTime"] = (
        aws_sdk_bedrock_data_automation.types.date_timestamp.serialize_json(
            value["creation_time"]
        )
    )
    import aws_sdk_bedrock_data_automation.types.date_timestamp

    out["lastModifiedTime"] = (
        aws_sdk_bedrock_data_automation.types.date_timestamp.serialize_json(
            value["last_modified_time"]
        )
    )
    out["projectName"] = value["project_name"]
    if "project_stage" in value:
        import aws_sdk_bedrock_data_automation.types.data_automation_project_stage

        out["projectStage"] = (
            aws_sdk_bedrock_data_automation.types.data_automation_project_stage.serialize_json(
                value["project_stage"]
            )
        )
    if "project_type" in value:
        import aws_sdk_bedrock_data_automation.types.data_automation_project_type

        out["projectType"] = (
            aws_sdk_bedrock_data_automation.types.data_automation_project_type.serialize_json(
                value["project_type"]
            )
        )
    if "project_description" in value:
        out["projectDescription"] = value["project_description"]
    if "standard_output_configuration" in value:
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
    import aws_sdk_bedrock_data_automation.types.data_automation_project_status

    out["status"] = (
        aws_sdk_bedrock_data_automation.types.data_automation_project_status.serialize_json(
            value["status"]
        )
    )
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "kms_encryption_context" in value:
        import aws_sdk_bedrock_data_automation.types.kms_encryption_context

        out["kmsEncryptionContext"] = (
            aws_sdk_bedrock_data_automation.types.kms_encryption_context.serialize_json(
                value["kms_encryption_context"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataAutomationProject:
    out: DataAutomationProject = {}  # type: ignore[typeddict-item]
    if "projectArn" in data:
        out["project_arn"] = data["projectArn"]
    else:
        raise DeserializationError("DataAutomationProject.project_arn required")
    if "creationTime" in data:
        import aws_sdk_bedrock_data_automation.types.date_timestamp

        out["creation_time"] = (
            aws_sdk_bedrock_data_automation.types.date_timestamp.deserialize_json(
                data["creationTime"]
            )
        )
    else:
        raise DeserializationError("DataAutomationProject.creation_time required")
    if "lastModifiedTime" in data:
        import aws_sdk_bedrock_data_automation.types.date_timestamp

        out["last_modified_time"] = (
            aws_sdk_bedrock_data_automation.types.date_timestamp.deserialize_json(
                data["lastModifiedTime"]
            )
        )
    else:
        raise DeserializationError("DataAutomationProject.last_modified_time required")
    if "projectName" in data:
        out["project_name"] = data["projectName"]
    else:
        raise DeserializationError("DataAutomationProject.project_name required")
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
    if "projectDescription" in data:
        out["project_description"] = data["projectDescription"]
    if "standardOutputConfiguration" in data:
        import aws_sdk_bedrock_data_automation.types.standard_output_configuration

        out["standard_output_configuration"] = (
            aws_sdk_bedrock_data_automation.types.standard_output_configuration.deserialize_json(
                data["standardOutputConfiguration"]
            )
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
    if "status" in data:
        import aws_sdk_bedrock_data_automation.types.data_automation_project_status

        out["status"] = (
            aws_sdk_bedrock_data_automation.types.data_automation_project_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("DataAutomationProject.status required")
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    if "kmsEncryptionContext" in data:
        import aws_sdk_bedrock_data_automation.types.kms_encryption_context

        out["kms_encryption_context"] = (
            aws_sdk_bedrock_data_automation.types.kms_encryption_context.deserialize_json(
                data["kmsEncryptionContext"]
            )
        )
    return out
