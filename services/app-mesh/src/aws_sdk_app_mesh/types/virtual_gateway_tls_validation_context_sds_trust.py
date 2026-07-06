"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualGatewayTlsValidationContextSdsTrust``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.virtual_gateway_sds_secret_name


class VirtualGatewayTlsValidationContextSdsTrust(TypedDict, closed=True):
    secret_name: "aws_sdk_app_mesh.types.virtual_gateway_sds_secret_name.VirtualGatewaySdsSecretName"
    """<p>A reference to an object that represents the name of the secret for a virtual gateway's Transport Layer Security (TLS) Secret Discovery Service validation context trust.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VirtualGatewayTlsValidationContextSdsTrust) -> dict:
    out: dict = {}
    out["secretName"] = value["secret_name"]
    return out


def deserialize_json(data: dict) -> VirtualGatewayTlsValidationContextSdsTrust:
    out: VirtualGatewayTlsValidationContextSdsTrust = {}  # type: ignore[typeddict-item]
    if "secretName" in data:
        out["secret_name"] = data["secretName"]
    else:
        raise DeserializationError(
            "VirtualGatewayTlsValidationContextSdsTrust.secret_name required"
        )
    return out
