"""Generated from Smithy shape ``com.amazonaws.connect#UpdateHoursOfOperationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.common_name_length127
    import aws_sdk_connect.types.hours_of_operation_config_list
    import aws_sdk_connect.types.hours_of_operation_id
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.time_zone
    import aws_sdk_connect.types.update_hours_of_operation_description


class UpdateHoursOfOperationRequest(TypedDict, closed=True):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    hours_of_operation_id: (
        "aws_sdk_connect.types.hours_of_operation_id.HoursOfOperationId"
    )
    """<p>The identifier of the hours of operation.</p>"""
    name: NotRequired["aws_sdk_connect.types.common_name_length127.CommonNameLength127"]
    """<p>The name of the hours of operation.</p>"""
    description: NotRequired[
        "aws_sdk_connect.types.update_hours_of_operation_description.UpdateHoursOfOperationDescription"
    ]
    """<p>The description of the hours of operation.</p>"""
    time_zone: NotRequired["aws_sdk_connect.types.time_zone.TimeZone"]
    """<p>The time zone of the hours of operation.</p>"""
    config: NotRequired[
        "aws_sdk_connect.types.hours_of_operation_config_list.HoursOfOperationConfigList"
    ]
    """<p>Configuration information of the hours of operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateHoursOfOperationRequest) -> dict:
    out: dict = {}
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
    return out


def deserialize_json(data: dict) -> UpdateHoursOfOperationRequest:
    out: UpdateHoursOfOperationRequest = {}  # type: ignore[typeddict-item]
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
    return out
