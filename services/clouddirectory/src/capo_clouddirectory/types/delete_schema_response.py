"""Generated from Smithy shape ``com.amazonaws.clouddirectory#DeleteSchemaResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.arn


class DeleteSchemaResponse(TypedDict, closed=True):
    schema_arn: NotRequired["capo_clouddirectory.types.arn.Arn"]
    """<p>The input ARN that is returned as part of the response. For more information, see <a>arns</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSchemaResponse) -> dict:
    out: dict = {}
    if "schema_arn" in value:
        out["SchemaArn"] = value["schema_arn"]
    return out


def deserialize_json(data: dict) -> DeleteSchemaResponse:
    out: DeleteSchemaResponse = {}  # type: ignore[typeddict-item]
    if "SchemaArn" in data:
        out["schema_arn"] = data["SchemaArn"]
    return out
