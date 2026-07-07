"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ConfirmDeviceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.boolean_type


class ConfirmDeviceResponse(TypedDict, closed=True):
    user_confirmation_necessary: (
        "aws_sdk_cognito_identity_provider.types.boolean_type.BooleanType"
    )
    """<p>When <code>true</code>, your user must confirm that they want to remember the device. Prompt the user for an answer.</p> <p>When <code>false</code>, immediately sets the device as remembered and eligible for device authentication.</p> <p>You can configure your user pool to always remember devices, in which case this response is <code>false</code>, or to allow users to opt in, in which case this response is <code>true</code>. Configure this option under <i>Device tracking</i> in the <i>Sign-in</i> menu of your user pool.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfirmDeviceResponse) -> dict:
    out: dict = {}
    out["UserConfirmationNecessary"] = value.get("user_confirmation_necessary", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> ConfirmDeviceResponse:
    out: ConfirmDeviceResponse = {}  # type: ignore[typeddict-item]
    if "UserConfirmationNecessary" in data:
        out["user_confirmation_necessary"] = data["UserConfirmationNecessary"]
    else:
        out["user_confirmation_necessary"] = False
    return out
