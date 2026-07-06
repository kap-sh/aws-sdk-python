"""Generated from Smithy shape ``com.amazonaws.connect#CreateHoursOfOperationOverrideRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.common_human_readable_description
    import aws_sdk_connect.types.common_human_readable_name
    import aws_sdk_connect.types.hours_of_operation_id
    import aws_sdk_connect.types.hours_of_operation_override_config_list
    import aws_sdk_connect.types.hours_of_operation_override_year_month_day_date_format
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.override_type
    import aws_sdk_connect.types.recurrence_config


class CreateHoursOfOperationOverrideRequest(TypedDict, closed=True):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance.</p>"""
    hours_of_operation_id: (
        "aws_sdk_connect.types.hours_of_operation_id.HoursOfOperationId"
    )
    """<p>The identifier for the hours of operation</p>"""
    name: "aws_sdk_connect.types.common_human_readable_name.CommonHumanReadableName"
    """<p>The name of the hours of operation override.</p>"""
    description: NotRequired[
        "aws_sdk_connect.types.common_human_readable_description.CommonHumanReadableDescription"
    ]
    """<p>The description of the hours of operation override.</p>"""
    config: "aws_sdk_connect.types.hours_of_operation_override_config_list.HoursOfOperationOverrideConfigList"
    """<p>Configuration information for the hours of operation override: day, start time, and end time.</p>"""
    effective_from: "aws_sdk_connect.types.hours_of_operation_override_year_month_day_date_format.HoursOfOperationOverrideYearMonthDayDateFormat"
    """<p>The date from when the hours of operation override is effective.</p>"""
    effective_till: "aws_sdk_connect.types.hours_of_operation_override_year_month_day_date_format.HoursOfOperationOverrideYearMonthDayDateFormat"
    """<p>The date until when the hours of operation override is effective.</p>"""
    recurrence_config: NotRequired[
        "aws_sdk_connect.types.recurrence_config.RecurrenceConfig"
    ]
    """<p>Configuration for a recurring event.</p>"""
    override_type: NotRequired["aws_sdk_connect.types.override_type.OverrideType"]
    r"""<p>Whether the override will be defined as a <i>standard</i> or as a <i>recurring event</i>.</p> <p>For more information about how override types are applied, see <a href=\"https://docs.aws.amazon.com/https:/docs.aws.amazon.com/connect/latest/adminguide/hours-of-operation-overrides.html\">Build your list of overrides</a> in the <i> Administrator Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateHoursOfOperationOverrideRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import aws_sdk_connect.types.hours_of_operation_override_config_list

    out["Config"] = (
        aws_sdk_connect.types.hours_of_operation_override_config_list.serialize_json(
            value["config"]
        )
    )
    out["EffectiveFrom"] = value["effective_from"]
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


def deserialize_json(data: dict) -> CreateHoursOfOperationOverrideRequest:
    out: CreateHoursOfOperationOverrideRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError(
            "CreateHoursOfOperationOverrideRequest.name required"
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "Config" in data:
        import aws_sdk_connect.types.hours_of_operation_override_config_list

        out["config"] = (
            aws_sdk_connect.types.hours_of_operation_override_config_list.deserialize_json(
                data["Config"]
            )
        )
    else:
        raise DeserializationError(
            "CreateHoursOfOperationOverrideRequest.config required"
        )
    if "EffectiveFrom" in data:
        out["effective_from"] = data["EffectiveFrom"]
    else:
        raise DeserializationError(
            "CreateHoursOfOperationOverrideRequest.effective_from required"
        )
    if "EffectiveTill" in data:
        out["effective_till"] = data["EffectiveTill"]
    else:
        raise DeserializationError(
            "CreateHoursOfOperationOverrideRequest.effective_till required"
        )
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
