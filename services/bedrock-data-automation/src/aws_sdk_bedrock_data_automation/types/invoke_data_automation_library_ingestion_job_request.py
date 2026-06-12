"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#InvokeDataAutomationLibraryIngestionJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.client_token
    import aws_sdk_bedrock_data_automation.types.data_automation_library_arn
    import aws_sdk_bedrock_data_automation.types.entity_type
    import aws_sdk_bedrock_data_automation.types.input_configuration
    import aws_sdk_bedrock_data_automation.types.library_ingestion_job_operation_type
    import aws_sdk_bedrock_data_automation.types.notification_configuration
    import aws_sdk_bedrock_data_automation.types.output_configuration
    import aws_sdk_bedrock_data_automation.types.tag_list


class InvokeDataAutomationLibraryIngestionJobRequest(TypedDict):
    library_arn: "aws_sdk_bedrock_data_automation.types.data_automation_library_arn.DataAutomationLibraryArn"
    """ARN generated at the server side when a DataAutomationLibrary is created"""
    client_token: NotRequired[
        "aws_sdk_bedrock_data_automation.types.client_token.ClientToken"
    ]
    """Idempotency token"""
    input_configuration: (
        "aws_sdk_bedrock_data_automation.types.input_configuration.InputConfiguration"
    )
    """Input configuration of DataAutomationLibraryIngestionJob request"""
    entity_type: "aws_sdk_bedrock_data_automation.types.entity_type.EntityType"
    """The entity type for which DataAutomationLibraryIngestionJob is being run"""
    operation_type: "aws_sdk_bedrock_data_automation.types.library_ingestion_job_operation_type.LibraryIngestionJobOperationType"
    """The operation to be performed by DataAutomationLibraryIngestionJob"""
    output_configuration: (
        "aws_sdk_bedrock_data_automation.types.output_configuration.OutputConfiguration"
    )
    """Output configuration of DataAutomationLibraryIngestionJob"""
    notification_configuration: NotRequired[
        "aws_sdk_bedrock_data_automation.types.notification_configuration.NotificationConfiguration"
    ]
    """Notification configuration."""
    tags: NotRequired["aws_sdk_bedrock_data_automation.types.tag_list.TagList"]
    """List of tags"""


# --- restJson1 ser/de ---
def serialize_json(value: InvokeDataAutomationLibraryIngestionJobRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    import aws_sdk_bedrock_data_automation.types.input_configuration

    out["inputConfiguration"] = (
        aws_sdk_bedrock_data_automation.types.input_configuration.serialize_json(
            value["input_configuration"]
        )
    )
    import aws_sdk_bedrock_data_automation.types.entity_type

    out["entityType"] = (
        aws_sdk_bedrock_data_automation.types.entity_type.serialize_json(
            value["entity_type"]
        )
    )
    import aws_sdk_bedrock_data_automation.types.library_ingestion_job_operation_type

    out["operationType"] = (
        aws_sdk_bedrock_data_automation.types.library_ingestion_job_operation_type.serialize_json(
            value["operation_type"]
        )
    )
    import aws_sdk_bedrock_data_automation.types.output_configuration

    out["outputConfiguration"] = (
        aws_sdk_bedrock_data_automation.types.output_configuration.serialize_json(
            value["output_configuration"]
        )
    )
    if "notification_configuration" in value:
        import aws_sdk_bedrock_data_automation.types.notification_configuration

        out["notificationConfiguration"] = (
            aws_sdk_bedrock_data_automation.types.notification_configuration.serialize_json(
                value["notification_configuration"]
            )
        )
    if "tags" in value:
        import aws_sdk_bedrock_data_automation.types.tag_list

        out["tags"] = aws_sdk_bedrock_data_automation.types.tag_list.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> InvokeDataAutomationLibraryIngestionJobRequest:
    out: InvokeDataAutomationLibraryIngestionJobRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "inputConfiguration" in data:
        import aws_sdk_bedrock_data_automation.types.input_configuration

        out["input_configuration"] = (
            aws_sdk_bedrock_data_automation.types.input_configuration.deserialize_json(
                data["inputConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "InvokeDataAutomationLibraryIngestionJobRequest.input_configuration required"
        )
    if "entityType" in data:
        import aws_sdk_bedrock_data_automation.types.entity_type

        out["entity_type"] = (
            aws_sdk_bedrock_data_automation.types.entity_type.deserialize_json(
                data["entityType"]
            )
        )
    else:
        raise DeserializationError(
            "InvokeDataAutomationLibraryIngestionJobRequest.entity_type required"
        )
    if "operationType" in data:
        import aws_sdk_bedrock_data_automation.types.library_ingestion_job_operation_type

        out["operation_type"] = (
            aws_sdk_bedrock_data_automation.types.library_ingestion_job_operation_type.deserialize_json(
                data["operationType"]
            )
        )
    else:
        raise DeserializationError(
            "InvokeDataAutomationLibraryIngestionJobRequest.operation_type required"
        )
    if "outputConfiguration" in data:
        import aws_sdk_bedrock_data_automation.types.output_configuration

        out["output_configuration"] = (
            aws_sdk_bedrock_data_automation.types.output_configuration.deserialize_json(
                data["outputConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "InvokeDataAutomationLibraryIngestionJobRequest.output_configuration required"
        )
    if "notificationConfiguration" in data:
        import aws_sdk_bedrock_data_automation.types.notification_configuration

        out["notification_configuration"] = (
            aws_sdk_bedrock_data_automation.types.notification_configuration.deserialize_json(
                data["notificationConfiguration"]
            )
        )
    if "tags" in data:
        import aws_sdk_bedrock_data_automation.types.tag_list

        out["tags"] = aws_sdk_bedrock_data_automation.types.tag_list.deserialize_json(
            data["tags"]
        )
    return out
