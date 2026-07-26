"""Generated from Smithy shape ``com.amazonaws.appmesh#DeleteVirtualServiceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import capo_app_mesh.types.virtual_service_data


class DeleteVirtualServiceOutput(TypedDict, closed=True):
    virtual_service: "capo_app_mesh.types.virtual_service_data.VirtualServiceData"
    """<p>The virtual service that was deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteVirtualServiceOutput) -> dict:
    out: dict = {}
    import capo_app_mesh.types.virtual_service_data

    out["virtualService"] = capo_app_mesh.types.virtual_service_data.serialize_json(
        value["virtual_service"]
    )
    return out


def deserialize_json(data: dict) -> DeleteVirtualServiceOutput:
    out: DeleteVirtualServiceOutput = {}  # type: ignore[typeddict-item]
    if "virtualService" in data:
        import capo_app_mesh.types.virtual_service_data

        out["virtual_service"] = (
            capo_app_mesh.types.virtual_service_data.deserialize_json(
                data["virtualService"]
            )
        )
    else:
        raise DeserializationError(
            "DeleteVirtualServiceOutput.virtual_service required"
        )
    return out
