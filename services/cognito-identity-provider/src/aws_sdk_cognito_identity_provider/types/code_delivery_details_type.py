"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#CodeDeliveryDetailsType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.attribute_name_type
    import aws_sdk_cognito_identity_provider.types.delivery_medium_type
    import aws_sdk_cognito_identity_provider.types.string_type


class CodeDeliveryDetailsType(TypedDict, closed=True):
    destination: NotRequired[
        "aws_sdk_cognito_identity_provider.types.string_type.StringType"
    ]
    """<p>The email address or phone number destination where Amazon Cognito sent the code.</p>"""
    delivery_medium: NotRequired[
        "aws_sdk_cognito_identity_provider.types.delivery_medium_type.DeliveryMediumType"
    ]
    """<p>The method that Amazon Cognito used to send the code.</p>"""
    attribute_name: NotRequired[
        "aws_sdk_cognito_identity_provider.types.attribute_name_type.AttributeNameType"
    ]
    """<p>The name of the attribute that Amazon Cognito verifies with the code.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CodeDeliveryDetailsType) -> dict:
    out: dict = {}
    if "destination" in value:
        out["Destination"] = value["destination"]
    if "delivery_medium" in value:
        import aws_sdk_cognito_identity_provider.types.delivery_medium_type

        out["DeliveryMedium"] = (
            aws_sdk_cognito_identity_provider.types.delivery_medium_type.serialize_aws_json_1_1(
                value["delivery_medium"]
            )
        )
    if "attribute_name" in value:
        out["AttributeName"] = value["attribute_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CodeDeliveryDetailsType:
    out: CodeDeliveryDetailsType = {}  # type: ignore[typeddict-item]
    if "Destination" in data:
        out["destination"] = data["Destination"]
    if "DeliveryMedium" in data:
        import aws_sdk_cognito_identity_provider.types.delivery_medium_type

        out["delivery_medium"] = (
            aws_sdk_cognito_identity_provider.types.delivery_medium_type.deserialize_aws_json_1_1(
                data["DeliveryMedium"]
            )
        )
    if "AttributeName" in data:
        out["attribute_name"] = data["AttributeName"]
    return out
