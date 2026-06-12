"""Generated from Smithy shape ``com.amazonaws.connect#BatchDescribeDataTableValueSuccessResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.data_table_id
    import aws_sdk_connect.types.data_table_lock_version
    import aws_sdk_connect.types.data_table_name
    import aws_sdk_connect.types.primary_values_response_set
    import aws_sdk_connect.types.region_name
    import aws_sdk_connect.types.string
    import aws_sdk_connect.types.timestamp


class BatchDescribeDataTableValueSuccessResult(TypedDict):
    record_id: "aws_sdk_connect.types.data_table_id.DataTableId"
    """<p>The result's record ID.</p>"""
    attribute_id: "aws_sdk_connect.types.data_table_id.DataTableId"
    """<p>The result's attribute ID.</p>"""
    primary_values: (
        "aws_sdk_connect.types.primary_values_response_set.PrimaryValuesResponseSet"
    )
    """<p>The result's primary values.</p>"""
    attribute_name: "aws_sdk_connect.types.data_table_name.DataTableName"
    """<p>The result's attribute name.</p>"""
    value: NotRequired["aws_sdk_connect.types.string.String"]
    """<p>The result's value.</p>"""
    lock_version: "aws_sdk_connect.types.data_table_lock_version.DataTableLockVersion"
    """<p>The result's lock version.</p>"""
    last_modified_time: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The result's last modified time.</p>"""
    last_modified_region: NotRequired["aws_sdk_connect.types.region_name.RegionName"]
    """<p>The result's last modified region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDescribeDataTableValueSuccessResult) -> dict:
    out: dict = {}
    out["RecordId"] = value["record_id"]
    out["AttributeId"] = value["attribute_id"]
    import aws_sdk_connect.types.primary_values_response_set

    out["PrimaryValues"] = (
        aws_sdk_connect.types.primary_values_response_set.serialize_json(
            value["primary_values"]
        )
    )
    out["AttributeName"] = value["attribute_name"]
    if "value" in value:
        out["Value"] = value["value"]
    import aws_sdk_connect.types.data_table_lock_version

    out["LockVersion"] = aws_sdk_connect.types.data_table_lock_version.serialize_json(
        value["lock_version"]
    )
    if "last_modified_time" in value:
        import aws_sdk_connect.types.timestamp

        out["LastModifiedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "last_modified_region" in value:
        out["LastModifiedRegion"] = value["last_modified_region"]
    return out


def deserialize_json(data: dict) -> BatchDescribeDataTableValueSuccessResult:
    out: BatchDescribeDataTableValueSuccessResult = {}  # type: ignore[typeddict-item]
    if "RecordId" in data:
        out["record_id"] = data["RecordId"]
    else:
        raise DeserializationError(
            "BatchDescribeDataTableValueSuccessResult.record_id required"
        )
    if "AttributeId" in data:
        out["attribute_id"] = data["AttributeId"]
    else:
        raise DeserializationError(
            "BatchDescribeDataTableValueSuccessResult.attribute_id required"
        )
    if "PrimaryValues" in data:
        import aws_sdk_connect.types.primary_values_response_set

        out["primary_values"] = (
            aws_sdk_connect.types.primary_values_response_set.deserialize_json(
                data["PrimaryValues"]
            )
        )
    else:
        raise DeserializationError(
            "BatchDescribeDataTableValueSuccessResult.primary_values required"
        )
    if "AttributeName" in data:
        out["attribute_name"] = data["AttributeName"]
    else:
        raise DeserializationError(
            "BatchDescribeDataTableValueSuccessResult.attribute_name required"
        )
    if "Value" in data:
        out["value"] = data["Value"]
    if "LockVersion" in data:
        import aws_sdk_connect.types.data_table_lock_version

        out["lock_version"] = (
            aws_sdk_connect.types.data_table_lock_version.deserialize_json(
                data["LockVersion"]
            )
        )
    else:
        raise DeserializationError(
            "BatchDescribeDataTableValueSuccessResult.lock_version required"
        )
    if "LastModifiedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["last_modified_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    if "LastModifiedRegion" in data:
        out["last_modified_region"] = data["LastModifiedRegion"]
    return out
