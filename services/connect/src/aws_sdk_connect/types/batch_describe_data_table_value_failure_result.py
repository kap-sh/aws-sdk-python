"""Generated from Smithy shape ``com.amazonaws.connect#BatchDescribeDataTableValueFailureResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.data_table_name
    import aws_sdk_connect.types.primary_values_set
    import aws_sdk_connect.types.string


class BatchDescribeDataTableValueFailureResult(TypedDict, closed=True):
    primary_values: "aws_sdk_connect.types.primary_values_set.PrimaryValuesSet"
    """<p>The result's primary values.</p>"""
    attribute_name: "aws_sdk_connect.types.data_table_name.DataTableName"
    """<p>The result's attribute name.</p>"""
    message: "aws_sdk_connect.types.string.String"
    """<p>The result's message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDescribeDataTableValueFailureResult) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.primary_values_set

    out["PrimaryValues"] = aws_sdk_connect.types.primary_values_set.serialize_json(
        value["primary_values"]
    )
    out["AttributeName"] = value["attribute_name"]
    out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BatchDescribeDataTableValueFailureResult:
    out: BatchDescribeDataTableValueFailureResult = {}  # type: ignore[typeddict-item]
    if "PrimaryValues" in data:
        import aws_sdk_connect.types.primary_values_set

        out["primary_values"] = (
            aws_sdk_connect.types.primary_values_set.deserialize_json(
                data["PrimaryValues"]
            )
        )
    else:
        raise DeserializationError(
            "BatchDescribeDataTableValueFailureResult.primary_values required"
        )
    if "AttributeName" in data:
        out["attribute_name"] = data["AttributeName"]
    else:
        raise DeserializationError(
            "BatchDescribeDataTableValueFailureResult.attribute_name required"
        )
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError(
            "BatchDescribeDataTableValueFailureResult.message required"
        )
    return out
