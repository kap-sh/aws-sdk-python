"""Generated from Smithy shape ``com.amazonaws.appmesh#JsonFormat``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.json_format_ref

JsonFormat: TypeAlias = list["aws_sdk_app_mesh.types.json_format_ref.JsonFormatRef"]


# --- restJson1 ser/de ---
def serialize_json(value: JsonFormat) -> list:
    import aws_sdk_app_mesh.types.json_format_ref

    out: list = []
    for item in value:
        out.append(aws_sdk_app_mesh.types.json_format_ref.serialize_json(item))
    return out


def deserialize_json(data: list) -> JsonFormat:
    import aws_sdk_app_mesh.types.json_format_ref

    out: JsonFormat = []
    for item in data:
        out.append(aws_sdk_app_mesh.types.json_format_ref.deserialize_json(item))
    return out
