"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.asset_bundle_export_format
    import aws_sdk_quicksight.types.asset_bundle_export_job_status
    import aws_sdk_quicksight.types.boolean
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.timestamp


class AssetBundleExportJobSummary(TypedDict):
    job_status: NotRequired[
        "aws_sdk_quicksight.types.asset_bundle_export_job_status.AssetBundleExportJobStatus"
    ]
    """<p>The current status of the export job.</p>"""
    arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The ARN of the export job.</p>"""
    created_time: NotRequired["aws_sdk_quicksight.types.timestamp.Timestamp"]
    """<p>The time that the export job was created.</p>"""
    asset_bundle_export_job_id: NotRequired[
        "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>The ID of the export job.</p>"""
    include_all_dependencies: "aws_sdk_quicksight.types.boolean.Boolean"
    """<p>The flag that determines the inclusion of resource dependencies in the returned asset bundle.</p>"""
    export_format: NotRequired[
        "aws_sdk_quicksight.types.asset_bundle_export_format.AssetBundleExportFormat"
    ]
    """<p>The format for the export job.</p>"""
    include_permissions: "aws_sdk_quicksight.types.boolean.Boolean"
    """<p>The flag that determines the inclusion of permissions associated with each resource ARN.</p>"""
    include_tags: "aws_sdk_quicksight.types.boolean.Boolean"
    """<p>The flag that determines the inclusion of tags associated with each resource ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleExportJobSummary) -> dict:
    out: dict = {}
    if "job_status" in value:
        import aws_sdk_quicksight.types.asset_bundle_export_job_status

        out["JobStatus"] = (
            aws_sdk_quicksight.types.asset_bundle_export_job_status.serialize_json(
                value["job_status"]
            )
        )
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "created_time" in value:
        import aws_sdk_quicksight.types.timestamp

        out["CreatedTime"] = aws_sdk_quicksight.types.timestamp.serialize_json(
            value["created_time"]
        )
    if "asset_bundle_export_job_id" in value:
        out["AssetBundleExportJobId"] = value["asset_bundle_export_job_id"]
    out["IncludeAllDependencies"] = value.get("include_all_dependencies", False)
    if "export_format" in value:
        import aws_sdk_quicksight.types.asset_bundle_export_format

        out["ExportFormat"] = (
            aws_sdk_quicksight.types.asset_bundle_export_format.serialize_json(
                value["export_format"]
            )
        )
    out["IncludePermissions"] = value.get("include_permissions", False)
    out["IncludeTags"] = value.get("include_tags", False)
    return out


def deserialize_json(data: dict) -> AssetBundleExportJobSummary:
    out: AssetBundleExportJobSummary = {}  # type: ignore[typeddict-item]
    if "JobStatus" in data:
        import aws_sdk_quicksight.types.asset_bundle_export_job_status

        out["job_status"] = (
            aws_sdk_quicksight.types.asset_bundle_export_job_status.deserialize_json(
                data["JobStatus"]
            )
        )
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "CreatedTime" in data:
        import aws_sdk_quicksight.types.timestamp

        out["created_time"] = aws_sdk_quicksight.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    if "AssetBundleExportJobId" in data:
        out["asset_bundle_export_job_id"] = data["AssetBundleExportJobId"]
    if "IncludeAllDependencies" in data:
        out["include_all_dependencies"] = data["IncludeAllDependencies"]
    else:
        out["include_all_dependencies"] = False
    if "ExportFormat" in data:
        import aws_sdk_quicksight.types.asset_bundle_export_format

        out["export_format"] = (
            aws_sdk_quicksight.types.asset_bundle_export_format.deserialize_json(
                data["ExportFormat"]
            )
        )
    if "IncludePermissions" in data:
        out["include_permissions"] = data["IncludePermissions"]
    else:
        out["include_permissions"] = False
    if "IncludeTags" in data:
        out["include_tags"] = data["IncludeTags"]
    else:
        out["include_tags"] = False
    return out
