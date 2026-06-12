"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#BatchDeleteImportDataError``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.batch_delete_import_data_error_code
    import aws_sdk_application_discovery_service.types.batch_delete_import_data_error_description
    import aws_sdk_application_discovery_service.types.import_task_identifier


class BatchDeleteImportDataError(TypedDict):
    import_task_id: NotRequired[
        "aws_sdk_application_discovery_service.types.import_task_identifier.ImportTaskIdentifier"
    ]
    """<p>The unique import ID associated with the error that occurred.</p>"""
    error_code: NotRequired[
        "aws_sdk_application_discovery_service.types.batch_delete_import_data_error_code.BatchDeleteImportDataErrorCode"
    ]
    """<p>The type of error that occurred for a specific import task.</p>"""
    error_description: NotRequired[
        "aws_sdk_application_discovery_service.types.batch_delete_import_data_error_description.BatchDeleteImportDataErrorDescription"
    ]
    """<p>The description of the error that occurred for a specific import task.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDeleteImportDataError) -> dict:
    out: dict = {}
    if "import_task_id" in value:
        out["importTaskId"] = value["import_task_id"]
    if "error_code" in value:
        import aws_sdk_application_discovery_service.types.batch_delete_import_data_error_code

        out["errorCode"] = (
            aws_sdk_application_discovery_service.types.batch_delete_import_data_error_code.serialize_aws_json_1_1(
                value["error_code"]
            )
        )
    if "error_description" in value:
        out["errorDescription"] = value["error_description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDeleteImportDataError:
    out: BatchDeleteImportDataError = {}  # type: ignore[typeddict-item]
    if "importTaskId" in data:
        out["import_task_id"] = data["importTaskId"]
    if "errorCode" in data:
        import aws_sdk_application_discovery_service.types.batch_delete_import_data_error_code

        out["error_code"] = (
            aws_sdk_application_discovery_service.types.batch_delete_import_data_error_code.deserialize_aws_json_1_1(
                data["errorCode"]
            )
        )
    if "errorDescription" in data:
        out["error_description"] = data["errorDescription"]
    return out
