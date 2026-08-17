"""Generated from Smithy shape ``com.amazonaws.secretsmanager#DeleteResourcePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_secrets_manager.types.name_type
    import capo_secrets_manager.types.secret_arn_type


class DeleteResourcePolicyResponse(TypedDict, closed=True):
    arn: NotRequired["capo_secrets_manager.types.secret_arn_type.SecretARNType"]
    """<p>The ARN of the secret that the resource-based policy was deleted for.</p>"""
    name: NotRequired["capo_secrets_manager.types.name_type.NameType"]
    """<p>The name of the secret that the resource-based policy was deleted for.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteResourcePolicyResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["ARN"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteResourcePolicyResponse:
    out: DeleteResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("ARN") is not None:
        out["arn"] = data["ARN"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    return out
