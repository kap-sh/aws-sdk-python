"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#DeveloperUserIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cognito_identity.types.developer_user_identifier

DeveloperUserIdentifierList: TypeAlias = list[
    "capo_cognito_identity.types.developer_user_identifier.DeveloperUserIdentifier"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeveloperUserIdentifierList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DeveloperUserIdentifierList:
    return list(data)
