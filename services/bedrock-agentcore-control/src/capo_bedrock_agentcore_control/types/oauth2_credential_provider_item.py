"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#Oauth2CredentialProviderItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore_control.types.credential_provider_arn_type
    import capo_bedrock_agentcore_control.types.credential_provider_name
    import capo_bedrock_agentcore_control.types.credential_provider_vendor_type


class Oauth2CredentialProviderItem(TypedDict, closed=True):
    name: "capo_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName"
    """<p>The name of the OAuth2 credential provider.</p>"""
    credential_provider_vendor: "capo_bedrock_agentcore_control.types.credential_provider_vendor_type.CredentialProviderVendorType"
    """<p>The vendor of the OAuth2 credential provider.</p>"""
    credential_provider_arn: "capo_bedrock_agentcore_control.types.credential_provider_arn_type.CredentialProviderArnType"
    """<p>The Amazon Resource Name (ARN) of the OAuth2 credential provider.</p>"""
    created_time: "datetime.datetime"
    """<p>The timestamp when the OAuth2 credential provider was created.</p>"""
    last_updated_time: "datetime.datetime"
    """<p>The timestamp when the OAuth2 credential provider was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Oauth2CredentialProviderItem) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_bedrock_agentcore_control.types.credential_provider_vendor_type

    out["credentialProviderVendor"] = (
        capo_bedrock_agentcore_control.types.credential_provider_vendor_type.serialize_json(
            value["credential_provider_vendor"]
        )
    )
    out["credentialProviderArn"] = value["credential_provider_arn"]
    import capo_bedrock_agentcore_control.types._prelude.timestamp

    out["createdTime"] = (
        capo_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["created_time"]
        )
    )
    import capo_bedrock_agentcore_control.types._prelude.timestamp

    out["lastUpdatedTime"] = (
        capo_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["last_updated_time"]
        )
    )
    return out


def deserialize_json(data: dict) -> Oauth2CredentialProviderItem:
    out: Oauth2CredentialProviderItem = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("Oauth2CredentialProviderItem.name required")
    if data.get("credentialProviderVendor") is not None:
        import capo_bedrock_agentcore_control.types.credential_provider_vendor_type

        out["credential_provider_vendor"] = (
            capo_bedrock_agentcore_control.types.credential_provider_vendor_type.deserialize_json(
                data["credentialProviderVendor"]
            )
        )
    else:
        raise DeserializationError(
            "Oauth2CredentialProviderItem.credential_provider_vendor required"
        )
    if data.get("credentialProviderArn") is not None:
        out["credential_provider_arn"] = data["credentialProviderArn"]
    else:
        raise DeserializationError(
            "Oauth2CredentialProviderItem.credential_provider_arn required"
        )
    if data.get("createdTime") is not None:
        import capo_bedrock_agentcore_control.types._prelude.timestamp

        out["created_time"] = (
            capo_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["createdTime"]
            )
        )
    else:
        raise DeserializationError("Oauth2CredentialProviderItem.created_time required")
    if data.get("lastUpdatedTime") is not None:
        import capo_bedrock_agentcore_control.types._prelude.timestamp

        out["last_updated_time"] = (
            capo_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["lastUpdatedTime"]
            )
        )
    else:
        raise DeserializationError(
            "Oauth2CredentialProviderItem.last_updated_time required"
        )
    return out
