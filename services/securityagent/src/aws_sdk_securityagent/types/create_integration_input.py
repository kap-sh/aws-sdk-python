"""Generated from Smithy shape ``com.amazonaws.securityagent#CreateIntegrationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.kms_key_id
    import aws_sdk_securityagent.types.provider
    import aws_sdk_securityagent.types.provider_input
    import aws_sdk_securityagent.types.tag_map


class CreateIntegrationInput(TypedDict, closed=True):
    provider: "aws_sdk_securityagent.types.provider.Provider"
    """<p>The integration provider. Currently, only GITHUB is supported.</p>"""
    input: "aws_sdk_securityagent.types.provider_input.ProviderInput"
    """<p>The provider-specific input required to create the integration.</p>"""
    integration_display_name: "str"
    """<p>The display name for the integration.</p>"""
    kms_key_id: NotRequired["aws_sdk_securityagent.types.kms_key_id.KmsKeyId"]
    """<p>The identifier of the AWS KMS key to use for encrypting data associated with the integration.</p>"""
    tags: NotRequired["aws_sdk_securityagent.types.tag_map.TagMap"]
    """<p>The tags to associate with the integration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateIntegrationInput) -> dict:
    out: dict = {}
    import aws_sdk_securityagent.types.provider

    out["provider"] = aws_sdk_securityagent.types.provider.serialize_json(
        value["provider"]
    )
    import aws_sdk_securityagent.types.provider_input

    out["input"] = aws_sdk_securityagent.types.provider_input.serialize_json(
        value["input"]
    )
    out["integrationDisplayName"] = value["integration_display_name"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "tags" in value:
        import aws_sdk_securityagent.types.tag_map

        out["tags"] = aws_sdk_securityagent.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateIntegrationInput:
    out: CreateIntegrationInput = {}  # type: ignore[typeddict-item]
    if "provider" in data:
        import aws_sdk_securityagent.types.provider

        out["provider"] = aws_sdk_securityagent.types.provider.deserialize_json(
            data["provider"]
        )
    else:
        raise DeserializationError("CreateIntegrationInput.provider required")
    if "input" in data:
        import aws_sdk_securityagent.types.provider_input

        out["input"] = aws_sdk_securityagent.types.provider_input.deserialize_json(
            data["input"]
        )
    else:
        raise DeserializationError("CreateIntegrationInput.input required")
    if "integrationDisplayName" in data:
        out["integration_display_name"] = data["integrationDisplayName"]
    else:
        raise DeserializationError(
            "CreateIntegrationInput.integration_display_name required"
        )
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    if "tags" in data:
        import aws_sdk_securityagent.types.tag_map

        out["tags"] = aws_sdk_securityagent.types.tag_map.deserialize_json(data["tags"])
    return out
