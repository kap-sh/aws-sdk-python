"""Generated from Smithy shape ``com.amazonaws.appmesh#ListenerTlsSdsCertificate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import capo_app_mesh.types.sds_secret_name


class ListenerTlsSdsCertificate(TypedDict, closed=True):
    secret_name: "capo_app_mesh.types.sds_secret_name.SdsSecretName"
    """<p>A reference to an object that represents the name of the secret requested from the Secret Discovery Service provider representing Transport Layer Security (TLS) materials like a certificate or certificate chain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListenerTlsSdsCertificate) -> dict:
    out: dict = {}
    out["secretName"] = value["secret_name"]
    return out


def deserialize_json(data: dict) -> ListenerTlsSdsCertificate:
    out: ListenerTlsSdsCertificate = {}  # type: ignore[typeddict-item]
    if "secretName" in data:
        out["secret_name"] = data["secretName"]
    else:
        raise DeserializationError("ListenerTlsSdsCertificate.secret_name required")
    return out
