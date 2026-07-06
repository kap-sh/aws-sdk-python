"""Generated from Smithy shape ``com.amazonaws.connect#BatchCreateDataTableValueResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.batch_create_data_table_value_failure_result_list
    import aws_sdk_connect.types.batch_create_data_table_value_success_result_list


class BatchCreateDataTableValueResponse(TypedDict, closed=True):
    successful: "aws_sdk_connect.types.batch_create_data_table_value_success_result_list.BatchCreateDataTableValueSuccessResultList"
    """<p>A list of successfully created values with their identifiers and lock versions.</p>"""
    failed: "aws_sdk_connect.types.batch_create_data_table_value_failure_result_list.BatchCreateDataTableValueFailureResultList"
    """<p>A list of values that failed to be created with error messages explaining the failure reason.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateDataTableValueResponse) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.batch_create_data_table_value_success_result_list

    out["Successful"] = (
        aws_sdk_connect.types.batch_create_data_table_value_success_result_list.serialize_json(
            value["successful"]
        )
    )
    import aws_sdk_connect.types.batch_create_data_table_value_failure_result_list

    out["Failed"] = (
        aws_sdk_connect.types.batch_create_data_table_value_failure_result_list.serialize_json(
            value["failed"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchCreateDataTableValueResponse:
    out: BatchCreateDataTableValueResponse = {}  # type: ignore[typeddict-item]
    if "Successful" in data:
        import aws_sdk_connect.types.batch_create_data_table_value_success_result_list

        out["successful"] = (
            aws_sdk_connect.types.batch_create_data_table_value_success_result_list.deserialize_json(
                data["Successful"]
            )
        )
    else:
        raise DeserializationError(
            "BatchCreateDataTableValueResponse.successful required"
        )
    if "Failed" in data:
        import aws_sdk_connect.types.batch_create_data_table_value_failure_result_list

        out["failed"] = (
            aws_sdk_connect.types.batch_create_data_table_value_failure_result_list.deserialize_json(
                data["Failed"]
            )
        )
    else:
        raise DeserializationError("BatchCreateDataTableValueResponse.failed required")
    return out
