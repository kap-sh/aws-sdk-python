"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ReplicaRegionsType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.string_type

ReplicaRegionsType: TypeAlias = list[
    "aws_sdk_cognito_identity_provider.types.string_type.StringType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicaRegionsType) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ReplicaRegionsType:
    return list(data)
