"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AttributeNameListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.attribute_name_type

AttributeNameListType: TypeAlias = list[
    "aws_sdk_cognito_identity_provider.types.attribute_name_type.AttributeNameType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttributeNameListType) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AttributeNameListType:
    return list(data)
