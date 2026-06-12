"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ProviderUserIdentifierType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.provider_name_type
    import aws_sdk_cognito_identity_provider.types.string_type


class ProviderUserIdentifierType(TypedDict):
    provider_name: NotRequired[
        "aws_sdk_cognito_identity_provider.types.provider_name_type.ProviderNameType"
    ]
    """<p>The name of the provider, such as Facebook, Google, or Login with Amazon.</p>"""
    provider_attribute_name: NotRequired[
        "aws_sdk_cognito_identity_provider.types.string_type.StringType"
    ]
    """<p>The name of the provider attribute to link to, such as <code>NameID</code>.</p>"""
    provider_attribute_value: NotRequired[
        "aws_sdk_cognito_identity_provider.types.string_type.StringType"
    ]
    """<p>The value of the provider attribute to link to, such as <code>xxxxx_account</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProviderUserIdentifierType) -> dict:
    out: dict = {}
    if "provider_name" in value:
        out["ProviderName"] = value["provider_name"]
    if "provider_attribute_name" in value:
        out["ProviderAttributeName"] = value["provider_attribute_name"]
    if "provider_attribute_value" in value:
        out["ProviderAttributeValue"] = value["provider_attribute_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ProviderUserIdentifierType:
    out: ProviderUserIdentifierType = {}  # type: ignore[typeddict-item]
    if "ProviderName" in data:
        out["provider_name"] = data["ProviderName"]
    if "ProviderAttributeName" in data:
        out["provider_attribute_name"] = data["ProviderAttributeName"]
    if "ProviderAttributeValue" in data:
        out["provider_attribute_value"] = data["ProviderAttributeValue"]
    return out
