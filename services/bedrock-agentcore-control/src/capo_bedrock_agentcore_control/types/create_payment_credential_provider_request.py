"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreatePaymentCredentialProviderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.credential_provider_name
    import capo_bedrock_agentcore_control.types.payment_credential_provider_vendor_type
    import capo_bedrock_agentcore_control.types.payment_provider_configuration_input
    import capo_bedrock_agentcore_control.types.tags_map


class CreatePaymentCredentialProviderRequest(TypedDict, closed=True):
    name: "capo_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName"
    """<p>Unique name for the payment credential provider.</p>"""
    credential_provider_vendor: "capo_bedrock_agentcore_control.types.payment_credential_provider_vendor_type.PaymentCredentialProviderVendorType"
    """<p>The vendor type for the payment credential provider (e.g., CoinbaseCDP, StripePrivy).</p>"""
    provider_configuration_input: "capo_bedrock_agentcore_control.types.payment_provider_configuration_input.PaymentProviderConfigurationInput"
    """<p>Configuration specific to the vendor, including API credentials.</p>"""
    tags: NotRequired["capo_bedrock_agentcore_control.types.tags_map.TagsMap"]
    """<p>Optional tags for resource organization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePaymentCredentialProviderRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_bedrock_agentcore_control.types.payment_credential_provider_vendor_type

    out["credentialProviderVendor"] = (
        capo_bedrock_agentcore_control.types.payment_credential_provider_vendor_type.serialize_json(
            value["credential_provider_vendor"]
        )
    )
    import capo_bedrock_agentcore_control.types.payment_provider_configuration_input

    out["providerConfigurationInput"] = (
        capo_bedrock_agentcore_control.types.payment_provider_configuration_input.serialize_json(
            value["provider_configuration_input"]
        )
    )
    if "tags" in value:
        import capo_bedrock_agentcore_control.types.tags_map

        out["tags"] = capo_bedrock_agentcore_control.types.tags_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreatePaymentCredentialProviderRequest:
    out: CreatePaymentCredentialProviderRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "CreatePaymentCredentialProviderRequest.name required"
        )
    if "credentialProviderVendor" in data:
        import capo_bedrock_agentcore_control.types.payment_credential_provider_vendor_type

        out["credential_provider_vendor"] = (
            capo_bedrock_agentcore_control.types.payment_credential_provider_vendor_type.deserialize_json(
                data["credentialProviderVendor"]
            )
        )
    else:
        raise DeserializationError(
            "CreatePaymentCredentialProviderRequest.credential_provider_vendor required"
        )
    if "providerConfigurationInput" in data:
        import capo_bedrock_agentcore_control.types.payment_provider_configuration_input

        out["provider_configuration_input"] = (
            capo_bedrock_agentcore_control.types.payment_provider_configuration_input.deserialize_json(
                data["providerConfigurationInput"]
            )
        )
    else:
        raise DeserializationError(
            "CreatePaymentCredentialProviderRequest.provider_configuration_input required"
        )
    if "tags" in data:
        import capo_bedrock_agentcore_control.types.tags_map

        out["tags"] = capo_bedrock_agentcore_control.types.tags_map.deserialize_json(
            data["tags"]
        )
    return out
