"""Generated from Smithy shape ``com.amazonaws.connect#BatchCreateDataTableValueSuccessResult``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.data_table_id
    import aws_sdk_connect.types.data_table_lock_version
    import aws_sdk_connect.types.data_table_name
    import aws_sdk_connect.types.primary_values_set


class BatchCreateDataTableValueSuccessResult(TypedDict):
    primary_values: "aws_sdk_connect.types.primary_values_set.PrimaryValuesSet"
    """<p>The result's primary values.</p>"""
    attribute_name: "aws_sdk_connect.types.data_table_name.DataTableName"
    """<p>The result's attribute name.</p>"""
    record_id: "aws_sdk_connect.types.data_table_id.DataTableId"
    """<p>The result's record ID.</p>"""
    lock_version: "aws_sdk_connect.types.data_table_lock_version.DataTableLockVersion"
    """<p>The result's lock version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateDataTableValueSuccessResult) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.primary_values_set

    out["PrimaryValues"] = aws_sdk_connect.types.primary_values_set.serialize_json(
        value["primary_values"]
    )
    out["AttributeName"] = value["attribute_name"]
    out["RecordId"] = value["record_id"]
    import aws_sdk_connect.types.data_table_lock_version

    out["LockVersion"] = aws_sdk_connect.types.data_table_lock_version.serialize_json(
        value["lock_version"]
    )
    return out


def deserialize_json(data: dict) -> BatchCreateDataTableValueSuccessResult:
    out: BatchCreateDataTableValueSuccessResult = {}  # type: ignore[typeddict-item]
    if "PrimaryValues" in data:
        import aws_sdk_connect.types.primary_values_set

        out["primary_values"] = (
            aws_sdk_connect.types.primary_values_set.deserialize_json(
                data["PrimaryValues"]
            )
        )
    else:
        raise DeserializationError(
            "BatchCreateDataTableValueSuccessResult.primary_values required"
        )
    if "AttributeName" in data:
        out["attribute_name"] = data["AttributeName"]
    else:
        raise DeserializationError(
            "BatchCreateDataTableValueSuccessResult.attribute_name required"
        )
    if "RecordId" in data:
        out["record_id"] = data["RecordId"]
    else:
        raise DeserializationError(
            "BatchCreateDataTableValueSuccessResult.record_id required"
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
            "BatchCreateDataTableValueSuccessResult.lock_version required"
        )
    return out
