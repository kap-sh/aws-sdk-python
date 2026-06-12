"""Generated from Smithy shape ``com.amazonaws.clouddirectory#CreateSchemaResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.arn


class CreateSchemaResponse(TypedDict):
    schema_arn: NotRequired["aws_sdk_clouddirectory.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) that is associated with the schema. For more information, see <a>arns</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSchemaResponse) -> dict:
    out: dict = {}
    if "schema_arn" in value:
        out["SchemaArn"] = value["schema_arn"]
    return out


def deserialize_json(data: dict) -> CreateSchemaResponse:
    out: CreateSchemaResponse = {}  # type: ignore[typeddict-item]
    if "SchemaArn" in data:
        out["schema_arn"] = data["SchemaArn"]
    return out
