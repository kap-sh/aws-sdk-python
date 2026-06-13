"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualGatewayAccessLog``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_app_mesh.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.virtual_gateway_file_access_log


class _VirtualGatewayAccessLog_file(TypedDict):
    file: "aws_sdk_app_mesh.types.virtual_gateway_file_access_log.VirtualGatewayFileAccessLog"


VirtualGatewayAccessLog: TypeAlias = _VirtualGatewayAccessLog_file


# --- restJson1 ser/de ---
def serialize_json(value: VirtualGatewayAccessLog) -> dict:
    if "file" in value:
        import aws_sdk_app_mesh.types.virtual_gateway_file_access_log

        return {
            "file": aws_sdk_app_mesh.types.virtual_gateway_file_access_log.serialize_json(
                value["file"]
            )
        }
    else:
        raise SerializationError("VirtualGatewayAccessLog: no variant present")


def deserialize_json(data: dict) -> VirtualGatewayAccessLog:
    if "file" in data:
        import aws_sdk_app_mesh.types.virtual_gateway_file_access_log

        return {
            "file": aws_sdk_app_mesh.types.virtual_gateway_file_access_log.deserialize_json(
                data["file"]
            )
        }
    else:
        raise DeserializationError("VirtualGatewayAccessLog: no recognized variant key")
