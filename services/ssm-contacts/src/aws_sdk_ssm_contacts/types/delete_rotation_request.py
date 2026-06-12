"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#DeleteRotationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.ssm_contacts_arn


class DeleteRotationRequest(TypedDict):
    rotation_id: "aws_sdk_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The Amazon Resource Name (ARN) of the on-call rotation to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteRotationRequest) -> dict:
    out: dict = {}
    out["RotationId"] = value["rotation_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteRotationRequest:
    out: DeleteRotationRequest = {}  # type: ignore[typeddict-item]
    if "RotationId" in data:
        out["rotation_id"] = data["RotationId"]
    else:
        raise DeserializationError("DeleteRotationRequest.rotation_id required")
    return out
