"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AttributeListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.attribute_type

AttributeListType: TypeAlias = list[
    "aws_sdk_cognito_identity_provider.types.attribute_type.AttributeType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttributeListType) -> list:
    import aws_sdk_cognito_identity_provider.types.attribute_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cognito_identity_provider.types.attribute_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AttributeListType:
    import aws_sdk_cognito_identity_provider.types.attribute_type

    out: AttributeListType = []
    for item in data:
        out.append(
            aws_sdk_cognito_identity_provider.types.attribute_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
