"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#GetRotationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.date_time
    import aws_sdk_ssm_contacts.types.recurrence_settings
    import aws_sdk_ssm_contacts.types.rotation_contacts_arn_list
    import aws_sdk_ssm_contacts.types.rotation_name
    import aws_sdk_ssm_contacts.types.ssm_contacts_arn
    import aws_sdk_ssm_contacts.types.time_zone_id


class GetRotationResult(TypedDict, closed=True):
    rotation_arn: "aws_sdk_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The Amazon Resource Name (ARN) of the on-call rotation.</p>"""
    name: "aws_sdk_ssm_contacts.types.rotation_name.RotationName"
    """<p>The name of the on-call rotation.</p>"""
    contact_ids: (
        "aws_sdk_ssm_contacts.types.rotation_contacts_arn_list.RotationContactsArnList"
    )
    """<p>The Amazon Resource Names (ARNs) of the contacts assigned to the on-call rotation team.</p>"""
    start_time: "aws_sdk_ssm_contacts.types.date_time.DateTime"
    """<p>The specified start time for the on-call rotation.</p>"""
    time_zone_id: "aws_sdk_ssm_contacts.types.time_zone_id.TimeZoneId"
    """<p>The time zone that the rotation’s activity is based on, in Internet Assigned Numbers Authority (IANA) format.</p>"""
    recurrence: "aws_sdk_ssm_contacts.types.recurrence_settings.RecurrenceSettings"
    """<p>Specifies how long a rotation lasts before restarting at the beginning of the shift order.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRotationResult) -> dict:
    out: dict = {}
    out["RotationArn"] = value["rotation_arn"]
    out["Name"] = value["name"]
    import aws_sdk_ssm_contacts.types.rotation_contacts_arn_list

    out["ContactIds"] = (
        aws_sdk_ssm_contacts.types.rotation_contacts_arn_list.serialize_aws_json_1_1(
            value["contact_ids"]
        )
    )
    import aws_sdk_ssm_contacts.types.date_time

    out["StartTime"] = aws_sdk_ssm_contacts.types.date_time.serialize_aws_json_1_1(
        value["start_time"]
    )
    out["TimeZoneId"] = value["time_zone_id"]
    import aws_sdk_ssm_contacts.types.recurrence_settings

    out["Recurrence"] = (
        aws_sdk_ssm_contacts.types.recurrence_settings.serialize_aws_json_1_1(
            value["recurrence"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRotationResult:
    out: GetRotationResult = {}  # type: ignore[typeddict-item]
    if "RotationArn" in data:
        out["rotation_arn"] = data["RotationArn"]
    else:
        raise DeserializationError("GetRotationResult.rotation_arn required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("GetRotationResult.name required")
    if "ContactIds" in data:
        import aws_sdk_ssm_contacts.types.rotation_contacts_arn_list

        out["contact_ids"] = (
            aws_sdk_ssm_contacts.types.rotation_contacts_arn_list.deserialize_aws_json_1_1(
                data["ContactIds"]
            )
        )
    else:
        raise DeserializationError("GetRotationResult.contact_ids required")
    if "StartTime" in data:
        import aws_sdk_ssm_contacts.types.date_time

        out["start_time"] = (
            aws_sdk_ssm_contacts.types.date_time.deserialize_aws_json_1_1(
                data["StartTime"]
            )
        )
    else:
        raise DeserializationError("GetRotationResult.start_time required")
    if "TimeZoneId" in data:
        out["time_zone_id"] = data["TimeZoneId"]
    else:
        raise DeserializationError("GetRotationResult.time_zone_id required")
    if "Recurrence" in data:
        import aws_sdk_ssm_contacts.types.recurrence_settings

        out["recurrence"] = (
            aws_sdk_ssm_contacts.types.recurrence_settings.deserialize_aws_json_1_1(
                data["Recurrence"]
            )
        )
    else:
        raise DeserializationError("GetRotationResult.recurrence required")
    return out
