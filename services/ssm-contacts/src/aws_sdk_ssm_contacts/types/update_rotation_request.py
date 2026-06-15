"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#UpdateRotationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.date_time
    import aws_sdk_ssm_contacts.types.recurrence_settings
    import aws_sdk_ssm_contacts.types.rotation_contacts_arn_list
    import aws_sdk_ssm_contacts.types.ssm_contacts_arn
    import aws_sdk_ssm_contacts.types.time_zone_id


class UpdateRotationRequest(TypedDict):
    rotation_id: "aws_sdk_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The Amazon Resource Name (ARN) of the rotation to update.</p>"""
    contact_ids: NotRequired[
        "aws_sdk_ssm_contacts.types.rotation_contacts_arn_list.RotationContactsArnList"
    ]
    """<p>The Amazon Resource Names (ARNs) of the contacts to include in the updated rotation. </p> <note> <p>Only the <code>PERSONAL</code> contact type is supported. The contact types <code>ESCALATION</code> and <code>ONCALL_SCHEDULE</code> are not supported for this operation. </p> </note> <p>The order in which you list the contacts is their shift order in the rotation schedule.</p>"""
    start_time: NotRequired["aws_sdk_ssm_contacts.types.date_time.DateTime"]
    """<p>The date and time the rotation goes into effect.</p>"""
    time_zone_id: NotRequired["aws_sdk_ssm_contacts.types.time_zone_id.TimeZoneId"]
    r"""<p>The time zone to base the updated rotation’s activity on, in Internet Assigned Numbers Authority (IANA) format. For example: \"America/Los_Angeles\", \"UTC\", or \"Asia/Seoul\". For more information, see the <a href=\"https://www.iana.org/time-zones\">Time Zone Database</a> on the IANA website.</p> <note> <p>Designators for time zones that don’t support Daylight Savings Time Rules, such as Pacific Standard Time (PST), aren't supported.</p> </note>"""
    recurrence: "aws_sdk_ssm_contacts.types.recurrence_settings.RecurrenceSettings"
    """<p>Information about how long the updated rotation lasts before restarting at the beginning of the shift order.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateRotationRequest) -> dict:
    out: dict = {}
    out["RotationId"] = value["rotation_id"]
    if "contact_ids" in value:
        import aws_sdk_ssm_contacts.types.rotation_contacts_arn_list

        out["ContactIds"] = (
            aws_sdk_ssm_contacts.types.rotation_contacts_arn_list.serialize_aws_json_1_1(
                value["contact_ids"]
            )
        )
    if "start_time" in value:
        import aws_sdk_ssm_contacts.types.date_time

        out["StartTime"] = aws_sdk_ssm_contacts.types.date_time.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "time_zone_id" in value:
        out["TimeZoneId"] = value["time_zone_id"]
    import aws_sdk_ssm_contacts.types.recurrence_settings

    out["Recurrence"] = (
        aws_sdk_ssm_contacts.types.recurrence_settings.serialize_aws_json_1_1(
            value["recurrence"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateRotationRequest:
    out: UpdateRotationRequest = {}  # type: ignore[typeddict-item]
    if "RotationId" in data:
        out["rotation_id"] = data["RotationId"]
    else:
        raise DeserializationError("UpdateRotationRequest.rotation_id required")
    if "ContactIds" in data:
        import aws_sdk_ssm_contacts.types.rotation_contacts_arn_list

        out["contact_ids"] = (
            aws_sdk_ssm_contacts.types.rotation_contacts_arn_list.deserialize_aws_json_1_1(
                data["ContactIds"]
            )
        )
    if "StartTime" in data:
        import aws_sdk_ssm_contacts.types.date_time

        out["start_time"] = (
            aws_sdk_ssm_contacts.types.date_time.deserialize_aws_json_1_1(
                data["StartTime"]
            )
        )
    if "TimeZoneId" in data:
        out["time_zone_id"] = data["TimeZoneId"]
    if "Recurrence" in data:
        import aws_sdk_ssm_contacts.types.recurrence_settings

        out["recurrence"] = (
            aws_sdk_ssm_contacts.types.recurrence_settings.deserialize_aws_json_1_1(
                data["Recurrence"]
            )
        )
    else:
        raise DeserializationError("UpdateRotationRequest.recurrence required")
    return out
