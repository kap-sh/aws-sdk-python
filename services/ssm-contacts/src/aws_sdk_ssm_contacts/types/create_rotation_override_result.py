"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#CreateRotationOverrideResult``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.uuid


class CreateRotationOverrideResult(TypedDict):
    rotation_override_id: "aws_sdk_ssm_contacts.types.uuid.Uuid"
    """<p>The Amazon Resource Name (ARN) of the created rotation override.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateRotationOverrideResult) -> dict:
    out: dict = {}
    out["RotationOverrideId"] = value["rotation_override_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateRotationOverrideResult:
    out: CreateRotationOverrideResult = {}  # type: ignore[typeddict-item]
    if "RotationOverrideId" in data:
        out["rotation_override_id"] = data["RotationOverrideId"]
    else:
        raise DeserializationError(
            "CreateRotationOverrideResult.rotation_override_id required"
        )
    return out
