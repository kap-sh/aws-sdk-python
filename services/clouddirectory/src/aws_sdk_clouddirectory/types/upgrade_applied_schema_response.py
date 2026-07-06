"""Generated from Smithy shape ``com.amazonaws.clouddirectory#UpgradeAppliedSchemaResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.arn


class UpgradeAppliedSchemaResponse(TypedDict, closed=True):
    upgraded_schema_arn: NotRequired["aws_sdk_clouddirectory.types.arn.Arn"]
    """<p>The ARN of the upgraded schema that is returned as part of the response.</p>"""
    directory_arn: NotRequired["aws_sdk_clouddirectory.types.arn.Arn"]
    """<p>The ARN of the directory that is returned as part of the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpgradeAppliedSchemaResponse) -> dict:
    out: dict = {}
    if "upgraded_schema_arn" in value:
        out["UpgradedSchemaArn"] = value["upgraded_schema_arn"]
    if "directory_arn" in value:
        out["DirectoryArn"] = value["directory_arn"]
    return out


def deserialize_json(data: dict) -> UpgradeAppliedSchemaResponse:
    out: UpgradeAppliedSchemaResponse = {}  # type: ignore[typeddict-item]
    if "UpgradedSchemaArn" in data:
        out["upgraded_schema_arn"] = data["UpgradedSchemaArn"]
    if "DirectoryArn" in data:
        out["directory_arn"] = data["DirectoryArn"]
    return out
