"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#RotationShift``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.date_time
    import aws_sdk_ssm_contacts.types.shift_details
    import aws_sdk_ssm_contacts.types.shift_type
    import aws_sdk_ssm_contacts.types.ssm_contacts_arn_list


class RotationShift(TypedDict, closed=True):
    contact_ids: NotRequired[
        "aws_sdk_ssm_contacts.types.ssm_contacts_arn_list.SsmContactsArnList"
    ]
    """<p>The Amazon Resource Names (ARNs) of the contacts who are part of the shift rotation. </p>"""
    start_time: "aws_sdk_ssm_contacts.types.date_time.DateTime"
    """<p>The time a shift rotation begins.</p>"""
    end_time: "aws_sdk_ssm_contacts.types.date_time.DateTime"
    """<p>The time a shift rotation ends.</p>"""
    type: NotRequired["aws_sdk_ssm_contacts.types.shift_type.ShiftType"]
    """<p>The type of shift rotation.</p>"""
    shift_details: NotRequired["aws_sdk_ssm_contacts.types.shift_details.ShiftDetails"]
    """<p>Additional information about an on-call rotation shift.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RotationShift) -> dict:
    out: dict = {}
    if "contact_ids" in value:
        import aws_sdk_ssm_contacts.types.ssm_contacts_arn_list

        out["ContactIds"] = (
            aws_sdk_ssm_contacts.types.ssm_contacts_arn_list.serialize_aws_json_1_1(
                value["contact_ids"]
            )
        )
    import aws_sdk_ssm_contacts.types.date_time

    out["StartTime"] = aws_sdk_ssm_contacts.types.date_time.serialize_aws_json_1_1(
        value["start_time"]
    )
    import aws_sdk_ssm_contacts.types.date_time

    out["EndTime"] = aws_sdk_ssm_contacts.types.date_time.serialize_aws_json_1_1(
        value["end_time"]
    )
    if "type" in value:
        import aws_sdk_ssm_contacts.types.shift_type

        out["Type"] = aws_sdk_ssm_contacts.types.shift_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "shift_details" in value:
        import aws_sdk_ssm_contacts.types.shift_details

        out["ShiftDetails"] = (
            aws_sdk_ssm_contacts.types.shift_details.serialize_aws_json_1_1(
                value["shift_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RotationShift:
    out: RotationShift = {}  # type: ignore[typeddict-item]
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
    else:
        raise DeserializationError("RotationShift.start_time required")
    if "EndTime" in data:
        import aws_sdk_ssm_contacts.types.date_time

        out["end_time"] = aws_sdk_ssm_contacts.types.date_time.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    else:
        raise DeserializationError("RotationShift.end_time required")
    if "Type" in data:
        import aws_sdk_ssm_contacts.types.shift_type

        out["type"] = aws_sdk_ssm_contacts.types.shift_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if "ShiftDetails" in data:
        import aws_sdk_ssm_contacts.types.shift_details

        out["shift_details"] = (
            aws_sdk_ssm_contacts.types.shift_details.deserialize_aws_json_1_1(
                data["ShiftDetails"]
            )
        )
    return out
