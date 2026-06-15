"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UserContextDataType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.string_type


class UserContextDataType(TypedDict):
    ip_address: NotRequired[
        "aws_sdk_cognito_identity_provider.types.string_type.StringType"
    ]
    """<p>The source IP address of your user's device.</p>"""
    encoded_data: NotRequired[
        "aws_sdk_cognito_identity_provider.types.string_type.StringType"
    ]
    r"""<p>Encoded device-fingerprint details that your app collected with the Amazon Cognito context data collection library. For more information, see <a href=\"https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-adaptive-authentication.html#user-pool-settings-adaptive-authentication-device-fingerprint\">Adding user device and session data to API requests</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserContextDataType) -> dict:
    out: dict = {}
    if "ip_address" in value:
        out["IpAddress"] = value["ip_address"]
    if "encoded_data" in value:
        out["EncodedData"] = value["encoded_data"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UserContextDataType:
    out: UserContextDataType = {}  # type: ignore[typeddict-item]
    if "IpAddress" in data:
        out["ip_address"] = data["IpAddress"]
    if "EncodedData" in data:
        out["encoded_data"] = data["EncodedData"]
    return out
