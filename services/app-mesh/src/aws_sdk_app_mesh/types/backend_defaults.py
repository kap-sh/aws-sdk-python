"""Generated from Smithy shape ``com.amazonaws.appmesh#BackendDefaults``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.client_policy

class BackendDefaults(TypedDict):
    client_policy: NotRequired["aws_sdk_app_mesh.types.client_policy.ClientPolicy"]
    """<p>A reference to an object that represents a client policy.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: BackendDefaults) -> dict:
    out: dict = {}
    if "client_policy" in value:
        import aws_sdk_app_mesh.types.client_policy
        out["clientPolicy"] = aws_sdk_app_mesh.types.client_policy.serialize_json(value["client_policy"])
    return out


def deserialize_json(data: dict) -> BackendDefaults:
    out: BackendDefaults = {}  # type: ignore[typeddict-item]
    if "clientPolicy" in data:
        import aws_sdk_app_mesh.types.client_policy
        out["client_policy"] = aws_sdk_app_mesh.types.client_policy.deserialize_json(data["clientPolicy"])
    return out