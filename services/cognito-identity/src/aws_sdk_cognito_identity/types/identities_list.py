"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#IdentitiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cognito_identity.types.identity_description

IdentitiesList: TypeAlias = list[
    "aws_sdk_cognito_identity.types.identity_description.IdentityDescription"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IdentitiesList) -> list:
    import aws_sdk_cognito_identity.types.identity_description

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cognito_identity.types.identity_description.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> IdentitiesList:
    import aws_sdk_cognito_identity.types.identity_description

    out: IdentitiesList = []
    for item in data:
        out.append(
            aws_sdk_cognito_identity.types.identity_description.deserialize_aws_json_1_1(
                item
            )
        )
    return out
