"""Generated from Smithy shape ``com.amazonaws.connect#UpdateDataTableMetadataRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.data_table_description
    import aws_sdk_connect.types.data_table_id
    import aws_sdk_connect.types.data_table_lock_level
    import aws_sdk_connect.types.data_table_name
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.time_zone


class UpdateDataTableMetadataRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p>The unique identifier for the Amazon Connect instance.</p>"""
    data_table_id: "aws_sdk_connect.types.data_table_id.DataTableId"
    """<p>The unique identifier for the data table. Must also accept the table ARN with or without a version alias. If the version is provided as part of the identifier or ARN, the version must be $LATEST. Providing any other alias fails with an error.</p>"""
    name: "aws_sdk_connect.types.data_table_name.DataTableName"
    """<p>The updated name for the data table. Must conform to Connect human readable string specification and have 1-127 characters. Must be unique for the instance using case-insensitive comparison.</p>"""
    description: NotRequired[
        "aws_sdk_connect.types.data_table_description.DataTableDescription"
    ]
    """<p>The updated description for the data table. Must conform to Connect human readable string specification and have 0-250 characters.</p>"""
    value_lock_level: "aws_sdk_connect.types.data_table_lock_level.DataTableLockLevel"
    """<p>The updated value lock level for the data table. One of DATA_TABLE, PRIMARY_VALUE, ATTRIBUTE, VALUE, and NONE.</p>"""
    time_zone: "aws_sdk_connect.types.time_zone.TimeZone"
    """<p>The updated IANA timezone identifier to use when resolving time based dynamic values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataTableMetadataRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import aws_sdk_connect.types.data_table_lock_level

    out["ValueLockLevel"] = aws_sdk_connect.types.data_table_lock_level.serialize_json(
        value["value_lock_level"]
    )
    out["TimeZone"] = value["time_zone"]
    return out


def deserialize_json(data: dict) -> UpdateDataTableMetadataRequest:
    out: UpdateDataTableMetadataRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateDataTableMetadataRequest.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "ValueLockLevel" in data:
        import aws_sdk_connect.types.data_table_lock_level

        out["value_lock_level"] = (
            aws_sdk_connect.types.data_table_lock_level.deserialize_json(
                data["ValueLockLevel"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateDataTableMetadataRequest.value_lock_level required"
        )
    if "TimeZone" in data:
        out["time_zone"] = data["TimeZone"]
    else:
        raise DeserializationError("UpdateDataTableMetadataRequest.time_zone required")
    return out
