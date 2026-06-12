"""Generated from Smithy shape ``com.amazonaws.directoryservice#StartSchemaExtensionResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.schema_extension_id


class StartSchemaExtensionResult(TypedDict):
    schema_extension_id: NotRequired[
        "aws_sdk_directory_service.types.schema_extension_id.SchemaExtensionId"
    ]
    """<p>The identifier of the schema extension that will be applied.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartSchemaExtensionResult) -> dict:
    out: dict = {}
    if "schema_extension_id" in value:
        out["SchemaExtensionId"] = value["schema_extension_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartSchemaExtensionResult:
    out: StartSchemaExtensionResult = {}  # type: ignore[typeddict-item]
    if "SchemaExtensionId" in data:
        out["schema_extension_id"] = data["SchemaExtensionId"]
    return out
