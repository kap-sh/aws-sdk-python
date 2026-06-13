"""Generated from Smithy shape ``com.amazonaws.securityagent#GetIntegrationOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.integration_id
    import aws_sdk_securityagent.types.kms_key_id
    import aws_sdk_securityagent.types.provider
    import aws_sdk_securityagent.types.provider_type


class GetIntegrationOutput(TypedDict):
    integration_id: "aws_sdk_securityagent.types.integration_id.IntegrationId"
    """<p>The unique identifier of the integration.</p>"""
    installation_id: "str"
    """<p>The installation identifier from the integration provider.</p>"""
    provider: "aws_sdk_securityagent.types.provider.Provider"
    """<p>The integration provider.</p>"""
    provider_type: "aws_sdk_securityagent.types.provider_type.ProviderType"
    """<p>The type of the integration provider.</p>"""
    display_name: NotRequired["str"]
    """<p>The display name of the integration.</p>"""
    kms_key_id: NotRequired["aws_sdk_securityagent.types.kms_key_id.KmsKeyId"]
    """<p>The identifier of the AWS KMS key used to encrypt data associated with the integration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIntegrationOutput) -> dict:
    out: dict = {}
    out["integrationId"] = value["integration_id"]
    out["installationId"] = value["installation_id"]
    import aws_sdk_securityagent.types.provider

    out["provider"] = aws_sdk_securityagent.types.provider.serialize_json(
        value["provider"]
    )
    import aws_sdk_securityagent.types.provider_type

    out["providerType"] = aws_sdk_securityagent.types.provider_type.serialize_json(
        value["provider_type"]
    )
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_json(data: dict) -> GetIntegrationOutput:
    out: GetIntegrationOutput = {}  # type: ignore[typeddict-item]
    if "integrationId" in data:
        out["integration_id"] = data["integrationId"]
    else:
        raise DeserializationError("GetIntegrationOutput.integration_id required")
    if "installationId" in data:
        out["installation_id"] = data["installationId"]
    else:
        raise DeserializationError("GetIntegrationOutput.installation_id required")
    if "provider" in data:
        import aws_sdk_securityagent.types.provider

        out["provider"] = aws_sdk_securityagent.types.provider.deserialize_json(
            data["provider"]
        )
    else:
        raise DeserializationError("GetIntegrationOutput.provider required")
    if "providerType" in data:
        import aws_sdk_securityagent.types.provider_type

        out["provider_type"] = (
            aws_sdk_securityagent.types.provider_type.deserialize_json(
                data["providerType"]
            )
        )
    else:
        raise DeserializationError("GetIntegrationOutput.provider_type required")
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    return out
