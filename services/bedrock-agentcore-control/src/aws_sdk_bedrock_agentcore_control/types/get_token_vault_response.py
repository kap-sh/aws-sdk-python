"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetTokenVaultResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_bedrock_agentcore_control.types.kms_configuration
    import aws_sdk_bedrock_agentcore_control.types.token_vault_id_type


class GetTokenVaultResponse(TypedDict, closed=True):
    token_vault_id: (
        "aws_sdk_bedrock_agentcore_control.types.token_vault_id_type.TokenVaultIdType"
    )
    """<p>The ID of the token vault.</p>"""
    kms_configuration: (
        "aws_sdk_bedrock_agentcore_control.types.kms_configuration.KmsConfiguration"
    )
    """<p>The KMS configuration for the token vault.</p>"""
    last_modified_date: "datetime.datetime"
    """<p>The timestamp when the token vault was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTokenVaultResponse) -> dict:
    out: dict = {}
    out["tokenVaultId"] = value["token_vault_id"]
    import aws_sdk_bedrock_agentcore_control.types.kms_configuration

    out["kmsConfiguration"] = (
        aws_sdk_bedrock_agentcore_control.types.kms_configuration.serialize_json(
            value["kms_configuration"]
        )
    )
    import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp

    out["lastModifiedDate"] = (
        aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["last_modified_date"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetTokenVaultResponse:
    out: GetTokenVaultResponse = {}  # type: ignore[typeddict-item]
    if "tokenVaultId" in data:
        out["token_vault_id"] = data["tokenVaultId"]
    else:
        raise DeserializationError("GetTokenVaultResponse.token_vault_id required")
    if "kmsConfiguration" in data:
        import aws_sdk_bedrock_agentcore_control.types.kms_configuration

        out["kms_configuration"] = (
            aws_sdk_bedrock_agentcore_control.types.kms_configuration.deserialize_json(
                data["kmsConfiguration"]
            )
        )
    else:
        raise DeserializationError("GetTokenVaultResponse.kms_configuration required")
    if "lastModifiedDate" in data:
        import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp

        out["last_modified_date"] = (
            aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["lastModifiedDate"]
            )
        )
    else:
        raise DeserializationError("GetTokenVaultResponse.last_modified_date required")
    return out
