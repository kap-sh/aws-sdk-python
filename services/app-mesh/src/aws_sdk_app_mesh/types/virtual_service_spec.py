"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualServiceSpec``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.virtual_service_provider


class VirtualServiceSpec(TypedDict, closed=True):
    provider: NotRequired[
        "aws_sdk_app_mesh.types.virtual_service_provider.VirtualServiceProvider"
    ]
    """<p>The App Mesh object that is acting as the provider for a virtual service. You can specify a single virtual node or virtual router.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VirtualServiceSpec) -> dict:
    out: dict = {}
    if "provider" in value:
        import aws_sdk_app_mesh.types.virtual_service_provider

        out["provider"] = (
            aws_sdk_app_mesh.types.virtual_service_provider.serialize_json(
                value["provider"]
            )
        )
    return out


def deserialize_json(data: dict) -> VirtualServiceSpec:
    out: VirtualServiceSpec = {}  # type: ignore[typeddict-item]
    if "provider" in data:
        import aws_sdk_app_mesh.types.virtual_service_provider

        out["provider"] = (
            aws_sdk_app_mesh.types.virtual_service_provider.deserialize_json(
                data["provider"]
            )
        )
    return out
