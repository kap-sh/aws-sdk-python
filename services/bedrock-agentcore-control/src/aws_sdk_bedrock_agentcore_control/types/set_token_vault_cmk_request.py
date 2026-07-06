"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#SetTokenVaultCMKRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.kms_configuration
    import aws_sdk_bedrock_agentcore_control.types.token_vault_id_type


class SetTokenVaultCMKRequest(TypedDict, closed=True):
    token_vault_id: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.token_vault_id_type.TokenVaultIdType"
    ]
    """<p>The unique identifier of the token vault to update.</p>"""
    kms_configuration: (
        "aws_sdk_bedrock_agentcore_control.types.kms_configuration.KmsConfiguration"
    )
    """<p>The KMS configuration for the token vault, including the key type and KMS key ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SetTokenVaultCMKRequest) -> dict:
    out: dict = {}
    if "token_vault_id" in value:
        out["tokenVaultId"] = value["token_vault_id"]
    import aws_sdk_bedrock_agentcore_control.types.kms_configuration

    out["kmsConfiguration"] = (
        aws_sdk_bedrock_agentcore_control.types.kms_configuration.serialize_json(
            value["kms_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> SetTokenVaultCMKRequest:
    out: SetTokenVaultCMKRequest = {}  # type: ignore[typeddict-item]
    if "tokenVaultId" in data:
        out["token_vault_id"] = data["tokenVaultId"]
    if "kmsConfiguration" in data:
        import aws_sdk_bedrock_agentcore_control.types.kms_configuration

        out["kms_configuration"] = (
            aws_sdk_bedrock_agentcore_control.types.kms_configuration.deserialize_json(
                data["kmsConfiguration"]
            )
        )
    else:
        raise DeserializationError("SetTokenVaultCMKRequest.kms_configuration required")
    return out
