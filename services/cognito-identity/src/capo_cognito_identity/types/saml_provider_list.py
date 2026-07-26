"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#SAMLProviderList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cognito_identity.types.arn_string

SAMLProviderList: TypeAlias = list["capo_cognito_identity.types.arn_string.ARNString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SAMLProviderList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SAMLProviderList:
    return list(data)
