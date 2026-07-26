"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualGatewayBackendDefaults``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_app_mesh.types.virtual_gateway_client_policy


class VirtualGatewayBackendDefaults(TypedDict, closed=True):
    client_policy: NotRequired[
        "capo_app_mesh.types.virtual_gateway_client_policy.VirtualGatewayClientPolicy"
    ]
    """<p>A reference to an object that represents a client policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VirtualGatewayBackendDefaults) -> dict:
    out: dict = {}
    if "client_policy" in value:
        import capo_app_mesh.types.virtual_gateway_client_policy

        out["clientPolicy"] = (
            capo_app_mesh.types.virtual_gateway_client_policy.serialize_json(
                value["client_policy"]
            )
        )
    return out


def deserialize_json(data: dict) -> VirtualGatewayBackendDefaults:
    out: VirtualGatewayBackendDefaults = {}  # type: ignore[typeddict-item]
    if "clientPolicy" in data:
        import capo_app_mesh.types.virtual_gateway_client_policy

        out["client_policy"] = (
            capo_app_mesh.types.virtual_gateway_client_policy.deserialize_json(
                data["clientPolicy"]
            )
        )
    return out
