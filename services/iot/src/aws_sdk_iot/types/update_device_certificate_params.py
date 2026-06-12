"""Generated from Smithy shape ``com.amazonaws.iot#UpdateDeviceCertificateParams``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.device_certificate_update_action


class UpdateDeviceCertificateParams(TypedDict):
    action: "aws_sdk_iot.types.device_certificate_update_action.DeviceCertificateUpdateAction"
    """<p>The action that you want to apply to the device certificate. The only supported value is <code>DEACTIVATE</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDeviceCertificateParams) -> dict:
    out: dict = {}
    import aws_sdk_iot.types.device_certificate_update_action

    out["action"] = aws_sdk_iot.types.device_certificate_update_action.serialize_json(
        value["action"]
    )
    return out


def deserialize_json(data: dict) -> UpdateDeviceCertificateParams:
    out: UpdateDeviceCertificateParams = {}  # type: ignore[typeddict-item]
    if "action" in data:
        import aws_sdk_iot.types.device_certificate_update_action

        out["action"] = (
            aws_sdk_iot.types.device_certificate_update_action.deserialize_json(
                data["action"]
            )
        )
    else:
        raise DeserializationError("UpdateDeviceCertificateParams.action required")
    return out
