"""Generated from Smithy shape ``com.amazonaws.securityagent#IntegrationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.provider
    import aws_sdk_securityagent.types.provider_type


class IntegrationSummary(TypedDict, closed=True):
    integration_id: "str"
    """<p>The unique identifier of the integration.</p>"""
    installation_id: "str"
    """<p>The installation identifier from the integration provider.</p>"""
    provider: "aws_sdk_securityagent.types.provider.Provider"
    """<p>The integration provider.</p>"""
    provider_type: "aws_sdk_securityagent.types.provider_type.ProviderType"
    """<p>The type of the integration provider.</p>"""
    display_name: "str"
    """<p>The display name of the integration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntegrationSummary) -> dict:
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
    out["displayName"] = value["display_name"]
    return out


def deserialize_json(data: dict) -> IntegrationSummary:
    out: IntegrationSummary = {}  # type: ignore[typeddict-item]
    if "integrationId" in data:
        out["integration_id"] = data["integrationId"]
    else:
        raise DeserializationError("IntegrationSummary.integration_id required")
    if "installationId" in data:
        out["installation_id"] = data["installationId"]
    else:
        raise DeserializationError("IntegrationSummary.installation_id required")
    if "provider" in data:
        import aws_sdk_securityagent.types.provider

        out["provider"] = aws_sdk_securityagent.types.provider.deserialize_json(
            data["provider"]
        )
    else:
        raise DeserializationError("IntegrationSummary.provider required")
    if "providerType" in data:
        import aws_sdk_securityagent.types.provider_type

        out["provider_type"] = (
            aws_sdk_securityagent.types.provider_type.deserialize_json(
                data["providerType"]
            )
        )
    else:
        raise DeserializationError("IntegrationSummary.provider_type required")
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    else:
        raise DeserializationError("IntegrationSummary.display_name required")
    return out
