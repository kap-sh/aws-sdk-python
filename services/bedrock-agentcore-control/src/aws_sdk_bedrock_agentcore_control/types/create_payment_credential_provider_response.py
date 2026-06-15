"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreatePaymentCredentialProviderResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.credential_provider_name
    import aws_sdk_bedrock_agentcore_control.types.payment_credential_provider_arn_type
    import aws_sdk_bedrock_agentcore_control.types.payment_credential_provider_vendor_type
    import aws_sdk_bedrock_agentcore_control.types.payment_provider_configuration_output


class CreatePaymentCredentialProviderResponse(TypedDict):
    name: "aws_sdk_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName"
    """<p>The name of the created payment credential provider.</p>"""
    credential_provider_vendor: "aws_sdk_bedrock_agentcore_control.types.payment_credential_provider_vendor_type.PaymentCredentialProviderVendorType"
    """<p>The vendor type for the created payment credential provider.</p>"""
    credential_provider_arn: "aws_sdk_bedrock_agentcore_control.types.payment_credential_provider_arn_type.PaymentCredentialProviderArnType"
    """<p>The Amazon Resource Name (ARN) of the created payment credential provider.</p>"""
    provider_configuration_output: "aws_sdk_bedrock_agentcore_control.types.payment_provider_configuration_output.PaymentProviderConfigurationOutput"
    """<p>Output configuration (contains secret ARNs, excludes actual secret values).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePaymentCredentialProviderResponse) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_bedrock_agentcore_control.types.payment_credential_provider_vendor_type

    out["credentialProviderVendor"] = (
        aws_sdk_bedrock_agentcore_control.types.payment_credential_provider_vendor_type.serialize_json(
            value["credential_provider_vendor"]
        )
    )
    out["credentialProviderArn"] = value["credential_provider_arn"]
    import aws_sdk_bedrock_agentcore_control.types.payment_provider_configuration_output

    out["providerConfigurationOutput"] = (
        aws_sdk_bedrock_agentcore_control.types.payment_provider_configuration_output.serialize_json(
            value["provider_configuration_output"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreatePaymentCredentialProviderResponse:
    out: CreatePaymentCredentialProviderResponse = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "CreatePaymentCredentialProviderResponse.name required"
        )
    if "credentialProviderVendor" in data:
        import aws_sdk_bedrock_agentcore_control.types.payment_credential_provider_vendor_type

        out["credential_provider_vendor"] = (
            aws_sdk_bedrock_agentcore_control.types.payment_credential_provider_vendor_type.deserialize_json(
                data["credentialProviderVendor"]
            )
        )
    else:
        raise DeserializationError(
            "CreatePaymentCredentialProviderResponse.credential_provider_vendor required"
        )
    if "credentialProviderArn" in data:
        out["credential_provider_arn"] = data["credentialProviderArn"]
    else:
        raise DeserializationError(
            "CreatePaymentCredentialProviderResponse.credential_provider_arn required"
        )
    if "providerConfigurationOutput" in data:
        import aws_sdk_bedrock_agentcore_control.types.payment_provider_configuration_output

        out["provider_configuration_output"] = (
            aws_sdk_bedrock_agentcore_control.types.payment_provider_configuration_output.deserialize_json(
                data["providerConfigurationOutput"]
            )
        )
    else:
        raise DeserializationError(
            "CreatePaymentCredentialProviderResponse.provider_configuration_output required"
        )
    return out
