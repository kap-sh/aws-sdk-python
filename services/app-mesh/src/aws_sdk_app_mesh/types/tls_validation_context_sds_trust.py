"""Generated from Smithy shape ``com.amazonaws.appmesh#TlsValidationContextSdsTrust``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.sds_secret_name


class TlsValidationContextSdsTrust(TypedDict):
    secret_name: "aws_sdk_app_mesh.types.sds_secret_name.SdsSecretName"
    """<p>A reference to an object that represents the name of the secret for a Transport Layer Security (TLS) Secret Discovery Service validation context trust.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TlsValidationContextSdsTrust) -> dict:
    out: dict = {}
    out["secretName"] = value["secret_name"]
    return out


def deserialize_json(data: dict) -> TlsValidationContextSdsTrust:
    out: TlsValidationContextSdsTrust = {}  # type: ignore[typeddict-item]
    if "secretName" in data:
        out["secret_name"] = data["secretName"]
    else:
        raise DeserializationError("TlsValidationContextSdsTrust.secret_name required")
    return out
