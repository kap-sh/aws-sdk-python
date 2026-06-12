"""Generated from Smithy shape ``com.amazonaws.datasync#ReportOverrides``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datasync.types.report_override


class ReportOverrides(TypedDict):
    transferred: NotRequired["aws_sdk_datasync.types.report_override.ReportOverride"]
    """<p>Specifies the level of reporting for the files, objects, and directories that DataSync attempted to transfer.</p>"""
    verified: NotRequired["aws_sdk_datasync.types.report_override.ReportOverride"]
    """<p>Specifies the level of reporting for the files, objects, and directories that DataSync attempted to verify at the end of your transfer.</p>"""
    deleted: NotRequired["aws_sdk_datasync.types.report_override.ReportOverride"]
    """<p>Specifies the level of reporting for the files, objects, and directories that DataSync attempted to delete in your destination location. This only applies if you <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/configure-metadata.html\">configure your task</a> to delete data in the destination that isn't in the source.</p>"""
    skipped: NotRequired["aws_sdk_datasync.types.report_override.ReportOverride"]
    """<p>Specifies the level of reporting for the files, objects, and directories that DataSync attempted to skip during your transfer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportOverrides) -> dict:
    out: dict = {}
    if "transferred" in value:
        import aws_sdk_datasync.types.report_override

        out["Transferred"] = (
            aws_sdk_datasync.types.report_override.serialize_aws_json_1_1(
                value["transferred"]
            )
        )
    if "verified" in value:
        import aws_sdk_datasync.types.report_override

        out["Verified"] = aws_sdk_datasync.types.report_override.serialize_aws_json_1_1(
            value["verified"]
        )
    if "deleted" in value:
        import aws_sdk_datasync.types.report_override

        out["Deleted"] = aws_sdk_datasync.types.report_override.serialize_aws_json_1_1(
            value["deleted"]
        )
    if "skipped" in value:
        import aws_sdk_datasync.types.report_override

        out["Skipped"] = aws_sdk_datasync.types.report_override.serialize_aws_json_1_1(
            value["skipped"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReportOverrides:
    out: ReportOverrides = {}  # type: ignore[typeddict-item]
    if "Transferred" in data:
        import aws_sdk_datasync.types.report_override

        out["transferred"] = (
            aws_sdk_datasync.types.report_override.deserialize_aws_json_1_1(
                data["Transferred"]
            )
        )
    if "Verified" in data:
        import aws_sdk_datasync.types.report_override

        out["verified"] = (
            aws_sdk_datasync.types.report_override.deserialize_aws_json_1_1(
                data["Verified"]
            )
        )
    if "Deleted" in data:
        import aws_sdk_datasync.types.report_override

        out["deleted"] = (
            aws_sdk_datasync.types.report_override.deserialize_aws_json_1_1(
                data["Deleted"]
            )
        )
    if "Skipped" in data:
        import aws_sdk_datasync.types.report_override

        out["skipped"] = (
            aws_sdk_datasync.types.report_override.deserialize_aws_json_1_1(
                data["Skipped"]
            )
        )
    return out
