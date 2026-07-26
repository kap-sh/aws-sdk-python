"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#LogoutURLsListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.redirect_url_type

LogoutURLsListType: TypeAlias = list[
    "capo_cognito_identity_provider.types.redirect_url_type.RedirectUrlType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogoutURLsListType) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> LogoutURLsListType:
    return list(data)
