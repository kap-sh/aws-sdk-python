"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#GetRotationOverrideResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.date_time
    import aws_sdk_ssm_contacts.types.ssm_contacts_arn
    import aws_sdk_ssm_contacts.types.ssm_contacts_arn_list
    import aws_sdk_ssm_contacts.types.uuid


class GetRotationOverrideResult(TypedDict):
    rotation_override_id: NotRequired["aws_sdk_ssm_contacts.types.uuid.Uuid"]
    """<p>The Amazon Resource Name (ARN) of the override to an on-call rotation.</p>"""
    rotation_arn: NotRequired[
        "aws_sdk_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the on-call rotation that was overridden.</p>"""
    new_contact_ids: NotRequired[
        "aws_sdk_ssm_contacts.types.ssm_contacts_arn_list.SsmContactsArnList"
    ]
    """<p>The Amazon Resource Names (ARNs) of the contacts assigned to the override of the on-call rotation.</p>"""
    start_time: NotRequired["aws_sdk_ssm_contacts.types.date_time.DateTime"]
    """<p>The date and time when the override goes into effect.</p>"""
    end_time: NotRequired["aws_sdk_ssm_contacts.types.date_time.DateTime"]
    """<p>The date and time when the override ends.</p>"""
    create_time: NotRequired["aws_sdk_ssm_contacts.types.date_time.DateTime"]
    """<p>The date and time when the override was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRotationOverrideResult) -> dict:
    out: dict = {}
    if "rotation_override_id" in value:
        out["RotationOverrideId"] = value["rotation_override_id"]
    if "rotation_arn" in value:
        out["RotationArn"] = value["rotation_arn"]
    if "new_contact_ids" in value:
        import aws_sdk_ssm_contacts.types.ssm_contacts_arn_list

        out["NewContactIds"] = (
            aws_sdk_ssm_contacts.types.ssm_contacts_arn_list.serialize_aws_json_1_1(
                value["new_contact_ids"]
            )
        )
    if "start_time" in value:
        import aws_sdk_ssm_contacts.types.date_time

        out["StartTime"] = aws_sdk_ssm_contacts.types.date_time.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_ssm_contacts.types.date_time

        out["EndTime"] = aws_sdk_ssm_contacts.types.date_time.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "create_time" in value:
        import aws_sdk_ssm_contacts.types.date_time

        out["CreateTime"] = aws_sdk_ssm_contacts.types.date_time.serialize_aws_json_1_1(
            value["create_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRotationOverrideResult:
    out: GetRotationOverrideResult = {}  # type: ignore[typeddict-item]
    if "RotationOverrideId" in data:
        out["rotation_override_id"] = data["RotationOverrideId"]
    if "RotationArn" in data:
        out["rotation_arn"] = data["RotationArn"]
    if "NewContactIds" in data:
        import aws_sdk_ssm_contacts.types.ssm_contacts_arn_list

        out["new_contact_ids"] = (
            aws_sdk_ssm_contacts.types.ssm_contacts_arn_list.deserialize_aws_json_1_1(
                data["NewContactIds"]
            )
        )
    if "StartTime" in data:
        import aws_sdk_ssm_contacts.types.date_time

        out["start_time"] = (
            aws_sdk_ssm_contacts.types.date_time.deserialize_aws_json_1_1(
                data["StartTime"]
            )
        )
    if "EndTime" in data:
        import aws_sdk_ssm_contacts.types.date_time

        out["end_time"] = aws_sdk_ssm_contacts.types.date_time.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if "CreateTime" in data:
        import aws_sdk_ssm_contacts.types.date_time

        out["create_time"] = (
            aws_sdk_ssm_contacts.types.date_time.deserialize_aws_json_1_1(
                data["CreateTime"]
            )
        )
    return out
