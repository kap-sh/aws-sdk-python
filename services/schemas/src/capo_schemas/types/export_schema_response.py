"""Generated from Smithy shape ``com.amazonaws.schemas#ExportSchemaResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_schemas.types.__string


class ExportSchemaResponse(TypedDict, closed=True):
    content: NotRequired["capo_schemas.types.__string.__string"]
    schema_arn: NotRequired["capo_schemas.types.__string.__string"]
    schema_name: NotRequired["capo_schemas.types.__string.__string"]
    schema_version: NotRequired["capo_schemas.types.__string.__string"]
    type: NotRequired["capo_schemas.types.__string.__string"]


# --- restJson1 ser/de ---
def serialize_json(value: ExportSchemaResponse) -> dict:
    out: dict = {}
    if "content" in value:
        out["Content"] = value["content"]
    if "schema_arn" in value:
        out["SchemaArn"] = value["schema_arn"]
    if "schema_name" in value:
        out["SchemaName"] = value["schema_name"]
    if "schema_version" in value:
        out["SchemaVersion"] = value["schema_version"]
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_json(data: dict) -> ExportSchemaResponse:
    out: ExportSchemaResponse = {}  # type: ignore[typeddict-item]
    if "Content" in data:
        out["content"] = data["Content"]
    if "SchemaArn" in data:
        out["schema_arn"] = data["SchemaArn"]
    if "SchemaName" in data:
        out["schema_name"] = data["SchemaName"]
    if "SchemaVersion" in data:
        out["schema_version"] = data["SchemaVersion"]
    if "Type" in data:
        out["type"] = data["Type"]
    return out
