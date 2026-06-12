"""Generated from Smithy shape ``com.amazonaws.connect#BatchDescribeDataTableValueResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.batch_describe_data_table_value_failure_result_list
    import aws_sdk_connect.types.batch_describe_data_table_value_success_result_list


class BatchDescribeDataTableValueResponse(TypedDict):
    successful: "aws_sdk_connect.types.batch_describe_data_table_value_success_result_list.BatchDescribeDataTableValueSuccessResultList"
    """<p>A list of successfully retrieved values with their data, metadata, and lock version information.</p>"""
    failed: "aws_sdk_connect.types.batch_describe_data_table_value_failure_result_list.BatchDescribeDataTableValueFailureResultList"
    """<p>A list of values that failed to be retrieved with error messages explaining the failure reason.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDescribeDataTableValueResponse) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.batch_describe_data_table_value_success_result_list

    out["Successful"] = (
        aws_sdk_connect.types.batch_describe_data_table_value_success_result_list.serialize_json(
            value["successful"]
        )
    )
    import aws_sdk_connect.types.batch_describe_data_table_value_failure_result_list

    out["Failed"] = (
        aws_sdk_connect.types.batch_describe_data_table_value_failure_result_list.serialize_json(
            value["failed"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchDescribeDataTableValueResponse:
    out: BatchDescribeDataTableValueResponse = {}  # type: ignore[typeddict-item]
    if "Successful" in data:
        import aws_sdk_connect.types.batch_describe_data_table_value_success_result_list

        out["successful"] = (
            aws_sdk_connect.types.batch_describe_data_table_value_success_result_list.deserialize_json(
                data["Successful"]
            )
        )
    else:
        raise DeserializationError(
            "BatchDescribeDataTableValueResponse.successful required"
        )
    if "Failed" in data:
        import aws_sdk_connect.types.batch_describe_data_table_value_failure_result_list

        out["failed"] = (
            aws_sdk_connect.types.batch_describe_data_table_value_failure_result_list.deserialize_json(
                data["Failed"]
            )
        )
    else:
        raise DeserializationError(
            "BatchDescribeDataTableValueResponse.failed required"
        )
    return out
