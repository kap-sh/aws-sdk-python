"""Generated from Smithy shape ``com.amazonaws.clouddirectory#GetAppliedSchemaVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.arn


class GetAppliedSchemaVersionResponse(TypedDict, closed=True):
    applied_schema_arn: NotRequired["aws_sdk_clouddirectory.types.arn.Arn"]
    """<p>Current applied schema ARN, including the minor version in use if one was provided.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAppliedSchemaVersionResponse) -> dict:
    out: dict = {}
    if "applied_schema_arn" in value:
        out["AppliedSchemaArn"] = value["applied_schema_arn"]
    return out


def deserialize_json(data: dict) -> GetAppliedSchemaVersionResponse:
    out: GetAppliedSchemaVersionResponse = {}  # type: ignore[typeddict-item]
    if "AppliedSchemaArn" in data:
        out["applied_schema_arn"] = data["AppliedSchemaArn"]
    return out
