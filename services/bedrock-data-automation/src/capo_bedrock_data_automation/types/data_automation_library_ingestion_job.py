"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DataAutomationLibraryIngestionJob``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.data_automation_library_ingestion_job_arn
    import capo_bedrock_data_automation.types.date_timestamp
    import capo_bedrock_data_automation.types.entity_type
    import capo_bedrock_data_automation.types.library_ingestion_job_operation_type
    import capo_bedrock_data_automation.types.library_ingestion_job_status
    import capo_bedrock_data_automation.types.output_configuration


class DataAutomationLibraryIngestionJob(TypedDict, closed=True):
    job_arn: "capo_bedrock_data_automation.types.data_automation_library_ingestion_job_arn.DataAutomationLibraryIngestionJobArn"
    """ARN of the DataAutomationLibraryIngestionJob"""
    creation_time: "capo_bedrock_data_automation.types.date_timestamp.DateTimestamp"
    """Timestamp when the DataAutomationLibraryIngestionJob was created"""
    entity_type: "capo_bedrock_data_automation.types.entity_type.EntityType"
    """The entity type associated with DataAutomationLibraryIngestionJob"""
    operation_type: "capo_bedrock_data_automation.types.library_ingestion_job_operation_type.LibraryIngestionJobOperationType"
    """The operation associated with DataAutomationLibraryIngestionJob"""
    job_status: "capo_bedrock_data_automation.types.library_ingestion_job_status.LibraryIngestionJobStatus"
    """The status of the DataAutomationLibraryIngestionJob"""
    output_configuration: (
        "capo_bedrock_data_automation.types.output_configuration.OutputConfiguration"
    )
    """Output configuration of DataAutomationLibraryIngestionJob"""
    completion_time: NotRequired[
        "capo_bedrock_data_automation.types.date_timestamp.DateTimestamp"
    ]
    """Timestamp when the DataAutomationLibraryIngestionJob was completed"""
    error_message: NotRequired["str"]
    """Error message"""
    error_type: NotRequired["str"]
    """Error type"""


# --- restJson1 ser/de ---
def serialize_json(value: DataAutomationLibraryIngestionJob) -> dict:
    out: dict = {}
    out["jobArn"] = value["job_arn"]
    import capo_bedrock_data_automation.types.date_timestamp

    out["creationTime"] = (
        capo_bedrock_data_automation.types.date_timestamp.serialize_json(
            value["creation_time"]
        )
    )
    import capo_bedrock_data_automation.types.entity_type

    out["entityType"] = capo_bedrock_data_automation.types.entity_type.serialize_json(
        value["entity_type"]
    )
    import capo_bedrock_data_automation.types.library_ingestion_job_operation_type

    out["operationType"] = (
        capo_bedrock_data_automation.types.library_ingestion_job_operation_type.serialize_json(
            value["operation_type"]
        )
    )
    import capo_bedrock_data_automation.types.library_ingestion_job_status

    out["jobStatus"] = (
        capo_bedrock_data_automation.types.library_ingestion_job_status.serialize_json(
            value["job_status"]
        )
    )
    import capo_bedrock_data_automation.types.output_configuration

    out["outputConfiguration"] = (
        capo_bedrock_data_automation.types.output_configuration.serialize_json(
            value["output_configuration"]
        )
    )
    if "completion_time" in value:
        import capo_bedrock_data_automation.types.date_timestamp

        out["completionTime"] = (
            capo_bedrock_data_automation.types.date_timestamp.serialize_json(
                value["completion_time"]
            )
        )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "error_type" in value:
        out["errorType"] = value["error_type"]
    return out


def deserialize_json(data: dict) -> DataAutomationLibraryIngestionJob:
    out: DataAutomationLibraryIngestionJob = {}  # type: ignore[typeddict-item]
    if "jobArn" in data:
        out["job_arn"] = data["jobArn"]
    else:
        raise DeserializationError("DataAutomationLibraryIngestionJob.job_arn required")
    if "creationTime" in data:
        import capo_bedrock_data_automation.types.date_timestamp

        out["creation_time"] = (
            capo_bedrock_data_automation.types.date_timestamp.deserialize_json(
                data["creationTime"]
            )
        )
    else:
        raise DeserializationError(
            "DataAutomationLibraryIngestionJob.creation_time required"
        )
    if "entityType" in data:
        import capo_bedrock_data_automation.types.entity_type

        out["entity_type"] = (
            capo_bedrock_data_automation.types.entity_type.deserialize_json(
                data["entityType"]
            )
        )
    else:
        raise DeserializationError(
            "DataAutomationLibraryIngestionJob.entity_type required"
        )
    if "operationType" in data:
        import capo_bedrock_data_automation.types.library_ingestion_job_operation_type

        out["operation_type"] = (
            capo_bedrock_data_automation.types.library_ingestion_job_operation_type.deserialize_json(
                data["operationType"]
            )
        )
    else:
        raise DeserializationError(
            "DataAutomationLibraryIngestionJob.operation_type required"
        )
    if "jobStatus" in data:
        import capo_bedrock_data_automation.types.library_ingestion_job_status

        out["job_status"] = (
            capo_bedrock_data_automation.types.library_ingestion_job_status.deserialize_json(
                data["jobStatus"]
            )
        )
    else:
        raise DeserializationError(
            "DataAutomationLibraryIngestionJob.job_status required"
        )
    if "outputConfiguration" in data:
        import capo_bedrock_data_automation.types.output_configuration

        out["output_configuration"] = (
            capo_bedrock_data_automation.types.output_configuration.deserialize_json(
                data["outputConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "DataAutomationLibraryIngestionJob.output_configuration required"
        )
    if "completionTime" in data:
        import capo_bedrock_data_automation.types.date_timestamp

        out["completion_time"] = (
            capo_bedrock_data_automation.types.date_timestamp.deserialize_json(
                data["completionTime"]
            )
        )
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    if "errorType" in data:
        out["error_type"] = data["errorType"]
    return out
