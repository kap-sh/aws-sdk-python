"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CertificateLocation``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.secrets_manager_location


class _CertificateLocation_secretsManager(TypedDict):
    secretsManager: "aws_sdk_bedrock_agentcore.types.secrets_manager_location.SecretsManagerLocation"


CertificateLocation: TypeAlias = _CertificateLocation_secretsManager


# --- restJson1 ser/de ---
def serialize_json(value: CertificateLocation) -> dict:
    if "secretsManager" in value:
        import aws_sdk_bedrock_agentcore.types.secrets_manager_location

        return {
            "secretsManager": aws_sdk_bedrock_agentcore.types.secrets_manager_location.serialize_json(
                value["secretsManager"]
            )
        }
    else:
        raise SerializationError("CertificateLocation: no variant present")


def deserialize_json(data: dict) -> CertificateLocation:
    if "secretsManager" in data:
        import aws_sdk_bedrock_agentcore.types.secrets_manager_location

        return {
            "secretsManager": aws_sdk_bedrock_agentcore.types.secrets_manager_location.deserialize_json(
                data["secretsManager"]
            )
        }
    else:
        raise DeserializationError("CertificateLocation: no recognized variant key")
