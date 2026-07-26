"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#TermsDescriptionListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.terms_description_type

TermsDescriptionListType: TypeAlias = list[
    "capo_cognito_identity_provider.types.terms_description_type.TermsDescriptionType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TermsDescriptionListType) -> list:
    import capo_cognito_identity_provider.types.terms_description_type

    out: list = []
    for item in value:
        out.append(
            capo_cognito_identity_provider.types.terms_description_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TermsDescriptionListType:
    import capo_cognito_identity_provider.types.terms_description_type

    out: TermsDescriptionListType = []
    for item in data:
        out.append(
            capo_cognito_identity_provider.types.terms_description_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
