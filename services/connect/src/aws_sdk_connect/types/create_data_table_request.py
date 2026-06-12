"""Generated from Smithy shape ``com.amazonaws.connect#CreateDataTableRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.data_table_description
    import aws_sdk_connect.types.data_table_lock_level
    import aws_sdk_connect.types.data_table_name
    import aws_sdk_connect.types.data_table_status
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.tag_map
    import aws_sdk_connect.types.time_zone


class CreateDataTableRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p>The unique identifier for the Amazon Connect instance where the data table will be created.</p>"""
    name: "aws_sdk_connect.types.data_table_name.DataTableName"
    """<p>The name for the data table. Must conform to Connect human readable string specification and have 1-127 characters. Whitespace must be trimmed first. Must not start with the reserved case insensitive values 'connect:' and 'aws:'. Must be unique for the instance using case-insensitive comparison.</p>"""
    description: NotRequired[
        "aws_sdk_connect.types.data_table_description.DataTableDescription"
    ]
    """<p>An optional description for the data table. Must conform to Connect human readable string specification and have 0-250 characters. Whitespace must be trimmed first.</p>"""
    time_zone: "aws_sdk_connect.types.time_zone.TimeZone"
    """<p>The IANA timezone identifier to use when resolving time based dynamic values. Required even if no time slices are specified.</p>"""
    value_lock_level: "aws_sdk_connect.types.data_table_lock_level.DataTableLockLevel"
    """<p>The data level that concurrent value edits are locked on. One of DATA_TABLE, PRIMARY_VALUE, ATTRIBUTE, VALUE, and NONE. NONE is the default if unspecified. This determines how concurrent edits are handled when multiple users attempt to modify values simultaneously.</p>"""
    status: "aws_sdk_connect.types.data_table_status.DataTableStatus"
    """<p>The status of the data table. One of PUBLISHED or SAVED. Required parameter that determines the initial state of the table.</p>"""
    tags: NotRequired["aws_sdk_connect.types.tag_map.TagMap"]
    """<p>Key value pairs for attribute based access control (TBAC or ABAC). Optional tags to apply to the data table for organization and access control purposes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataTableRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["TimeZone"] = value["time_zone"]
    import aws_sdk_connect.types.data_table_lock_level

    out["ValueLockLevel"] = aws_sdk_connect.types.data_table_lock_level.serialize_json(
        value["value_lock_level"]
    )
    import aws_sdk_connect.types.data_table_status

    out["Status"] = aws_sdk_connect.types.data_table_status.serialize_json(
        value["status"]
    )
    if "tags" in value:
        import aws_sdk_connect.types.tag_map

        out["Tags"] = aws_sdk_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateDataTableRequest:
    out: CreateDataTableRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateDataTableRequest.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "TimeZone" in data:
        out["time_zone"] = data["TimeZone"]
    else:
        raise DeserializationError("CreateDataTableRequest.time_zone required")
    if "ValueLockLevel" in data:
        import aws_sdk_connect.types.data_table_lock_level

        out["value_lock_level"] = (
            aws_sdk_connect.types.data_table_lock_level.deserialize_json(
                data["ValueLockLevel"]
            )
        )
    else:
        raise DeserializationError("CreateDataTableRequest.value_lock_level required")
    if "Status" in data:
        import aws_sdk_connect.types.data_table_status

        out["status"] = aws_sdk_connect.types.data_table_status.deserialize_json(
            data["Status"]
        )
    else:
        raise DeserializationError("CreateDataTableRequest.status required")
    if "Tags" in data:
        import aws_sdk_connect.types.tag_map

        out["tags"] = aws_sdk_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
