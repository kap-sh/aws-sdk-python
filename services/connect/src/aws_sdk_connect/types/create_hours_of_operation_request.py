"""Generated from Smithy shape ``com.amazonaws.connect#CreateHoursOfOperationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.common_name_length127
    import aws_sdk_connect.types.hours_of_operation_config_list
    import aws_sdk_connect.types.hours_of_operation_description
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.parent_hours_of_operation_config_list
    import aws_sdk_connect.types.tag_map
    import aws_sdk_connect.types.time_zone


class CreateHoursOfOperationRequest(TypedDict, closed=True):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    name: "aws_sdk_connect.types.common_name_length127.CommonNameLength127"
    """<p>The name of the hours of operation.</p>"""
    description: NotRequired[
        "aws_sdk_connect.types.hours_of_operation_description.HoursOfOperationDescription"
    ]
    """<p>The description of the hours of operation.</p>"""
    time_zone: "aws_sdk_connect.types.time_zone.TimeZone"
    """<p>The time zone of the hours of operation.</p>"""
    config: "aws_sdk_connect.types.hours_of_operation_config_list.HoursOfOperationConfigList"
    """<p>Configuration information for the hours of operation: day, start time, and end time.</p>"""
    parent_hours_of_operation_configs: NotRequired[
        "aws_sdk_connect.types.parent_hours_of_operation_config_list.ParentHoursOfOperationConfigList"
    ]
    r"""<p>Configuration for parent hours of operations. Eg: ResourceArn. </p> <p>For more information about parent hours of operations, see <a href=\"https://docs.aws.amazon.com/https:/docs.aws.amazon.com/connect/latest/adminguide/hours-of-operation-overrides.html\">Link overrides from different hours of operation</a> in the <i> Administrator Guide</i>.</p>"""
    tags: NotRequired["aws_sdk_connect.types.tag_map.TagMap"]
    r"""<p>The tags used to organize, track, or control access for this resource. For example, { \"Tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateHoursOfOperationRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["TimeZone"] = value["time_zone"]
    import aws_sdk_connect.types.hours_of_operation_config_list

    out["Config"] = aws_sdk_connect.types.hours_of_operation_config_list.serialize_json(
        value["config"]
    )
    if "parent_hours_of_operation_configs" in value:
        import aws_sdk_connect.types.parent_hours_of_operation_config_list

        out["ParentHoursOfOperationConfigs"] = (
            aws_sdk_connect.types.parent_hours_of_operation_config_list.serialize_json(
                value["parent_hours_of_operation_configs"]
            )
        )
    if "tags" in value:
        import aws_sdk_connect.types.tag_map

        out["Tags"] = aws_sdk_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateHoursOfOperationRequest:
    out: CreateHoursOfOperationRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateHoursOfOperationRequest.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "TimeZone" in data:
        out["time_zone"] = data["TimeZone"]
    else:
        raise DeserializationError("CreateHoursOfOperationRequest.time_zone required")
    if "Config" in data:
        import aws_sdk_connect.types.hours_of_operation_config_list

        out["config"] = (
            aws_sdk_connect.types.hours_of_operation_config_list.deserialize_json(
                data["Config"]
            )
        )
    else:
        raise DeserializationError("CreateHoursOfOperationRequest.config required")
    if "ParentHoursOfOperationConfigs" in data:
        import aws_sdk_connect.types.parent_hours_of_operation_config_list

        out["parent_hours_of_operation_configs"] = (
            aws_sdk_connect.types.parent_hours_of_operation_config_list.deserialize_json(
                data["ParentHoursOfOperationConfigs"]
            )
        )
    if "Tags" in data:
        import aws_sdk_connect.types.tag_map

        out["tags"] = aws_sdk_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
