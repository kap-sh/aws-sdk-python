"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DeviceSecretVerifierConfigType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.string_type


class DeviceSecretVerifierConfigType(TypedDict):
    password_verifier: NotRequired[
        "aws_sdk_cognito_identity_provider.types.string_type.StringType"
    ]
    """<p>A password verifier for a user's device. Used in SRP authentication.</p>"""
    salt: NotRequired["aws_sdk_cognito_identity_provider.types.string_type.StringType"]
    """<p>The salt that you want to use in SRP authentication with the user's device.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeviceSecretVerifierConfigType) -> dict:
    out: dict = {}
    if "password_verifier" in value:
        out["PasswordVerifier"] = value["password_verifier"]
    if "salt" in value:
        out["Salt"] = value["salt"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeviceSecretVerifierConfigType:
    out: DeviceSecretVerifierConfigType = {}  # type: ignore[typeddict-item]
    if "PasswordVerifier" in data:
        out["password_verifier"] = data["PasswordVerifier"]
    if "Salt" in data:
        out["salt"] = data["Salt"]
    return out
