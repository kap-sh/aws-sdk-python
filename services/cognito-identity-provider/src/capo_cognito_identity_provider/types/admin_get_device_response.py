"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AdminGetDeviceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.device_type


class AdminGetDeviceResponse(TypedDict, closed=True):
    device: "capo_cognito_identity_provider.types.device_type.DeviceType"
    """<p>Details of the requested device. Includes device information, last-accessed and created dates, and the device key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdminGetDeviceResponse) -> dict:
    out: dict = {}
    import capo_cognito_identity_provider.types.device_type

    out["Device"] = (
        capo_cognito_identity_provider.types.device_type.serialize_aws_json_1_1(
            value["device"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AdminGetDeviceResponse:
    out: AdminGetDeviceResponse = {}  # type: ignore[typeddict-item]
    if "Device" in data:
        import capo_cognito_identity_provider.types.device_type

        out["device"] = (
            capo_cognito_identity_provider.types.device_type.deserialize_aws_json_1_1(
                data["Device"]
            )
        )
    else:
        raise DeserializationError("AdminGetDeviceResponse.device required")
    return out
