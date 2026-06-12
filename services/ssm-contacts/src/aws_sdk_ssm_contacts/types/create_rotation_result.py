"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#CreateRotationResult``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.ssm_contacts_arn


class CreateRotationResult(TypedDict):
    rotation_arn: "aws_sdk_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The Amazon Resource Name (ARN) of the created rotation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateRotationResult) -> dict:
    out: dict = {}
    out["RotationArn"] = value["rotation_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateRotationResult:
    out: CreateRotationResult = {}  # type: ignore[typeddict-item]
    if "RotationArn" in data:
        out["rotation_arn"] = data["RotationArn"]
    else:
        raise DeserializationError("CreateRotationResult.rotation_arn required")
    return out
