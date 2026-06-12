"""Generated from Smithy shape ``com.amazonaws.schemas#ExportSchemaRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_schemas.types.__string


class ExportSchemaRequest(TypedDict):
    registry_name: "aws_sdk_schemas.types.__string.__string"
    """<p>The name of the registry.</p>"""
    schema_name: "aws_sdk_schemas.types.__string.__string"
    """<p>The name of the schema.</p>"""
    schema_version: NotRequired["aws_sdk_schemas.types.__string.__string"]
    """<p>Specifying this limits the results to only this schema version.</p>"""
    type: NotRequired["aws_sdk_schemas.types.__string.__string"]


# --- restJson1 ser/de ---
def serialize_json(value: ExportSchemaRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ExportSchemaRequest:
    out: ExportSchemaRequest = {}  # type: ignore[typeddict-item]
    return out
