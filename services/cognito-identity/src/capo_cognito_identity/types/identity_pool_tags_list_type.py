"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#IdentityPoolTagsListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cognito_identity.types.tag_keys_type

IdentityPoolTagsListType: TypeAlias = list[
    "capo_cognito_identity.types.tag_keys_type.TagKeysType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IdentityPoolTagsListType) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> IdentityPoolTagsListType:
    return list(data)
