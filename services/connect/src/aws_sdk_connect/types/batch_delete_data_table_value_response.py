"""Generated from Smithy shape ``com.amazonaws.connect#BatchDeleteDataTableValueResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.batch_delete_data_table_value_failure_result_list
    import aws_sdk_connect.types.batch_delete_data_table_value_success_result_list


class BatchDeleteDataTableValueResponse(TypedDict, closed=True):
    successful: "aws_sdk_connect.types.batch_delete_data_table_value_success_result_list.BatchDeleteDataTableValueSuccessResultList"
    """<p>A list of successfully deleted values with their identifiers and updated lock versions.</p>"""
    failed: "aws_sdk_connect.types.batch_delete_data_table_value_failure_result_list.BatchDeleteDataTableValueFailureResultList"
    """<p>A list of values that failed to be deleted with error messages explaining the failure reason.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteDataTableValueResponse) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.batch_delete_data_table_value_success_result_list

    out["Successful"] = (
        aws_sdk_connect.types.batch_delete_data_table_value_success_result_list.serialize_json(
            value["successful"]
        )
    )
    import aws_sdk_connect.types.batch_delete_data_table_value_failure_result_list

    out["Failed"] = (
        aws_sdk_connect.types.batch_delete_data_table_value_failure_result_list.serialize_json(
            value["failed"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchDeleteDataTableValueResponse:
    out: BatchDeleteDataTableValueResponse = {}  # type: ignore[typeddict-item]
    if "Successful" in data:
        import aws_sdk_connect.types.batch_delete_data_table_value_success_result_list

        out["successful"] = (
            aws_sdk_connect.types.batch_delete_data_table_value_success_result_list.deserialize_json(
                data["Successful"]
            )
        )
    else:
        raise DeserializationError(
            "BatchDeleteDataTableValueResponse.successful required"
        )
    if "Failed" in data:
        import aws_sdk_connect.types.batch_delete_data_table_value_failure_result_list

        out["failed"] = (
            aws_sdk_connect.types.batch_delete_data_table_value_failure_result_list.deserialize_json(
                data["Failed"]
            )
        )
    else:
        raise DeserializationError("BatchDeleteDataTableValueResponse.failed required")
    return out
