"""Generated from Smithy shape ``com.amazonaws.clouddirectory#UpdateSchemaResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.arn


class UpdateSchemaResponse(TypedDict, closed=True):
    schema_arn: NotRequired["capo_clouddirectory.types.arn.Arn"]
    """<p>The ARN that is associated with the updated schema. For more information, see <a>arns</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSchemaResponse) -> dict:
    out: dict = {}
    if "schema_arn" in value:
        out["SchemaArn"] = value["schema_arn"]
    return out


def deserialize_json(data: dict) -> UpdateSchemaResponse:
    out: UpdateSchemaResponse = {}  # type: ignore[typeddict-item]
    if "SchemaArn" in data:
        out["schema_arn"] = data["SchemaArn"]
    return out
