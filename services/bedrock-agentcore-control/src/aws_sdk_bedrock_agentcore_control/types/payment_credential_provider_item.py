"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PaymentCredentialProviderItem``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_bedrock_agentcore_control.types.credential_provider_name
    import aws_sdk_bedrock_agentcore_control.types.payment_credential_provider_arn_type
    import aws_sdk_bedrock_agentcore_control.types.payment_credential_provider_vendor_type


class PaymentCredentialProviderItem(TypedDict):
    name: "aws_sdk_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName"
    """<p>The name of the payment credential provider.</p>"""
    credential_provider_vendor: "aws_sdk_bedrock_agentcore_control.types.payment_credential_provider_vendor_type.PaymentCredentialProviderVendorType"
    """<p>The vendor type for the payment credential provider.</p>"""
    credential_provider_arn: "aws_sdk_bedrock_agentcore_control.types.payment_credential_provider_arn_type.PaymentCredentialProviderArnType"
    """<p>The Amazon Resource Name (ARN) of the payment credential provider.</p>"""
    created_time: "datetime.datetime"
    """<p>The timestamp when the payment credential provider was created.</p>"""
    last_updated_time: "datetime.datetime"
    """<p>The timestamp when the payment credential provider was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PaymentCredentialProviderItem) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_bedrock_agentcore_control.types.payment_credential_provider_vendor_type

    out["credentialProviderVendor"] = (
        aws_sdk_bedrock_agentcore_control.types.payment_credential_provider_vendor_type.serialize_json(
            value["credential_provider_vendor"]
        )
    )
    out["credentialProviderArn"] = value["credential_provider_arn"]
    import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp

    out["createdTime"] = (
        aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["created_time"]
        )
    )
    import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp

    out["lastUpdatedTime"] = (
        aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["last_updated_time"]
        )
    )
    return out


def deserialize_json(data: dict) -> PaymentCredentialProviderItem:
    out: PaymentCredentialProviderItem = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("PaymentCredentialProviderItem.name required")
    if "credentialProviderVendor" in data:
        import aws_sdk_bedrock_agentcore_control.types.payment_credential_provider_vendor_type

        out["credential_provider_vendor"] = (
            aws_sdk_bedrock_agentcore_control.types.payment_credential_provider_vendor_type.deserialize_json(
                data["credentialProviderVendor"]
            )
        )
    else:
        raise DeserializationError(
            "PaymentCredentialProviderItem.credential_provider_vendor required"
        )
    if "credentialProviderArn" in data:
        out["credential_provider_arn"] = data["credentialProviderArn"]
    else:
        raise DeserializationError(
            "PaymentCredentialProviderItem.credential_provider_arn required"
        )
    if "createdTime" in data:
        import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp

        out["created_time"] = (
            aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["createdTime"]
            )
        )
    else:
        raise DeserializationError(
            "PaymentCredentialProviderItem.created_time required"
        )
    if "lastUpdatedTime" in data:
        import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp

        out["last_updated_time"] = (
            aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["lastUpdatedTime"]
            )
        )
    else:
        raise DeserializationError(
            "PaymentCredentialProviderItem.last_updated_time required"
        )
    return out
