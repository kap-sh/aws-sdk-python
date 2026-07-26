"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#CustomAttributesListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.schema_attribute_type

CustomAttributesListType: TypeAlias = list[
    "capo_cognito_identity_provider.types.schema_attribute_type.SchemaAttributeType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomAttributesListType) -> list:
    import capo_cognito_identity_provider.types.schema_attribute_type

    out: list = []
    for item in value:
        out.append(
            capo_cognito_identity_provider.types.schema_attribute_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CustomAttributesListType:
    import capo_cognito_identity_provider.types.schema_attribute_type

    out: CustomAttributesListType = []
    for item in data:
        out.append(
            capo_cognito_identity_provider.types.schema_attribute_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
