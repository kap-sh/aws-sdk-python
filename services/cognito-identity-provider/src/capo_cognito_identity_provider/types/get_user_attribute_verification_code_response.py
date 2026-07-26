"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#GetUserAttributeVerificationCodeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.code_delivery_details_type


class GetUserAttributeVerificationCodeResponse(TypedDict, closed=True):
    code_delivery_details: NotRequired[
        "capo_cognito_identity_provider.types.code_delivery_details_type.CodeDeliveryDetailsType"
    ]
    """<p>Information about the delivery destination of the user attribute verification code.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetUserAttributeVerificationCodeResponse) -> dict:
    out: dict = {}
    if "code_delivery_details" in value:
        import capo_cognito_identity_provider.types.code_delivery_details_type

        out["CodeDeliveryDetails"] = (
            capo_cognito_identity_provider.types.code_delivery_details_type.serialize_aws_json_1_1(
                value["code_delivery_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetUserAttributeVerificationCodeResponse:
    out: GetUserAttributeVerificationCodeResponse = {}  # type: ignore[typeddict-item]
    if "CodeDeliveryDetails" in data:
        import capo_cognito_identity_provider.types.code_delivery_details_type

        out["code_delivery_details"] = (
            capo_cognito_identity_provider.types.code_delivery_details_type.deserialize_aws_json_1_1(
                data["CodeDeliveryDetails"]
            )
        )
    return out
