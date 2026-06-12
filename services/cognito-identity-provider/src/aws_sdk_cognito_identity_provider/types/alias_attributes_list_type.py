"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AliasAttributesListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.alias_attribute_type

AliasAttributesListType: TypeAlias = list[
    "aws_sdk_cognito_identity_provider.types.alias_attribute_type.AliasAttributeType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AliasAttributesListType) -> list:
    import aws_sdk_cognito_identity_provider.types.alias_attribute_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cognito_identity_provider.types.alias_attribute_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AliasAttributesListType:
    import aws_sdk_cognito_identity_provider.types.alias_attribute_type

    out: AliasAttributesListType = []
    for item in data:
        out.append(
            aws_sdk_cognito_identity_provider.types.alias_attribute_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
