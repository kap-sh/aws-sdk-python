"""Generated from Smithy shape ``com.amazonaws.appmesh#Backend``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_app_mesh.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.virtual_service_backend


class _Backend_virtualService(TypedDict, closed=True):
    virtualService: (
        "aws_sdk_app_mesh.types.virtual_service_backend.VirtualServiceBackend"
    )


Backend: TypeAlias = _Backend_virtualService


# --- restJson1 ser/de ---
def serialize_json(value: Backend) -> dict:
    if "virtualService" in value:
        import aws_sdk_app_mesh.types.virtual_service_backend

        return {
            "virtualService": aws_sdk_app_mesh.types.virtual_service_backend.serialize_json(
                value["virtualService"]
            )
        }
    else:
        raise SerializationError("Backend: no variant present")


def deserialize_json(data: dict) -> Backend:
    if "virtualService" in data:
        import aws_sdk_app_mesh.types.virtual_service_backend

        return {
            "virtualService": aws_sdk_app_mesh.types.virtual_service_backend.deserialize_json(
                data["virtualService"]
            )
        }
    else:
        raise DeserializationError("Backend: no recognized variant key")
