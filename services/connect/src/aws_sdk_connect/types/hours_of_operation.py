"""Generated from Smithy shape ``com.amazonaws.connect#HoursOfOperation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.common_name_length127
    import aws_sdk_connect.types.hours_of_operation_config_list
    import aws_sdk_connect.types.hours_of_operation_description
    import aws_sdk_connect.types.hours_of_operation_id
    import aws_sdk_connect.types.parent_hours_of_operations_list
    import aws_sdk_connect.types.region_name
    import aws_sdk_connect.types.tag_map
    import aws_sdk_connect.types.time_zone
    import aws_sdk_connect.types.timestamp


class HoursOfOperation(TypedDict):
    hours_of_operation_id: NotRequired[
        "aws_sdk_connect.types.hours_of_operation_id.HoursOfOperationId"
    ]
    """<p>The identifier for the hours of operation.</p>"""
    hours_of_operation_arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) for the hours of operation.</p>"""
    name: NotRequired["aws_sdk_connect.types.common_name_length127.CommonNameLength127"]
    """<p>The name for the hours of operation.</p>"""
    description: NotRequired[
        "aws_sdk_connect.types.hours_of_operation_description.HoursOfOperationDescription"
    ]
    """<p>The description for the hours of operation.</p>"""
    time_zone: NotRequired["aws_sdk_connect.types.time_zone.TimeZone"]
    """<p>The time zone for the hours of operation.</p>"""
    config: NotRequired[
        "aws_sdk_connect.types.hours_of_operation_config_list.HoursOfOperationConfigList"
    ]
    """<p>Configuration information for the hours of operation.</p>"""
    parent_hours_of_operations: NotRequired[
        "aws_sdk_connect.types.parent_hours_of_operations_list.ParentHoursOfOperationsList"
    ]
    """<p>Information about parent hours of operations.</p>"""
    tags: NotRequired["aws_sdk_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, { \"Tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>"""
    last_modified_time: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when this resource was last modified.</p>"""
    last_modified_region: NotRequired["aws_sdk_connect.types.region_name.RegionName"]
    """<p>The Amazon Web Services Region where this resource was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HoursOfOperation) -> dict:
    out: dict = {}
    if "hours_of_operation_id" in value:
        out["HoursOfOperationId"] = value["hours_of_operation_id"]
    if "hours_of_operation_arn" in value:
        out["HoursOfOperationArn"] = value["hours_of_operation_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "time_zone" in value:
        out["TimeZone"] = value["time_zone"]
    if "config" in value:
        import aws_sdk_connect.types.hours_of_operation_config_list

        out["Config"] = (
            aws_sdk_connect.types.hours_of_operation_config_list.serialize_json(
                value["config"]
            )
        )
    if "parent_hours_of_operations" in value:
        import aws_sdk_connect.types.parent_hours_of_operations_list

        out["ParentHoursOfOperations"] = (
            aws_sdk_connect.types.parent_hours_of_operations_list.serialize_json(
                value["parent_hours_of_operations"]
            )
        )
    if "tags" in value:
        import aws_sdk_connect.types.tag_map

        out["Tags"] = aws_sdk_connect.types.tag_map.serialize_json(value["tags"])
    if "last_modified_time" in value:
        import aws_sdk_connect.types.timestamp

        out["LastModifiedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "last_modified_region" in value:
        out["LastModifiedRegion"] = value["last_modified_region"]
    return out


def deserialize_json(data: dict) -> HoursOfOperation:
    out: HoursOfOperation = {}  # type: ignore[typeddict-item]
    if "HoursOfOperationId" in data:
        out["hours_of_operation_id"] = data["HoursOfOperationId"]
    if "HoursOfOperationArn" in data:
        out["hours_of_operation_arn"] = data["HoursOfOperationArn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "TimeZone" in data:
        out["time_zone"] = data["TimeZone"]
    if "Config" in data:
        import aws_sdk_connect.types.hours_of_operation_config_list

        out["config"] = (
            aws_sdk_connect.types.hours_of_operation_config_list.deserialize_json(
                data["Config"]
            )
        )
    if "ParentHoursOfOperations" in data:
        import aws_sdk_connect.types.parent_hours_of_operations_list

        out["parent_hours_of_operations"] = (
            aws_sdk_connect.types.parent_hours_of_operations_list.deserialize_json(
                data["ParentHoursOfOperations"]
            )
        )
    if "Tags" in data:
        import aws_sdk_connect.types.tag_map

        out["tags"] = aws_sdk_connect.types.tag_map.deserialize_json(data["Tags"])
    if "LastModifiedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["last_modified_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    if "LastModifiedRegion" in data:
        out["last_modified_region"] = data["LastModifiedRegion"]
    return out
