"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ResendConfirmationCodeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.code_delivery_details_type


class ResendConfirmationCodeResponse(TypedDict, closed=True):
    code_delivery_details: NotRequired[
        "aws_sdk_cognito_identity_provider.types.code_delivery_details_type.CodeDeliveryDetailsType"
    ]
    """<p>Information about the phone number or email address that Amazon Cognito sent the confirmation code to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResendConfirmationCodeResponse) -> dict:
    out: dict = {}
    if "code_delivery_details" in value:
        import aws_sdk_cognito_identity_provider.types.code_delivery_details_type

        out["CodeDeliveryDetails"] = (
            aws_sdk_cognito_identity_provider.types.code_delivery_details_type.serialize_aws_json_1_1(
                value["code_delivery_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResendConfirmationCodeResponse:
    out: ResendConfirmationCodeResponse = {}  # type: ignore[typeddict-item]
    if "CodeDeliveryDetails" in data:
        import aws_sdk_cognito_identity_provider.types.code_delivery_details_type

        out["code_delivery_details"] = (
            aws_sdk_cognito_identity_provider.types.code_delivery_details_type.deserialize_aws_json_1_1(
                data["CodeDeliveryDetails"]
            )
        )
    return out
