"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#CodeDeliveryDetailsListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.code_delivery_details_type

CodeDeliveryDetailsListType: TypeAlias = list[
    "capo_cognito_identity_provider.types.code_delivery_details_type.CodeDeliveryDetailsType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CodeDeliveryDetailsListType) -> list:
    import capo_cognito_identity_provider.types.code_delivery_details_type

    out: list = []
    for item in value:
        out.append(
            capo_cognito_identity_provider.types.code_delivery_details_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CodeDeliveryDetailsListType:
    import capo_cognito_identity_provider.types.code_delivery_details_type

    out: CodeDeliveryDetailsListType = []
    for item in data:
        out.append(
            capo_cognito_identity_provider.types.code_delivery_details_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
