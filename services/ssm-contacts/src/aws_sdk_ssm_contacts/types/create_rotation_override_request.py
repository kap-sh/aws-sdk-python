"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#CreateRotationOverrideRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.date_time
    import aws_sdk_ssm_contacts.types.idempotency_token
    import aws_sdk_ssm_contacts.types.rotation_override_contacts_arn_list
    import aws_sdk_ssm_contacts.types.ssm_contacts_arn


class CreateRotationOverrideRequest(TypedDict):
    rotation_id: "aws_sdk_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The Amazon Resource Name (ARN) of the rotation to create an override for.</p>"""
    new_contact_ids: "aws_sdk_ssm_contacts.types.rotation_override_contacts_arn_list.RotationOverrideContactsArnList"
    """<p>The Amazon Resource Names (ARNs) of the contacts to replace those in the current on-call rotation with.</p> <p>If you want to include any current team members in the override shift, you must include their ARNs in the new contact ID list.</p>"""
    start_time: "aws_sdk_ssm_contacts.types.date_time.DateTime"
    """<p>The date and time when the override goes into effect.</p>"""
    end_time: "aws_sdk_ssm_contacts.types.date_time.DateTime"
    """<p>The date and time when the override ends.</p>"""
    idempotency_token: NotRequired[
        "aws_sdk_ssm_contacts.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A token that ensures that the operation is called only once with the specified details.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateRotationOverrideRequest) -> dict:
    out: dict = {}
    out["RotationId"] = value["rotation_id"]
    import aws_sdk_ssm_contacts.types.rotation_override_contacts_arn_list

    out["NewContactIds"] = (
        aws_sdk_ssm_contacts.types.rotation_override_contacts_arn_list.serialize_aws_json_1_1(
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
    if "idempotency_token" in value:
        out["IdempotencyToken"] = value["idempotency_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateRotationOverrideRequest:
    out: CreateRotationOverrideRequest = {}  # type: ignore[typeddict-item]
    if "RotationId" in data:
        out["rotation_id"] = data["RotationId"]
    else:
        raise DeserializationError("CreateRotationOverrideRequest.rotation_id required")
    if "NewContactIds" in data:
        import aws_sdk_ssm_contacts.types.rotation_override_contacts_arn_list

        out["new_contact_ids"] = (
            aws_sdk_ssm_contacts.types.rotation_override_contacts_arn_list.deserialize_aws_json_1_1(
                data["NewContactIds"]
            )
        )
    else:
        raise DeserializationError(
            "CreateRotationOverrideRequest.new_contact_ids required"
        )
    if "StartTime" in data:
        import aws_sdk_ssm_contacts.types.date_time

        out["start_time"] = (
            aws_sdk_ssm_contacts.types.date_time.deserialize_aws_json_1_1(
                data["StartTime"]
            )
        )
    else:
        raise DeserializationError("CreateRotationOverrideRequest.start_time required")
    if "EndTime" in data:
        import aws_sdk_ssm_contacts.types.date_time

        out["end_time"] = aws_sdk_ssm_contacts.types.date_time.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    else:
        raise DeserializationError("CreateRotationOverrideRequest.end_time required")
    if "IdempotencyToken" in data:
        out["idempotency_token"] = data["IdempotencyToken"]
    return out
