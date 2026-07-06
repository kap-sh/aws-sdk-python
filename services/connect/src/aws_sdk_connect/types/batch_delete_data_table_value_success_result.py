"""Generated from Smithy shape ``com.amazonaws.connect#BatchDeleteDataTableValueSuccessResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.data_table_lock_version
    import aws_sdk_connect.types.data_table_name
    import aws_sdk_connect.types.primary_values_set


class BatchDeleteDataTableValueSuccessResult(TypedDict, closed=True):
    primary_values: "aws_sdk_connect.types.primary_values_set.PrimaryValuesSet"
    """<p>The result's primary values.</p>"""
    attribute_name: "aws_sdk_connect.types.data_table_name.DataTableName"
    """<p>The result's attribute name.</p>"""
    lock_version: "aws_sdk_connect.types.data_table_lock_version.DataTableLockVersion"
    """<p>The result's lock version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteDataTableValueSuccessResult) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.primary_values_set

    out["PrimaryValues"] = aws_sdk_connect.types.primary_values_set.serialize_json(
        value["primary_values"]
    )
    out["AttributeName"] = value["attribute_name"]
    import aws_sdk_connect.types.data_table_lock_version

    out["LockVersion"] = aws_sdk_connect.types.data_table_lock_version.serialize_json(
        value["lock_version"]
    )
    return out


def deserialize_json(data: dict) -> BatchDeleteDataTableValueSuccessResult:
    out: BatchDeleteDataTableValueSuccessResult = {}  # type: ignore[typeddict-item]
    if "PrimaryValues" in data:
        import aws_sdk_connect.types.primary_values_set

        out["primary_values"] = (
            aws_sdk_connect.types.primary_values_set.deserialize_json(
                data["PrimaryValues"]
            )
        )
    else:
        raise DeserializationError(
            "BatchDeleteDataTableValueSuccessResult.primary_values required"
        )
    if "AttributeName" in data:
        out["attribute_name"] = data["AttributeName"]
    else:
        raise DeserializationError(
            "BatchDeleteDataTableValueSuccessResult.attribute_name required"
        )
    if "LockVersion" in data:
        import aws_sdk_connect.types.data_table_lock_version

        out["lock_version"] = (
            aws_sdk_connect.types.data_table_lock_version.deserialize_json(
                data["LockVersion"]
            )
        )
    else:
        raise DeserializationError(
            "BatchDeleteDataTableValueSuccessResult.lock_version required"
        )
    return out
