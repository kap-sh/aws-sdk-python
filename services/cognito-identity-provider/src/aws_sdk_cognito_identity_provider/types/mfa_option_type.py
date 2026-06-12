"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#MFAOptionType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.attribute_name_type
    import aws_sdk_cognito_identity_provider.types.delivery_medium_type


class MFAOptionType(TypedDict):
    delivery_medium: NotRequired[
        "aws_sdk_cognito_identity_provider.types.delivery_medium_type.DeliveryMediumType"
    ]
    """<p>The delivery medium to send the MFA code. You can use this parameter to set only the <code>SMS</code> delivery medium value.</p>"""
    attribute_name: NotRequired[
        "aws_sdk_cognito_identity_provider.types.attribute_name_type.AttributeNameType"
    ]
    """<p>The attribute name of the MFA option type. The only valid value is <code>phone_number</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MFAOptionType) -> dict:
    out: dict = {}
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


def deserialize_aws_json_1_1(data: dict) -> MFAOptionType:
    out: MFAOptionType = {}  # type: ignore[typeddict-item]
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
