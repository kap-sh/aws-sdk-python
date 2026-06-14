"""Generated from Smithy shape ``com.amazonaws.connect#UpdateHoursOfOperationOverrideRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.common_human_readable_description
    import aws_sdk_connect.types.common_human_readable_name
    import aws_sdk_connect.types.hours_of_operation_id
    import aws_sdk_connect.types.hours_of_operation_override_config_list
    import aws_sdk_connect.types.hours_of_operation_override_id
    import aws_sdk_connect.types.hours_of_operation_override_year_month_day_date_format
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.override_type
    import aws_sdk_connect.types.recurrence_config


class UpdateHoursOfOperationOverrideRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance.</p>"""
    hours_of_operation_id: (
        "aws_sdk_connect.types.hours_of_operation_id.HoursOfOperationId"
    )
    """<p>The identifier for the hours of operation.</p>"""
    hours_of_operation_override_id: "aws_sdk_connect.types.hours_of_operation_override_id.HoursOfOperationOverrideId"
    """<p>The identifier for the hours of operation override.</p>"""
    name: NotRequired[
        "aws_sdk_connect.types.common_human_readable_name.CommonHumanReadableName"
    ]
    """<p>The name of the hours of operation override.</p>"""
    description: NotRequired[
        "aws_sdk_connect.types.common_human_readable_description.CommonHumanReadableDescription"
    ]
    """<p>The description of the hours of operation override.</p>"""
    config: NotRequired[
        "aws_sdk_connect.types.hours_of_operation_override_config_list.HoursOfOperationOverrideConfigList"
    ]
    """<p>Configuration information for the hours of operation override: day, start time, and end time.</p>"""
    effective_from: NotRequired[
        "aws_sdk_connect.types.hours_of_operation_override_year_month_day_date_format.HoursOfOperationOverrideYearMonthDayDateFormat"
    ]
    """<p>The date from when the hours of operation override would be effective.</p>"""
    effective_till: NotRequired[
        "aws_sdk_connect.types.hours_of_operation_override_year_month_day_date_format.HoursOfOperationOverrideYearMonthDayDateFormat"
    ]
    """<p>The date until the hours of operation override is effective.</p>"""
    recurrence_config: NotRequired[
        "aws_sdk_connect.types.recurrence_config.RecurrenceConfig"
    ]
    """<p>Configuration for a recurring event.</p>"""
    override_type: NotRequired["aws_sdk_connect.types.override_type.OverrideType"]
    r"""<p>Whether the override will be defined as a <i>standard</i> or as a <i>recurring event</i>.</p> <p>For more information about how override types are applied, see <a href=\"https://docs.aws.amazon.com/https:/docs.aws.amazon.com/connect/latest/adminguide/hours-of-operation-overrides.html\">Build your list of overrides</a> in the <i> Administrator Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateHoursOfOperationOverrideRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "config" in value:
        import aws_sdk_connect.types.hours_of_operation_override_config_list

        out["Config"] = (
            aws_sdk_connect.types.hours_of_operation_override_config_list.serialize_json(
                value["config"]
            )
        )
    if "effective_from" in value:
        out["EffectiveFrom"] = value["effective_from"]
    if "effective_till" in value:
        out["EffectiveTill"] = value["effective_till"]
    if "recurrence_config" in value:
        import aws_sdk_connect.types.recurrence_config

        out["RecurrenceConfig"] = (
            aws_sdk_connect.types.recurrence_config.serialize_json(
                value["recurrence_config"]
            )
        )
    if "override_type" in value:
        import aws_sdk_connect.types.override_type

        out["OverrideType"] = aws_sdk_connect.types.override_type.serialize_json(
            value["override_type"]
        )
    return out


def deserialize_json(data: dict) -> UpdateHoursOfOperationOverrideRequest:
    out: UpdateHoursOfOperationOverrideRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Config" in data:
        import aws_sdk_connect.types.hours_of_operation_override_config_list

        out["config"] = (
            aws_sdk_connect.types.hours_of_operation_override_config_list.deserialize_json(
                data["Config"]
            )
        )
    if "EffectiveFrom" in data:
        out["effective_from"] = data["EffectiveFrom"]
    if "EffectiveTill" in data:
        out["effective_till"] = data["EffectiveTill"]
    if "RecurrenceConfig" in data:
        import aws_sdk_connect.types.recurrence_config

        out["recurrence_config"] = (
            aws_sdk_connect.types.recurrence_config.deserialize_json(
                data["RecurrenceConfig"]
            )
        )
    if "OverrideType" in data:
        import aws_sdk_connect.types.override_type

        out["override_type"] = aws_sdk_connect.types.override_type.deserialize_json(
            data["OverrideType"]
        )
    return out
