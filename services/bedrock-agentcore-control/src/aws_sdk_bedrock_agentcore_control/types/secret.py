"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#Secret``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.secret_arn


class Secret(TypedDict):
    secret_arn: "aws_sdk_bedrock_agentcore_control.types.secret_arn.SecretArn"
    """<p>The Amazon Resource Name (ARN) of the secret in AWS Secrets Manager.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Secret) -> dict:
    out: dict = {}
    out["secretArn"] = value["secret_arn"]
    return out


def deserialize_json(data: dict) -> Secret:
    out: Secret = {}  # type: ignore[typeddict-item]
    if "secretArn" in data:
        out["secret_arn"] = data["secretArn"]
    else:
        raise DeserializationError("Secret.secret_arn required")
    return out
