"""Generated from Smithy shape ``com.amazonaws.clouddirectory#PutSchemaFromJsonResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.arn


class PutSchemaFromJsonResponse(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_clouddirectory.types.arn.Arn"]
    """<p>The ARN of the schema to update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutSchemaFromJsonResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> PutSchemaFromJsonResponse:
    out: PutSchemaFromJsonResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
