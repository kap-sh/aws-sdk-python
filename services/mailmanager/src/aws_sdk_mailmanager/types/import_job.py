"""Generated from Smithy shape ``com.amazonaws.mailmanager#ImportJob``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_mailmanager.types.address_list_id
    import aws_sdk_mailmanager.types.error_message
    import aws_sdk_mailmanager.types.import_data_format
    import aws_sdk_mailmanager.types.import_job_status
    import aws_sdk_mailmanager.types.job_id
    import aws_sdk_mailmanager.types.job_items_count
    import aws_sdk_mailmanager.types.job_name
    import aws_sdk_mailmanager.types.pre_signed_url


class ImportJob(TypedDict):
    job_id: "aws_sdk_mailmanager.types.job_id.JobId"
    """<p>The identifier of the import job.</p>"""
    name: "aws_sdk_mailmanager.types.job_name.JobName"
    """<p>A user-friendly name for the import job.</p>"""
    status: "aws_sdk_mailmanager.types.import_job_status.ImportJobStatus"
    """<p>The status of the import job.</p>"""
    pre_signed_url: "aws_sdk_mailmanager.types.pre_signed_url.PreSignedUrl"
    """<p>The pre-signed URL target for uploading the input file.</p>"""
    imported_items_count: NotRequired[
        "aws_sdk_mailmanager.types.job_items_count.JobItemsCount"
    ]
    """<p>The number of addresses in the input that were successfully imported into the address list.</p>"""
    failed_items_count: NotRequired[
        "aws_sdk_mailmanager.types.job_items_count.JobItemsCount"
    ]
    """<p>The number of addresses in the input that failed to get imported into address list.</p>"""
    import_data_format: "aws_sdk_mailmanager.types.import_data_format.ImportDataFormat"
    """<p>The format of the input for the import job.</p>"""
    address_list_id: "aws_sdk_mailmanager.types.address_list_id.AddressListId"
    """<p>The unique identifier of the address list the import job was created for.</p>"""
    created_timestamp: "datetime.datetime"
    """<p>The timestamp of when the import job was created.</p>"""
    start_timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the import job was started.</p>"""
    completed_timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the import job was completed.</p>"""
    error: NotRequired["aws_sdk_mailmanager.types.error_message.ErrorMessage"]
    """<p>The reason for failure of an import job.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ImportJob) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    out["Name"] = value["name"]
    import aws_sdk_mailmanager.types.import_job_status

    out["Status"] = aws_sdk_mailmanager.types.import_job_status.serialize_aws_json_1_0(
        value["status"]
    )
    out["PreSignedUrl"] = value["pre_signed_url"]
    if "imported_items_count" in value:
        out["ImportedItemsCount"] = value["imported_items_count"]
    if "failed_items_count" in value:
        out["FailedItemsCount"] = value["failed_items_count"]
    import aws_sdk_mailmanager.types.import_data_format

    out["ImportDataFormat"] = (
        aws_sdk_mailmanager.types.import_data_format.serialize_aws_json_1_0(
            value["import_data_format"]
        )
    )
    out["AddressListId"] = value["address_list_id"]
    import aws_sdk_mailmanager.types._prelude.timestamp

    out["CreatedTimestamp"] = (
        aws_sdk_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
            value["created_timestamp"]
        )
    )
    if "start_timestamp" in value:
        import aws_sdk_mailmanager.types._prelude.timestamp

        out["StartTimestamp"] = (
            aws_sdk_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
                value["start_timestamp"]
            )
        )
    if "completed_timestamp" in value:
        import aws_sdk_mailmanager.types._prelude.timestamp

        out["CompletedTimestamp"] = (
            aws_sdk_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
                value["completed_timestamp"]
            )
        )
    if "error" in value:
        out["Error"] = value["error"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ImportJob:
    out: ImportJob = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    else:
        raise DeserializationError("ImportJob.job_id required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("ImportJob.name required")
    if "Status" in data:
        import aws_sdk_mailmanager.types.import_job_status

        out["status"] = (
            aws_sdk_mailmanager.types.import_job_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("ImportJob.status required")
    if "PreSignedUrl" in data:
        out["pre_signed_url"] = data["PreSignedUrl"]
    else:
        raise DeserializationError("ImportJob.pre_signed_url required")
    if "ImportedItemsCount" in data:
        out["imported_items_count"] = data["ImportedItemsCount"]
    if "FailedItemsCount" in data:
        out["failed_items_count"] = data["FailedItemsCount"]
    if "ImportDataFormat" in data:
        import aws_sdk_mailmanager.types.import_data_format

        out["import_data_format"] = (
            aws_sdk_mailmanager.types.import_data_format.deserialize_aws_json_1_0(
                data["ImportDataFormat"]
            )
        )
    else:
        raise DeserializationError("ImportJob.import_data_format required")
    if "AddressListId" in data:
        out["address_list_id"] = data["AddressListId"]
    else:
        raise DeserializationError("ImportJob.address_list_id required")
    if "CreatedTimestamp" in data:
        import aws_sdk_mailmanager.types._prelude.timestamp

        out["created_timestamp"] = (
            aws_sdk_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["CreatedTimestamp"]
            )
        )
    else:
        raise DeserializationError("ImportJob.created_timestamp required")
    if "StartTimestamp" in data:
        import aws_sdk_mailmanager.types._prelude.timestamp

        out["start_timestamp"] = (
            aws_sdk_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["StartTimestamp"]
            )
        )
    if "CompletedTimestamp" in data:
        import aws_sdk_mailmanager.types._prelude.timestamp

        out["completed_timestamp"] = (
            aws_sdk_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["CompletedTimestamp"]
            )
        )
    if "Error" in data:
        out["error"] = data["Error"]
    return out
