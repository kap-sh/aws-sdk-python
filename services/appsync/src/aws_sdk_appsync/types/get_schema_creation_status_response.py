"""Generated from Smithy shape ``com.amazonaws.appsync#GetSchemaCreationStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appsync.types.schema_status
    import aws_sdk_appsync.types.string


class GetSchemaCreationStatusResponse(TypedDict, closed=True):
    status: NotRequired["aws_sdk_appsync.types.schema_status.SchemaStatus"]
    """<p>The current state of the schema (PROCESSING, FAILED, SUCCESS, or NOT_APPLICABLE). When the schema is in the ACTIVE state, you can add data.</p>"""
    details: NotRequired["aws_sdk_appsync.types.string.String"]
    """<p>Detailed information about the status of the schema creation operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSchemaCreationStatusResponse) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_appsync.types.schema_status

        out["status"] = aws_sdk_appsync.types.schema_status.serialize_json(
            value["status"]
        )
    if "details" in value:
        out["details"] = value["details"]
    return out


def deserialize_json(data: dict) -> GetSchemaCreationStatusResponse:
    out: GetSchemaCreationStatusResponse = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_appsync.types.schema_status

        out["status"] = aws_sdk_appsync.types.schema_status.deserialize_json(
            data["status"]
        )
    if "details" in data:
        out["details"] = data["details"]
    return out
