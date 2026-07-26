"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#OIDCProviderList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cognito_identity.types.arn_string

OIDCProviderList: TypeAlias = list["capo_cognito_identity.types.arn_string.ARNString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OIDCProviderList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> OIDCProviderList:
    return list(data)
