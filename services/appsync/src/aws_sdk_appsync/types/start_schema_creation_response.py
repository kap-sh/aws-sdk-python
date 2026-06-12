"""Generated from Smithy shape ``com.amazonaws.appsync#StartSchemaCreationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appsync.types.schema_status


class StartSchemaCreationResponse(TypedDict):
    status: NotRequired["aws_sdk_appsync.types.schema_status.SchemaStatus"]
    """<p>The current state of the schema (PROCESSING, FAILED, SUCCESS, or NOT_APPLICABLE). When the schema is in the ACTIVE state, you can add data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartSchemaCreationResponse) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_appsync.types.schema_status

        out["status"] = aws_sdk_appsync.types.schema_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> StartSchemaCreationResponse:
    out: StartSchemaCreationResponse = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_appsync.types.schema_status

        out["status"] = aws_sdk_appsync.types.schema_status.deserialize_json(
            data["status"]
        )
    return out
