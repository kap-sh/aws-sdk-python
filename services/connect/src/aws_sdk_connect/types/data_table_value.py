"""Generated from Smithy shape ``com.amazonaws.connect#DataTableValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.data_table_lock_version
    import aws_sdk_connect.types.data_table_name
    import aws_sdk_connect.types.primary_values_set
    import aws_sdk_connect.types.region_name
    import aws_sdk_connect.types.string
    import aws_sdk_connect.types.timestamp


class DataTableValue(TypedDict, closed=True):
    primary_values: NotRequired[
        "aws_sdk_connect.types.primary_values_set.PrimaryValuesSet"
    ]
    """<p>The value's primary values.</p>"""
    attribute_name: "aws_sdk_connect.types.data_table_name.DataTableName"
    """<p>The value's attribute name.</p>"""
    value: "aws_sdk_connect.types.string.String"
    """<p>The value's value.</p>"""
    lock_version: NotRequired[
        "aws_sdk_connect.types.data_table_lock_version.DataTableLockVersion"
    ]
    """<p>The value's lock version.</p>"""
    last_modified_time: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The value's last modified time.</p>"""
    last_modified_region: NotRequired["aws_sdk_connect.types.region_name.RegionName"]
    """<p>The value's last modified region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataTableValue) -> dict:
    out: dict = {}
    if "primary_values" in value:
        import aws_sdk_connect.types.primary_values_set

        out["PrimaryValues"] = aws_sdk_connect.types.primary_values_set.serialize_json(
            value["primary_values"]
        )
    out["AttributeName"] = value["attribute_name"]
    out["Value"] = value["value"]
    if "lock_version" in value:
        import aws_sdk_connect.types.data_table_lock_version

        out["LockVersion"] = (
            aws_sdk_connect.types.data_table_lock_version.serialize_json(
                value["lock_version"]
            )
        )
    if "last_modified_time" in value:
        import aws_sdk_connect.types.timestamp

        out["LastModifiedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "last_modified_region" in value:
        out["LastModifiedRegion"] = value["last_modified_region"]
    return out


def deserialize_json(data: dict) -> DataTableValue:
    out: DataTableValue = {}  # type: ignore[typeddict-item]
    if "PrimaryValues" in data:
        import aws_sdk_connect.types.primary_values_set

        out["primary_values"] = (
            aws_sdk_connect.types.primary_values_set.deserialize_json(
                data["PrimaryValues"]
            )
        )
    if "AttributeName" in data:
        out["attribute_name"] = data["AttributeName"]
    else:
        raise DeserializationError("DataTableValue.attribute_name required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("DataTableValue.value required")
    if "LockVersion" in data:
        import aws_sdk_connect.types.data_table_lock_version

        out["lock_version"] = (
            aws_sdk_connect.types.data_table_lock_version.deserialize_json(
                data["LockVersion"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["last_modified_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    if "LastModifiedRegion" in data:
        out["last_modified_region"] = data["LastModifiedRegion"]
    return out
