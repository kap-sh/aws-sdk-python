"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#UnprocessedIdentityIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cognito_identity.types.unprocessed_identity_id

UnprocessedIdentityIdList: TypeAlias = list[
    "aws_sdk_cognito_identity.types.unprocessed_identity_id.UnprocessedIdentityId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnprocessedIdentityIdList) -> list:
    import aws_sdk_cognito_identity.types.unprocessed_identity_id

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cognito_identity.types.unprocessed_identity_id.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> UnprocessedIdentityIdList:
    import aws_sdk_cognito_identity.types.unprocessed_identity_id

    out: UnprocessedIdentityIdList = []
    for item in data:
        out.append(
            aws_sdk_cognito_identity.types.unprocessed_identity_id.deserialize_aws_json_1_1(
                item
            )
        )
    return out
