"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#IdentityIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cognito_identity.types.identity_id

IdentityIdList: TypeAlias = list["capo_cognito_identity.types.identity_id.IdentityId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IdentityIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> IdentityIdList:
    return list(data)
