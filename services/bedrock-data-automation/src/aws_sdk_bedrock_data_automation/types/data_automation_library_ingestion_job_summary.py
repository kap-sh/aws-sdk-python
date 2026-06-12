"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DataAutomationLibraryIngestionJobSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.data_automation_library_ingestion_job_arn
    import aws_sdk_bedrock_data_automation.types.date_timestamp
    import aws_sdk_bedrock_data_automation.types.entity_type
    import aws_sdk_bedrock_data_automation.types.library_ingestion_job_operation_type
    import aws_sdk_bedrock_data_automation.types.library_ingestion_job_status


class DataAutomationLibraryIngestionJobSummary(TypedDict):
    job_arn: "aws_sdk_bedrock_data_automation.types.data_automation_library_ingestion_job_arn.DataAutomationLibraryIngestionJobArn"
    job_status: "aws_sdk_bedrock_data_automation.types.library_ingestion_job_status.LibraryIngestionJobStatus"
    entity_type: "aws_sdk_bedrock_data_automation.types.entity_type.EntityType"
    operation_type: "aws_sdk_bedrock_data_automation.types.library_ingestion_job_operation_type.LibraryIngestionJobOperationType"
    creation_time: "aws_sdk_bedrock_data_automation.types.date_timestamp.DateTimestamp"
    completion_time: NotRequired[
        "aws_sdk_bedrock_data_automation.types.date_timestamp.DateTimestamp"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DataAutomationLibraryIngestionJobSummary) -> dict:
    out: dict = {}
    out["jobArn"] = value["job_arn"]
    import aws_sdk_bedrock_data_automation.types.library_ingestion_job_status

    out["jobStatus"] = (
        aws_sdk_bedrock_data_automation.types.library_ingestion_job_status.serialize_json(
            value["job_status"]
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
    import aws_sdk_bedrock_data_automation.types.date_timestamp

    out["creationTime"] = (
        aws_sdk_bedrock_data_automation.types.date_timestamp.serialize_json(
            value["creation_time"]
        )
    )
    if "completion_time" in value:
        import aws_sdk_bedrock_data_automation.types.date_timestamp

        out["completionTime"] = (
            aws_sdk_bedrock_data_automation.types.date_timestamp.serialize_json(
                value["completion_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataAutomationLibraryIngestionJobSummary:
    out: DataAutomationLibraryIngestionJobSummary = {}  # type: ignore[typeddict-item]
    if "jobArn" in data:
        out["job_arn"] = data["jobArn"]
    else:
        raise DeserializationError(
            "DataAutomationLibraryIngestionJobSummary.job_arn required"
        )
    if "jobStatus" in data:
        import aws_sdk_bedrock_data_automation.types.library_ingestion_job_status

        out["job_status"] = (
            aws_sdk_bedrock_data_automation.types.library_ingestion_job_status.deserialize_json(
                data["jobStatus"]
            )
        )
    else:
        raise DeserializationError(
            "DataAutomationLibraryIngestionJobSummary.job_status required"
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
            "DataAutomationLibraryIngestionJobSummary.entity_type required"
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
            "DataAutomationLibraryIngestionJobSummary.operation_type required"
        )
    if "creationTime" in data:
        import aws_sdk_bedrock_data_automation.types.date_timestamp

        out["creation_time"] = (
            aws_sdk_bedrock_data_automation.types.date_timestamp.deserialize_json(
                data["creationTime"]
            )
        )
    else:
        raise DeserializationError(
            "DataAutomationLibraryIngestionJobSummary.creation_time required"
        )
    if "completionTime" in data:
        import aws_sdk_bedrock_data_automation.types.date_timestamp

        out["completion_time"] = (
            aws_sdk_bedrock_data_automation.types.date_timestamp.deserialize_json(
                data["completionTime"]
            )
        )
    return out
