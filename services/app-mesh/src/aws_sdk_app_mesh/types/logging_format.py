"""Generated from Smithy shape ``com.amazonaws.appmesh#LoggingFormat``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_app_mesh.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.json_format
    import aws_sdk_app_mesh.types.text_format


class _LoggingFormat_text(TypedDict):
    text: "aws_sdk_app_mesh.types.text_format.TextFormat"


class _LoggingFormat_json(TypedDict):
    json: "aws_sdk_app_mesh.types.json_format.JsonFormat"


LoggingFormat: TypeAlias = _LoggingFormat_text | _LoggingFormat_json


# --- restJson1 ser/de ---
def serialize_json(value: LoggingFormat) -> dict:
    if "text" in value:
        return {"text": value["text"]}
    elif "json" in value:
        import aws_sdk_app_mesh.types.json_format

        return {
            "json": aws_sdk_app_mesh.types.json_format.serialize_json(value["json"])
        }
    else:
        raise SerializationError("LoggingFormat: no variant present")


def deserialize_json(data: dict) -> LoggingFormat:
    if "text" in data:
        return {"text": data["text"]}
    elif "json" in data:
        import aws_sdk_app_mesh.types.json_format

        return {
            "json": aws_sdk_app_mesh.types.json_format.deserialize_json(data["json"])
        }
    else:
        raise DeserializationError("LoggingFormat: no recognized variant key")
