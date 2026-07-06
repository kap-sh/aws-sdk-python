"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#SecretReference``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.secret_id_type
    import aws_sdk_bedrock_agentcore_control.types.secret_json_key_type


class SecretReference(TypedDict, closed=True):
    secret_id: "aws_sdk_bedrock_agentcore_control.types.secret_id_type.SecretIdType"
    """<p>The ID of the AWS Secrets Manager secret that stores the secret value.</p>"""
    json_key: (
        "aws_sdk_bedrock_agentcore_control.types.secret_json_key_type.SecretJsonKeyType"
    )
    """<p>The JSON key used to extract the secret value from the AWS Secrets Manager secret.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SecretReference) -> dict:
    out: dict = {}
    out["secretId"] = value["secret_id"]
    out["jsonKey"] = value["json_key"]
    return out


def deserialize_json(data: dict) -> SecretReference:
    out: SecretReference = {}  # type: ignore[typeddict-item]
    if "secretId" in data:
        out["secret_id"] = data["secretId"]
    else:
        raise DeserializationError("SecretReference.secret_id required")
    if "jsonKey" in data:
        out["json_key"] = data["jsonKey"]
    else:
        raise DeserializationError("SecretReference.json_key required")
    return out
