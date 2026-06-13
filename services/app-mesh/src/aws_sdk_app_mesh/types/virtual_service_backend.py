"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualServiceBackend``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.client_policy
    import aws_sdk_app_mesh.types.service_name


class VirtualServiceBackend(TypedDict):
    virtual_service_name: "aws_sdk_app_mesh.types.service_name.ServiceName"
    """<p>The name of the virtual service that is acting as a virtual node backend.</p>"""
    client_policy: NotRequired["aws_sdk_app_mesh.types.client_policy.ClientPolicy"]
    """<p>A reference to an object that represents the client policy for a backend.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VirtualServiceBackend) -> dict:
    out: dict = {}
    out["virtualServiceName"] = value["virtual_service_name"]
    if "client_policy" in value:
        import aws_sdk_app_mesh.types.client_policy

        out["clientPolicy"] = aws_sdk_app_mesh.types.client_policy.serialize_json(
            value["client_policy"]
        )
    return out


def deserialize_json(data: dict) -> VirtualServiceBackend:
    out: VirtualServiceBackend = {}  # type: ignore[typeddict-item]
    if "virtualServiceName" in data:
        out["virtual_service_name"] = data["virtualServiceName"]
    else:
        raise DeserializationError(
            "VirtualServiceBackend.virtual_service_name required"
        )
    if "clientPolicy" in data:
        import aws_sdk_app_mesh.types.client_policy

        out["client_policy"] = aws_sdk_app_mesh.types.client_policy.deserialize_json(
            data["clientPolicy"]
        )
    return out
