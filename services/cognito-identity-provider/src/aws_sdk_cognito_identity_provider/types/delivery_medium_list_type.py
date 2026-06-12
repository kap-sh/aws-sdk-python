"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DeliveryMediumListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.delivery_medium_type

DeliveryMediumListType: TypeAlias = list[
    "aws_sdk_cognito_identity_provider.types.delivery_medium_type.DeliveryMediumType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeliveryMediumListType) -> list:
    import aws_sdk_cognito_identity_provider.types.delivery_medium_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cognito_identity_provider.types.delivery_medium_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DeliveryMediumListType:
    import aws_sdk_cognito_identity_provider.types.delivery_medium_type

    out: DeliveryMediumListType = []
    for item in data:
        out.append(
            aws_sdk_cognito_identity_provider.types.delivery_medium_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
