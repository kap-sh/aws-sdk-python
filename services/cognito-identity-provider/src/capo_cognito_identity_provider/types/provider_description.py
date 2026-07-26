"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ProviderDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.date_type
    import capo_cognito_identity_provider.types.identity_provider_type_type
    import capo_cognito_identity_provider.types.provider_name_type


class ProviderDescription(TypedDict, closed=True):
    provider_name: NotRequired[
        "capo_cognito_identity_provider.types.provider_name_type.ProviderNameType"
    ]
    """<p>The name of the IdP, for example <code>MySAMLProvider</code>.</p>"""
    provider_type: NotRequired[
        "capo_cognito_identity_provider.types.identity_provider_type_type.IdentityProviderTypeType"
    ]
    """<p>The type of the provider, for example <code>SAML</code>. Amazon Cognito supports SAML 2.0, OIDC, and social IdPs. User pools list supported social IdPs by name in this response parameter: Facebook, Google, Login with Amazon, and Sign in with Apple.</p>"""
    last_modified_date: NotRequired[
        "capo_cognito_identity_provider.types.date_type.DateType"
    ]
    """<p>The date and time when the item was modified. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java <code>Date</code> object.</p>"""
    creation_date: NotRequired[
        "capo_cognito_identity_provider.types.date_type.DateType"
    ]
    """<p>The date and time when the item was created. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java <code>Date</code> object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProviderDescription) -> dict:
    out: dict = {}
    if "provider_name" in value:
        out["ProviderName"] = value["provider_name"]
    if "provider_type" in value:
        import capo_cognito_identity_provider.types.identity_provider_type_type

        out["ProviderType"] = (
            capo_cognito_identity_provider.types.identity_provider_type_type.serialize_aws_json_1_1(
                value["provider_type"]
            )
        )
    if "last_modified_date" in value:
        import capo_cognito_identity_provider.types.date_type

        out["LastModifiedDate"] = (
            capo_cognito_identity_provider.types.date_type.serialize_aws_json_1_1(
                value["last_modified_date"]
            )
        )
    if "creation_date" in value:
        import capo_cognito_identity_provider.types.date_type

        out["CreationDate"] = (
            capo_cognito_identity_provider.types.date_type.serialize_aws_json_1_1(
                value["creation_date"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProviderDescription:
    out: ProviderDescription = {}  # type: ignore[typeddict-item]
    if "ProviderName" in data:
        out["provider_name"] = data["ProviderName"]
    if "ProviderType" in data:
        import capo_cognito_identity_provider.types.identity_provider_type_type

        out["provider_type"] = (
            capo_cognito_identity_provider.types.identity_provider_type_type.deserialize_aws_json_1_1(
                data["ProviderType"]
            )
        )
    if "LastModifiedDate" in data:
        import capo_cognito_identity_provider.types.date_type

        out["last_modified_date"] = (
            capo_cognito_identity_provider.types.date_type.deserialize_aws_json_1_1(
                data["LastModifiedDate"]
            )
        )
    if "CreationDate" in data:
        import capo_cognito_identity_provider.types.date_type

        out["creation_date"] = (
            capo_cognito_identity_provider.types.date_type.deserialize_aws_json_1_1(
                data["CreationDate"]
            )
        )
    return out
