"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#SecretsManagerLocation``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.tool_secret_arn


class SecretsManagerLocation(TypedDict):
    secret_arn: "aws_sdk_bedrock_agentcore_control.types.tool_secret_arn.ToolSecretArn"
    """<p>The ARN of the Amazon Web Services Secrets Manager secret containing the certificate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SecretsManagerLocation) -> dict:
    out: dict = {}
    out["secretArn"] = value["secret_arn"]
    return out


def deserialize_json(data: dict) -> SecretsManagerLocation:
    out: SecretsManagerLocation = {}  # type: ignore[typeddict-item]
    if "secretArn" in data:
        out["secret_arn"] = data["secretArn"]
    else:
        raise DeserializationError("SecretsManagerLocation.secret_arn required")
    return out
