"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#BatchDeleteImportDataResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.batch_delete_import_data_error_list


class BatchDeleteImportDataResponse(TypedDict, closed=True):
    errors: NotRequired[
        "aws_sdk_application_discovery_service.types.batch_delete_import_data_error_list.BatchDeleteImportDataErrorList"
    ]
    """<p>Error messages returned for each import task that you deleted as a response for this command.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDeleteImportDataResponse) -> dict:
    out: dict = {}
    if "errors" in value:
        import aws_sdk_application_discovery_service.types.batch_delete_import_data_error_list

        out["errors"] = (
            aws_sdk_application_discovery_service.types.batch_delete_import_data_error_list.serialize_aws_json_1_1(
                value["errors"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDeleteImportDataResponse:
    out: BatchDeleteImportDataResponse = {}  # type: ignore[typeddict-item]
    if "errors" in data:
        import aws_sdk_application_discovery_service.types.batch_delete_import_data_error_list

        out["errors"] = (
            aws_sdk_application_discovery_service.types.batch_delete_import_data_error_list.deserialize_aws_json_1_1(
                data["errors"]
            )
        )
    return out
