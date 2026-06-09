"""Generated from Smithy shape ``com.amazonaws.secretsmanager#PutResourcePolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.name_type
    import aws_sdk_secrets_manager.types.secret_arn_type


class PutResourcePolicyResponse(TypedDict):
    arn: NotRequired["aws_sdk_secrets_manager.types.secret_arn_type.SecretARNType"]
    """<p>The ARN of the secret.</p>"""
    name: NotRequired["aws_sdk_secrets_manager.types.name_type.NameType"]
    """<p>The name of the secret.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutResourcePolicyResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["ARN"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutResourcePolicyResponse:
    out: PutResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if "ARN" in data:
        out["arn"] = data["ARN"]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
