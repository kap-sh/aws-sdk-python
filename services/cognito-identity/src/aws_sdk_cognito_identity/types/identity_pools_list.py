"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#IdentityPoolsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cognito_identity.types.identity_pool_short_description

IdentityPoolsList: TypeAlias = list[
    "aws_sdk_cognito_identity.types.identity_pool_short_description.IdentityPoolShortDescription"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IdentityPoolsList) -> list:
    import aws_sdk_cognito_identity.types.identity_pool_short_description

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cognito_identity.types.identity_pool_short_description.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> IdentityPoolsList:
    import aws_sdk_cognito_identity.types.identity_pool_short_description

    out: IdentityPoolsList = []
    for item in data:
        out.append(
            aws_sdk_cognito_identity.types.identity_pool_short_description.deserialize_aws_json_1_1(
                item
            )
        )
    return out
