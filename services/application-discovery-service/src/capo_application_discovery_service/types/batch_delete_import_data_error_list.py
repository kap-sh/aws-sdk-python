"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#BatchDeleteImportDataErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_discovery_service.types.batch_delete_import_data_error

BatchDeleteImportDataErrorList: TypeAlias = list[
    "capo_application_discovery_service.types.batch_delete_import_data_error.BatchDeleteImportDataError"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDeleteImportDataErrorList) -> list:
    import capo_application_discovery_service.types.batch_delete_import_data_error

    out: list = []
    for item in value:
        out.append(
            capo_application_discovery_service.types.batch_delete_import_data_error.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> BatchDeleteImportDataErrorList:
    import capo_application_discovery_service.types.batch_delete_import_data_error

    out: BatchDeleteImportDataErrorList = []
    for item in data:
        out.append(
            capo_application_discovery_service.types.batch_delete_import_data_error.deserialize_aws_json_1_1(
                item
            )
        )
    return out
