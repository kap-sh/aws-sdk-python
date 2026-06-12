"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#GetRotationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.ssm_contacts_arn


class GetRotationRequest(TypedDict):
    rotation_id: "aws_sdk_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The Amazon Resource Name (ARN) of the on-call rotation to retrieve information about.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRotationRequest) -> dict:
    out: dict = {}
    out["RotationId"] = value["rotation_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRotationRequest:
    out: GetRotationRequest = {}  # type: ignore[typeddict-item]
    if "RotationId" in data:
        out["rotation_id"] = data["RotationId"]
    else:
        raise DeserializationError("GetRotationRequest.rotation_id required")
    return out
