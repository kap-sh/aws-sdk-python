"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#TermsDescriptionListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.terms_description_type

TermsDescriptionListType: TypeAlias = list[
    "aws_sdk_cognito_identity_provider.types.terms_description_type.TermsDescriptionType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TermsDescriptionListType) -> list:
    import aws_sdk_cognito_identity_provider.types.terms_description_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cognito_identity_provider.types.terms_description_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TermsDescriptionListType:
    import aws_sdk_cognito_identity_provider.types.terms_description_type

    out: TermsDescriptionListType = []
    for item in data:
        out.append(
            aws_sdk_cognito_identity_provider.types.terms_description_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
