"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#DeleteRotationOverrideRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.ssm_contacts_arn
    import aws_sdk_ssm_contacts.types.uuid


class DeleteRotationOverrideRequest(TypedDict):
    rotation_id: "aws_sdk_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The Amazon Resource Name (ARN) of the rotation that was overridden.</p>"""
    rotation_override_id: "aws_sdk_ssm_contacts.types.uuid.Uuid"
    """<p>The Amazon Resource Name (ARN) of the on-call rotation override to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteRotationOverrideRequest) -> dict:
    out: dict = {}
    out["RotationId"] = value["rotation_id"]
    out["RotationOverrideId"] = value["rotation_override_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteRotationOverrideRequest:
    out: DeleteRotationOverrideRequest = {}  # type: ignore[typeddict-item]
    if "RotationId" in data:
        out["rotation_id"] = data["RotationId"]
    else:
        raise DeserializationError("DeleteRotationOverrideRequest.rotation_id required")
    if "RotationOverrideId" in data:
        out["rotation_override_id"] = data["RotationOverrideId"]
    else:
        raise DeserializationError(
            "DeleteRotationOverrideRequest.rotation_override_id required"
        )
    return out
