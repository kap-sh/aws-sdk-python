"""Generated from Smithy shape ``com.amazonaws.clouddirectory#ApplySchemaResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.arn


class ApplySchemaResponse(TypedDict):
    applied_schema_arn: NotRequired["aws_sdk_clouddirectory.types.arn.Arn"]
    """<p>The applied schema ARN that is associated with the copied schema in the <a>Directory</a>. You can use this ARN to describe the schema information applied on this directory. For more information, see <a>arns</a>.</p>"""
    directory_arn: NotRequired["aws_sdk_clouddirectory.types.arn.Arn"]
    """<p>The ARN that is associated with the <a>Directory</a>. For more information, see <a>arns</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApplySchemaResponse) -> dict:
    out: dict = {}
    if "applied_schema_arn" in value:
        out["AppliedSchemaArn"] = value["applied_schema_arn"]
    if "directory_arn" in value:
        out["DirectoryArn"] = value["directory_arn"]
    return out


def deserialize_json(data: dict) -> ApplySchemaResponse:
    out: ApplySchemaResponse = {}  # type: ignore[typeddict-item]
    if "AppliedSchemaArn" in data:
        out["applied_schema_arn"] = data["AppliedSchemaArn"]
    if "DirectoryArn" in data:
        out["directory_arn"] = data["DirectoryArn"]
    return out
