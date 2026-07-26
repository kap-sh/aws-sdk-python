"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#ImportTask``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_discovery_service.types.client_request_token
    import capo_application_discovery_service.types.file_classification
    import capo_application_discovery_service.types.import_status
    import capo_application_discovery_service.types.import_task_identifier
    import capo_application_discovery_service.types.import_task_name
    import capo_application_discovery_service.types.import_url
    import capo_application_discovery_service.types.integer
    import capo_application_discovery_service.types.s3_presigned_url
    import capo_application_discovery_service.types.time_stamp


class ImportTask(TypedDict, closed=True):
    import_task_id: NotRequired[
        "capo_application_discovery_service.types.import_task_identifier.ImportTaskIdentifier"
    ]
    """<p>The unique ID for a specific import task. These IDs aren't globally unique, but they are unique within an Amazon Web Services account.</p>"""
    client_request_token: NotRequired[
        "capo_application_discovery_service.types.client_request_token.ClientRequestToken"
    ]
    """<p>A unique token used to prevent the same import request from occurring more than once. If you didn't provide a token, a token was automatically generated when the import task request was sent.</p>"""
    name: NotRequired[
        "capo_application_discovery_service.types.import_task_name.ImportTaskName"
    ]
    """<p>A descriptive name for an import task. You can use this name to filter future requests related to this import task, such as identifying applications and servers that were included in this import task. We recommend that you use a meaningful name for each import task.</p>"""
    import_url: NotRequired[
        "capo_application_discovery_service.types.import_url.ImportURL"
    ]
    """<p>The URL for your import file that you've uploaded to Amazon S3.</p>"""
    status: NotRequired[
        "capo_application_discovery_service.types.import_status.ImportStatus"
    ]
    """<p>The status of the import task. An import can have the status of <code>IMPORT_COMPLETE</code> and still have some records fail to import from the overall request. More information can be found in the downloadable archive defined in the <code>errorsAndFailedEntriesZip</code> field, or in the Migration Hub management console.</p>"""
    import_request_time: NotRequired[
        "capo_application_discovery_service.types.time_stamp.TimeStamp"
    ]
    """<p>The time that the import task request was made, presented in the Unix time stamp format.</p>"""
    import_completion_time: NotRequired[
        "capo_application_discovery_service.types.time_stamp.TimeStamp"
    ]
    """<p>The time that the import task request finished, presented in the Unix time stamp format.</p>"""
    import_deleted_time: NotRequired[
        "capo_application_discovery_service.types.time_stamp.TimeStamp"
    ]
    """<p>The time that the import task request was deleted, presented in the Unix time stamp format.</p>"""
    file_classification: NotRequired[
        "capo_application_discovery_service.types.file_classification.FileClassification"
    ]
    """<p>The type of file detected by the import task.</p>"""
    server_import_success: "capo_application_discovery_service.types.integer.Integer"
    """<p>The total number of server records in the import file that were successfully imported.</p>"""
    server_import_failure: "capo_application_discovery_service.types.integer.Integer"
    """<p>The total number of server records in the import file that failed to be imported.</p>"""
    application_import_success: (
        "capo_application_discovery_service.types.integer.Integer"
    )
    """<p>The total number of application records in the import file that were successfully imported.</p>"""
    application_import_failure: (
        "capo_application_discovery_service.types.integer.Integer"
    )
    """<p>The total number of application records in the import file that failed to be imported.</p>"""
    errors_and_failed_entries_zip: NotRequired[
        "capo_application_discovery_service.types.s3_presigned_url.S3PresignedUrl"
    ]
    """<p>A link to a compressed archive folder (in the ZIP format) that contains an error log and a file of failed records. You can use these two files to quickly identify records that failed, why they failed, and correct those records. Afterward, you can upload the corrected file to your Amazon S3 bucket and create another import task request.</p> <p>This field also includes authorization information so you can confirm the authenticity of the compressed archive before you download it.</p> <p>If some records failed to be imported we recommend that you correct the records in the failed entries file and then imports that failed entries file. This prevents you from having to correct and update the larger original file and attempt importing it again.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportTask) -> dict:
    out: dict = {}
    if "import_task_id" in value:
        out["importTaskId"] = value["import_task_id"]
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    if "name" in value:
        out["name"] = value["name"]
    if "import_url" in value:
        out["importUrl"] = value["import_url"]
    if "status" in value:
        import capo_application_discovery_service.types.import_status

        out["status"] = (
            capo_application_discovery_service.types.import_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "import_request_time" in value:
        import capo_application_discovery_service.types.time_stamp

        out["importRequestTime"] = (
            capo_application_discovery_service.types.time_stamp.serialize_aws_json_1_1(
                value["import_request_time"]
            )
        )
    if "import_completion_time" in value:
        import capo_application_discovery_service.types.time_stamp

        out["importCompletionTime"] = (
            capo_application_discovery_service.types.time_stamp.serialize_aws_json_1_1(
                value["import_completion_time"]
            )
        )
    if "import_deleted_time" in value:
        import capo_application_discovery_service.types.time_stamp

        out["importDeletedTime"] = (
            capo_application_discovery_service.types.time_stamp.serialize_aws_json_1_1(
                value["import_deleted_time"]
            )
        )
    if "file_classification" in value:
        import capo_application_discovery_service.types.file_classification

        out["fileClassification"] = (
            capo_application_discovery_service.types.file_classification.serialize_aws_json_1_1(
                value["file_classification"]
            )
        )
    out["serverImportSuccess"] = value.get("server_import_success", 0)
    out["serverImportFailure"] = value.get("server_import_failure", 0)
    out["applicationImportSuccess"] = value.get("application_import_success", 0)
    out["applicationImportFailure"] = value.get("application_import_failure", 0)
    if "errors_and_failed_entries_zip" in value:
        out["errorsAndFailedEntriesZip"] = value["errors_and_failed_entries_zip"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportTask:
    out: ImportTask = {}  # type: ignore[typeddict-item]
    if "importTaskId" in data:
        out["import_task_id"] = data["importTaskId"]
    if "clientRequestToken" in data:
        out["client_request_token"] = data["clientRequestToken"]
    if "name" in data:
        out["name"] = data["name"]
    if "importUrl" in data:
        out["import_url"] = data["importUrl"]
    if "status" in data:
        import capo_application_discovery_service.types.import_status

        out["status"] = (
            capo_application_discovery_service.types.import_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "importRequestTime" in data:
        import capo_application_discovery_service.types.time_stamp

        out["import_request_time"] = (
            capo_application_discovery_service.types.time_stamp.deserialize_aws_json_1_1(
                data["importRequestTime"]
            )
        )
    if "importCompletionTime" in data:
        import capo_application_discovery_service.types.time_stamp

        out["import_completion_time"] = (
            capo_application_discovery_service.types.time_stamp.deserialize_aws_json_1_1(
                data["importCompletionTime"]
            )
        )
    if "importDeletedTime" in data:
        import capo_application_discovery_service.types.time_stamp

        out["import_deleted_time"] = (
            capo_application_discovery_service.types.time_stamp.deserialize_aws_json_1_1(
                data["importDeletedTime"]
            )
        )
    if "fileClassification" in data:
        import capo_application_discovery_service.types.file_classification

        out["file_classification"] = (
            capo_application_discovery_service.types.file_classification.deserialize_aws_json_1_1(
                data["fileClassification"]
            )
        )
    if "serverImportSuccess" in data:
        out["server_import_success"] = data["serverImportSuccess"]
    else:
        out["server_import_success"] = 0
    if "serverImportFailure" in data:
        out["server_import_failure"] = data["serverImportFailure"]
    else:
        out["server_import_failure"] = 0
    if "applicationImportSuccess" in data:
        out["application_import_success"] = data["applicationImportSuccess"]
    else:
        out["application_import_success"] = 0
    if "applicationImportFailure" in data:
        out["application_import_failure"] = data["applicationImportFailure"]
    else:
        out["application_import_failure"] = 0
    if "errorsAndFailedEntriesZip" in data:
        out["errors_and_failed_entries_zip"] = data["errorsAndFailedEntriesZip"]
    return out
