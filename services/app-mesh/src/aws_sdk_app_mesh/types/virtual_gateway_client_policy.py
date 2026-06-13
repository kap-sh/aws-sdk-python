"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualGatewayClientPolicy``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.virtual_gateway_client_policy_tls


class VirtualGatewayClientPolicy(TypedDict):
    tls: NotRequired[
        "aws_sdk_app_mesh.types.virtual_gateway_client_policy_tls.VirtualGatewayClientPolicyTls"
    ]
    """<p>A reference to an object that represents a Transport Layer Security (TLS) client policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VirtualGatewayClientPolicy) -> dict:
    out: dict = {}
    if "tls" in value:
        import aws_sdk_app_mesh.types.virtual_gateway_client_policy_tls

        out["tls"] = (
            aws_sdk_app_mesh.types.virtual_gateway_client_policy_tls.serialize_json(
                value["tls"]
            )
        )
    return out


def deserialize_json(data: dict) -> VirtualGatewayClientPolicy:
    out: VirtualGatewayClientPolicy = {}  # type: ignore[typeddict-item]
    if "tls" in data:
        import aws_sdk_app_mesh.types.virtual_gateway_client_policy_tls

        out["tls"] = (
            aws_sdk_app_mesh.types.virtual_gateway_client_policy_tls.deserialize_json(
                data["tls"]
            )
        )
    return out
