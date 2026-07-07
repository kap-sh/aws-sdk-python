"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#RotationOverride``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.date_time
    import aws_sdk_ssm_contacts.types.ssm_contacts_arn_list
    import aws_sdk_ssm_contacts.types.uuid


class RotationOverride(TypedDict, closed=True):
    rotation_override_id: "aws_sdk_ssm_contacts.types.uuid.Uuid"
    """<p>The Amazon Resource Name (ARN) of the override to an on-call rotation.</p>"""
    new_contact_ids: (
        "aws_sdk_ssm_contacts.types.ssm_contacts_arn_list.SsmContactsArnList"
    )
    """<p>The Amazon Resource Names (ARNs) of the contacts assigned to the override of the on-call rotation.</p>"""
    start_time: "aws_sdk_ssm_contacts.types.date_time.DateTime"
    """<p>The time a rotation override begins.</p>"""
    end_time: "aws_sdk_ssm_contacts.types.date_time.DateTime"
    """<p>The time a rotation override ends.</p>"""
    create_time: "aws_sdk_ssm_contacts.types.date_time.DateTime"
    """<p>The time a rotation override was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RotationOverride) -> dict:
    out: dict = {}
    out["RotationOverrideId"] = value["rotation_override_id"]
    import aws_sdk_ssm_contacts.types.ssm_contacts_arn_list

    out["NewContactIds"] = (
        aws_sdk_ssm_contacts.types.ssm_contacts_arn_list.serialize_aws_json_1_1(
            value["new_contact_ids"]
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
    import aws_sdk_ssm_contacts.types.date_time

    out["CreateTime"] = aws_sdk_ssm_contacts.types.date_time.serialize_aws_json_1_1(
        value["create_time"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RotationOverride:
    out: RotationOverride = {}  # type: ignore[typeddict-item]
    if "RotationOverrideId" in data:
        out["rotation_override_id"] = data["RotationOverrideId"]
    else:
        raise DeserializationError("RotationOverride.rotation_override_id required")
    if "NewContactIds" in data:
        import aws_sdk_ssm_contacts.types.ssm_contacts_arn_list

        out["new_contact_ids"] = (
            aws_sdk_ssm_contacts.types.ssm_contacts_arn_list.deserialize_aws_json_1_1(
                data["NewContactIds"]
            )
        )
    else:
        raise DeserializationError("RotationOverride.new_contact_ids required")
    if "StartTime" in data:
        import aws_sdk_ssm_contacts.types.date_time

        out["start_time"] = (
            aws_sdk_ssm_contacts.types.date_time.deserialize_aws_json_1_1(
                data["StartTime"]
            )
        )
    else:
        raise DeserializationError("RotationOverride.start_time required")
    if "EndTime" in data:
        import aws_sdk_ssm_contacts.types.date_time

        out["end_time"] = aws_sdk_ssm_contacts.types.date_time.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    else:
        raise DeserializationError("RotationOverride.end_time required")
    if "CreateTime" in data:
        import aws_sdk_ssm_contacts.types.date_time

        out["create_time"] = (
            aws_sdk_ssm_contacts.types.date_time.deserialize_aws_json_1_1(
                data["CreateTime"]
            )
        )
    else:
        raise DeserializationError("RotationOverride.create_time required")
    return out
