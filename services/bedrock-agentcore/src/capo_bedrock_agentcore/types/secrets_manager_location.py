"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#SecretsManagerLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.secret_arn


class SecretsManagerLocation(TypedDict, closed=True):
    secret_arn: "capo_bedrock_agentcore.types.secret_arn.SecretArn"
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
