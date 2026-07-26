"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AttributesRequireVerificationBeforeUpdateType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.verified_attribute_type

AttributesRequireVerificationBeforeUpdateType: TypeAlias = list[
    "capo_cognito_identity_provider.types.verified_attribute_type.VerifiedAttributeType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: AttributesRequireVerificationBeforeUpdateType,
) -> list:
    import capo_cognito_identity_provider.types.verified_attribute_type

    out: list = []
    for item in value:
        out.append(
            capo_cognito_identity_provider.types.verified_attribute_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: list,
) -> AttributesRequireVerificationBeforeUpdateType:
    import capo_cognito_identity_provider.types.verified_attribute_type

    out: AttributesRequireVerificationBeforeUpdateType = []
    for item in data:
        out.append(
            capo_cognito_identity_provider.types.verified_attribute_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
