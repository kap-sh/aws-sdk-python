"""Generated from Smithy shape ``com.amazonaws.iot#UpdateCACertificateParams``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.ca_certificate_update_action


class UpdateCACertificateParams(TypedDict):
    action: "aws_sdk_iot.types.ca_certificate_update_action.CACertificateUpdateAction"
    """<p>The action that you want to apply to the CA certificate. The only supported value is <code>DEACTIVATE</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCACertificateParams) -> dict:
    out: dict = {}
    import aws_sdk_iot.types.ca_certificate_update_action

    out["action"] = aws_sdk_iot.types.ca_certificate_update_action.serialize_json(
        value["action"]
    )
    return out


def deserialize_json(data: dict) -> UpdateCACertificateParams:
    out: UpdateCACertificateParams = {}  # type: ignore[typeddict-item]
    if "action" in data:
        import aws_sdk_iot.types.ca_certificate_update_action

        out["action"] = aws_sdk_iot.types.ca_certificate_update_action.deserialize_json(
            data["action"]
        )
    else:
        raise DeserializationError("UpdateCACertificateParams.action required")
    return out
