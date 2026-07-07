"""Generated from Smithy shape ``com.amazonaws.appmesh#ClientPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.client_policy_tls


class ClientPolicy(TypedDict, closed=True):
    tls: NotRequired["aws_sdk_app_mesh.types.client_policy_tls.ClientPolicyTls"]
    """<p>A reference to an object that represents a Transport Layer Security (TLS) client policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClientPolicy) -> dict:
    out: dict = {}
    if "tls" in value:
        import aws_sdk_app_mesh.types.client_policy_tls

        out["tls"] = aws_sdk_app_mesh.types.client_policy_tls.serialize_json(
            value["tls"]
        )
    return out


def deserialize_json(data: dict) -> ClientPolicy:
    out: ClientPolicy = {}  # type: ignore[typeddict-item]
    if "tls" in data:
        import aws_sdk_app_mesh.types.client_policy_tls

        out["tls"] = aws_sdk_app_mesh.types.client_policy_tls.deserialize_json(
            data["tls"]
        )
    return out
