"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#CallbackURLsListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.redirect_url_type

CallbackURLsListType: TypeAlias = list[
    "capo_cognito_identity_provider.types.redirect_url_type.RedirectUrlType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CallbackURLsListType) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> CallbackURLsListType:
    return list(data)
