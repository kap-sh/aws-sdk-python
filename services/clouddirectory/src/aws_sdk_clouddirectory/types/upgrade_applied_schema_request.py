"""Generated from Smithy shape ``com.amazonaws.clouddirectory#UpgradeAppliedSchemaRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.arn
    import aws_sdk_clouddirectory.types.bool


class UpgradeAppliedSchemaRequest(TypedDict, closed=True):
    published_schema_arn: "aws_sdk_clouddirectory.types.arn.Arn"
    """<p>The revision of the published schema to upgrade the directory to.</p>"""
    directory_arn: "aws_sdk_clouddirectory.types.arn.Arn"
    """<p>The ARN for the directory to which the upgraded schema will be applied.</p>"""
    dry_run: "aws_sdk_clouddirectory.types.bool.Bool"
    """<p>Used for testing whether the major version schemas are backward compatible or not. If schema compatibility fails, an exception would be thrown else the call would succeed but no changes will be saved. This parameter is optional.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpgradeAppliedSchemaRequest) -> dict:
    out: dict = {}
    out["PublishedSchemaArn"] = value["published_schema_arn"]
    out["DirectoryArn"] = value["directory_arn"]
    out["DryRun"] = value.get("dry_run", False)
    return out


def deserialize_json(data: dict) -> UpgradeAppliedSchemaRequest:
    out: UpgradeAppliedSchemaRequest = {}  # type: ignore[typeddict-item]
    if "PublishedSchemaArn" in data:
        out["published_schema_arn"] = data["PublishedSchemaArn"]
    else:
        raise DeserializationError(
            "UpgradeAppliedSchemaRequest.published_schema_arn required"
        )
    if "DirectoryArn" in data:
        out["directory_arn"] = data["DirectoryArn"]
    else:
        raise DeserializationError("UpgradeAppliedSchemaRequest.directory_arn required")
    if "DryRun" in data:
        out["dry_run"] = data["DryRun"]
    else:
        out["dry_run"] = False
    return out
