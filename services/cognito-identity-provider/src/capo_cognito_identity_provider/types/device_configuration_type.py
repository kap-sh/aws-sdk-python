"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DeviceConfigurationType``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.boolean_type


class DeviceConfigurationType(TypedDict, closed=True):
    challenge_required_on_new_device: (
        "capo_cognito_identity_provider.types.boolean_type.BooleanType"
    )
    """<p>When true, a remembered device can sign in with device authentication instead of SMS and time-based one-time password (TOTP) factors for multi-factor authentication (MFA).</p> <note> <p>Whether or not <code>ChallengeRequiredOnNewDevice</code> is true, users who sign in with devices that have not been confirmed or remembered must still provide a second factor in a user pool that requires MFA.</p> </note>"""
    device_only_remembered_on_user_prompt: (
        "capo_cognito_identity_provider.types.boolean_type.BooleanType"
    )
    """<p>When true, Amazon Cognito doesn't automatically remember a user's device when your app sends a <code>ConfirmDevice</code> API request. In your app, create a prompt for your user to choose whether they want to remember their device. Return the user's choice in an <code>UpdateDeviceStatus</code> API request.</p> <p>When <code>DeviceOnlyRememberedOnUserPrompt</code> is <code>false</code>, Amazon Cognito immediately remembers devices that you register in a <code>ConfirmDevice</code> API request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeviceConfigurationType) -> dict:
    out: dict = {}
    out["ChallengeRequiredOnNewDevice"] = value.get(
        "challenge_required_on_new_device", False
    )
    out["DeviceOnlyRememberedOnUserPrompt"] = value.get(
        "device_only_remembered_on_user_prompt", False
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeviceConfigurationType:
    out: DeviceConfigurationType = {}  # type: ignore[typeddict-item]
    if "ChallengeRequiredOnNewDevice" in data:
        out["challenge_required_on_new_device"] = data["ChallengeRequiredOnNewDevice"]
    else:
        out["challenge_required_on_new_device"] = False
    if "DeviceOnlyRememberedOnUserPrompt" in data:
        out["device_only_remembered_on_user_prompt"] = data[
            "DeviceOnlyRememberedOnUserPrompt"
        ]
    else:
        out["device_only_remembered_on_user_prompt"] = False
    return out
