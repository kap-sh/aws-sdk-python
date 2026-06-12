"""Generated from Smithy shape ``com.amazonaws.connect#DataTable``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.data_table_description
    import aws_sdk_connect.types.data_table_id
    import aws_sdk_connect.types.data_table_lock_level
    import aws_sdk_connect.types.data_table_lock_version
    import aws_sdk_connect.types.data_table_name
    import aws_sdk_connect.types.data_table_status
    import aws_sdk_connect.types.data_table_version
    import aws_sdk_connect.types.region_name
    import aws_sdk_connect.types.tag_map
    import aws_sdk_connect.types.time_zone
    import aws_sdk_connect.types.timestamp


class DataTable(TypedDict):
    name: "aws_sdk_connect.types.data_table_name.DataTableName"
    """<p>The human-readable name of the data table. Must be unique within the instance and conform to Connect naming standards.</p>"""
    id: "aws_sdk_connect.types.data_table_id.DataTableId"
    """<p>The unique identifier for the data table. Does not include version aliases.</p>"""
    arn: "aws_sdk_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) for the data table. Does not include version aliases.</p>"""
    time_zone: "aws_sdk_connect.types.time_zone.TimeZone"
    """<p>The IANA timezone identifier used when resolving time based dynamic values. Required even if no time slices are specified.</p>"""
    description: NotRequired[
        "aws_sdk_connect.types.data_table_description.DataTableDescription"
    ]
    """<p>An optional description of the data table's purpose and contents.</p>"""
    value_lock_level: NotRequired[
        "aws_sdk_connect.types.data_table_lock_level.DataTableLockLevel"
    ]
    """<p>The data level that concurrent value edits are locked on. One of DATA_TABLE, PRIMARY_VALUE, ATTRIBUTE, VALUE, and NONE. Determines how concurrent edits are handled when multiple users attempt to modify values simultaneously.</p>"""
    lock_version: NotRequired[
        "aws_sdk_connect.types.data_table_lock_version.DataTableLockVersion"
    ]
    """<p>The lock version information used for optimistic locking and table versioning. Changes with each update to prevent concurrent modification conflicts.</p>"""
    version: NotRequired["aws_sdk_connect.types.data_table_version.DataTableVersion"]
    """<p>A unique identifier and alias for customer managed versions (not $LATEST or $SAVED).</p>"""
    version_description: NotRequired[
        "aws_sdk_connect.types.data_table_description.DataTableDescription"
    ]
    """<p>A description of the customer managed version.</p>"""
    status: NotRequired["aws_sdk_connect.types.data_table_status.DataTableStatus"]
    """<p>The current status of the data table. One of PUBLISHED or SAVED.</p>"""
    created_time: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when the data table was created.</p>"""
    last_modified_time: "aws_sdk_connect.types.timestamp.Timestamp"
    """<p>The timestamp when the data table or any of its properties were last modified.</p>"""
    last_modified_region: NotRequired["aws_sdk_connect.types.region_name.RegionName"]
    """<p>The Amazon Web Services Region where the data table was last modified, used for region replication.</p>"""
    tags: NotRequired["aws_sdk_connect.types.tag_map.TagMap"]
    """<p>Key-value pairs for attribute based access control (TBAC or ABAC) and organization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataTable) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Id"] = value["id"]
    out["Arn"] = value["arn"]
    out["TimeZone"] = value["time_zone"]
    if "description" in value:
        out["Description"] = value["description"]
    if "value_lock_level" in value:
        import aws_sdk_connect.types.data_table_lock_level

        out["ValueLockLevel"] = (
            aws_sdk_connect.types.data_table_lock_level.serialize_json(
                value["value_lock_level"]
            )
        )
    if "lock_version" in value:
        import aws_sdk_connect.types.data_table_lock_version

        out["LockVersion"] = (
            aws_sdk_connect.types.data_table_lock_version.serialize_json(
                value["lock_version"]
            )
        )
    if "version" in value:
        out["Version"] = value["version"]
    if "version_description" in value:
        out["VersionDescription"] = value["version_description"]
    if "status" in value:
        import aws_sdk_connect.types.data_table_status

        out["Status"] = aws_sdk_connect.types.data_table_status.serialize_json(
            value["status"]
        )
    if "created_time" in value:
        import aws_sdk_connect.types.timestamp

        out["CreatedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["created_time"]
        )
    import aws_sdk_connect.types.timestamp

    out["LastModifiedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
        value["last_modified_time"]
    )
    if "last_modified_region" in value:
        out["LastModifiedRegion"] = value["last_modified_region"]
    if "tags" in value:
        import aws_sdk_connect.types.tag_map

        out["Tags"] = aws_sdk_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> DataTable:
    out: DataTable = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DataTable.name required")
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("DataTable.id required")
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("DataTable.arn required")
    if "TimeZone" in data:
        out["time_zone"] = data["TimeZone"]
    else:
        raise DeserializationError("DataTable.time_zone required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "ValueLockLevel" in data:
        import aws_sdk_connect.types.data_table_lock_level

        out["value_lock_level"] = (
            aws_sdk_connect.types.data_table_lock_level.deserialize_json(
                data["ValueLockLevel"]
            )
        )
    if "LockVersion" in data:
        import aws_sdk_connect.types.data_table_lock_version

        out["lock_version"] = (
            aws_sdk_connect.types.data_table_lock_version.deserialize_json(
                data["LockVersion"]
            )
        )
    if "Version" in data:
        out["version"] = data["Version"]
    if "VersionDescription" in data:
        out["version_description"] = data["VersionDescription"]
    if "Status" in data:
        import aws_sdk_connect.types.data_table_status

        out["status"] = aws_sdk_connect.types.data_table_status.deserialize_json(
            data["Status"]
        )
    if "CreatedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["created_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    if "LastModifiedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["last_modified_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    else:
        raise DeserializationError("DataTable.last_modified_time required")
    if "LastModifiedRegion" in data:
        out["last_modified_region"] = data["LastModifiedRegion"]
    if "Tags" in data:
        import aws_sdk_connect.types.tag_map

        out["tags"] = aws_sdk_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
