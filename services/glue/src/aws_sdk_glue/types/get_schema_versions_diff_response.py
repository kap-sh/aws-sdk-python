"""Generated from Smithy shape ``com.amazonaws.glue#GetSchemaVersionsDiffResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.schema_definition_diff


class GetSchemaVersionsDiffResponse(TypedDict, closed=True):
    diff: NotRequired["aws_sdk_glue.types.schema_definition_diff.SchemaDefinitionDiff"]
    """<p>The difference between schemas as a string in JsonPatch format.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSchemaVersionsDiffResponse) -> dict:
    out: dict = {}
    if "diff" in value:
        out["Diff"] = value["diff"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSchemaVersionsDiffResponse:
    out: GetSchemaVersionsDiffResponse = {}  # type: ignore[typeddict-item]
    if "Diff" in data:
        out["diff"] = data["Diff"]
    return out
