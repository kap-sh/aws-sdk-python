"""Generated from Smithy shape ``com.amazonaws.connect#BatchDeleteDataTableValueRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.data_table_delete_value_identifier_list
    import aws_sdk_connect.types.data_table_id
    import aws_sdk_connect.types.instance_id


class BatchDeleteDataTableValueRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p>The unique identifier for the Amazon Connect instance.</p>"""
    data_table_id: "aws_sdk_connect.types.data_table_id.DataTableId"
    """<p>The unique identifier for the data table. Must also accept the table ARN with or without a version alias.</p>"""
    values: "aws_sdk_connect.types.data_table_delete_value_identifier_list.DataTableDeleteValueIdentifierList"
    """<p>A list of value identifiers to delete, each specifying primary values, attribute name, and lock version information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteDataTableValueRequest) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.data_table_delete_value_identifier_list

    out["Values"] = (
        aws_sdk_connect.types.data_table_delete_value_identifier_list.serialize_json(
            value["values"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchDeleteDataTableValueRequest:
    out: BatchDeleteDataTableValueRequest = {}  # type: ignore[typeddict-item]
    if "Values" in data:
        import aws_sdk_connect.types.data_table_delete_value_identifier_list

        out["values"] = (
            aws_sdk_connect.types.data_table_delete_value_identifier_list.deserialize_json(
                data["Values"]
            )
        )
    else:
        raise DeserializationError("BatchDeleteDataTableValueRequest.values required")
    return out
