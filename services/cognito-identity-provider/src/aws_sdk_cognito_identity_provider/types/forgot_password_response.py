"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ForgotPasswordResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.code_delivery_details_type


class ForgotPasswordResponse(TypedDict):
    code_delivery_details: NotRequired[
        "aws_sdk_cognito_identity_provider.types.code_delivery_details_type.CodeDeliveryDetailsType"
    ]
    """<p>Information about the phone number or email address that Amazon Cognito sent the password-recovery code to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ForgotPasswordResponse) -> dict:
    out: dict = {}
    if "code_delivery_details" in value:
        import aws_sdk_cognito_identity_provider.types.code_delivery_details_type

        out["CodeDeliveryDetails"] = (
            aws_sdk_cognito_identity_provider.types.code_delivery_details_type.serialize_aws_json_1_1(
                value["code_delivery_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ForgotPasswordResponse:
    out: ForgotPasswordResponse = {}  # type: ignore[typeddict-item]
    if "CodeDeliveryDetails" in data:
        import aws_sdk_cognito_identity_provider.types.code_delivery_details_type

        out["code_delivery_details"] = (
            aws_sdk_cognito_identity_provider.types.code_delivery_details_type.deserialize_aws_json_1_1(
                data["CodeDeliveryDetails"]
            )
        )
    return out
