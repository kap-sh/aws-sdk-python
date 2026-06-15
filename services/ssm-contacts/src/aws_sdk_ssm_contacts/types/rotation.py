"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#Rotation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.date_time
    import aws_sdk_ssm_contacts.types.recurrence_settings
    import aws_sdk_ssm_contacts.types.rotation_name
    import aws_sdk_ssm_contacts.types.ssm_contacts_arn
    import aws_sdk_ssm_contacts.types.ssm_contacts_arn_list
    import aws_sdk_ssm_contacts.types.time_zone_id


class Rotation(TypedDict):
    rotation_arn: "aws_sdk_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The Amazon Resource Name (ARN) of the rotation.</p>"""
    name: "aws_sdk_ssm_contacts.types.rotation_name.RotationName"
    """<p>The name of the rotation.</p>"""
    contact_ids: NotRequired[
        "aws_sdk_ssm_contacts.types.ssm_contacts_arn_list.SsmContactsArnList"
    ]
    """<p>The Amazon Resource Names (ARNs) of the contacts assigned to the rotation team.</p>"""
    start_time: NotRequired["aws_sdk_ssm_contacts.types.date_time.DateTime"]
    """<p>The date and time the rotation becomes active.</p>"""
    time_zone_id: NotRequired["aws_sdk_ssm_contacts.types.time_zone_id.TimeZoneId"]
    r"""<p>The time zone the rotation’s activity is based on, in Internet Assigned Numbers Authority (IANA) format. For example: \"America/Los_Angeles\", \"UTC\", or \"Asia/Seoul\". </p>"""
    recurrence: NotRequired[
        "aws_sdk_ssm_contacts.types.recurrence_settings.RecurrenceSettings"
    ]
    """<p>Information about when an on-call rotation is in effect and how long the rotation period lasts.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Rotation) -> dict:
    out: dict = {}
    out["RotationArn"] = value["rotation_arn"]
    out["Name"] = value["name"]
    if "contact_ids" in value:
        import aws_sdk_ssm_contacts.types.ssm_contacts_arn_list

        out["ContactIds"] = (
            aws_sdk_ssm_contacts.types.ssm_contacts_arn_list.serialize_aws_json_1_1(
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
    if "recurrence" in value:
        import aws_sdk_ssm_contacts.types.recurrence_settings

        out["Recurrence"] = (
            aws_sdk_ssm_contacts.types.recurrence_settings.serialize_aws_json_1_1(
                value["recurrence"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Rotation:
    out: Rotation = {}  # type: ignore[typeddict-item]
    if "RotationArn" in data:
        out["rotation_arn"] = data["RotationArn"]
    else:
        raise DeserializationError("Rotation.rotation_arn required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("Rotation.name required")
    if "ContactIds" in data:
        import aws_sdk_ssm_contacts.types.ssm_contacts_arn_list

        out["contact_ids"] = (
            aws_sdk_ssm_contacts.types.ssm_contacts_arn_list.deserialize_aws_json_1_1(
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
    return out
