"""Generated from Smithy shape ``com.amazonaws.fsx#CompletionReport``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fsx.types.archive_path
    import aws_sdk_fsx.types.flag
    import aws_sdk_fsx.types.report_format
    import aws_sdk_fsx.types.report_scope


class CompletionReport(TypedDict, closed=True):
    enabled: NotRequired["aws_sdk_fsx.types.flag.Flag"]
    """<p>Set <code>Enabled</code> to <code>True</code> to generate a <code>CompletionReport</code> when the task completes. If set to <code>true</code>, then you need to provide a report <code>Scope</code>, <code>Path</code>, and <code>Format</code>. Set <code>Enabled</code> to <code>False</code> if you do not want a <code>CompletionReport</code> generated when the task completes.</p>"""
    path: NotRequired["aws_sdk_fsx.types.archive_path.ArchivePath"]
    r"""<p>Required if <code>Enabled</code> is set to <code>true</code>. Specifies the location of the report on the file system's linked S3 data repository. An absolute path that defines where the completion report will be stored in the destination location. The <code>Path</code> you provide must be located within the file system’s ExportPath. An example <code>Path</code> value is \"s3://amzn-s3-demo-bucket/myExportPath/optionalPrefix\". The report provides the following information for each file in the report: FilePath, FileStatus, and ErrorCode.</p>"""
    format: NotRequired["aws_sdk_fsx.types.report_format.ReportFormat"]
    """<p>Required if <code>Enabled</code> is set to <code>true</code>. Specifies the format of the <code>CompletionReport</code>. <code>REPORT_CSV_20191124</code> is the only format currently supported. When <code>Format</code> is set to <code>REPORT_CSV_20191124</code>, the <code>CompletionReport</code> is provided in CSV format, and is delivered to <code>{path}/task-{id}/failures.csv</code>. </p>"""
    scope: NotRequired["aws_sdk_fsx.types.report_scope.ReportScope"]
    """<p>Required if <code>Enabled</code> is set to <code>true</code>. Specifies the scope of the <code>CompletionReport</code>; <code>FAILED_FILES_ONLY</code> is the only scope currently supported. When <code>Scope</code> is set to <code>FAILED_FILES_ONLY</code>, the <code>CompletionReport</code> only contains information about files that the data repository task failed to process.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CompletionReport) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "path" in value:
        out["Path"] = value["path"]
    if "format" in value:
        import aws_sdk_fsx.types.report_format

        out["Format"] = aws_sdk_fsx.types.report_format.serialize_aws_json_1_1(
            value["format"]
        )
    if "scope" in value:
        import aws_sdk_fsx.types.report_scope

        out["Scope"] = aws_sdk_fsx.types.report_scope.serialize_aws_json_1_1(
            value["scope"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CompletionReport:
    out: CompletionReport = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    if "Path" in data:
        out["path"] = data["Path"]
    if "Format" in data:
        import aws_sdk_fsx.types.report_format

        out["format"] = aws_sdk_fsx.types.report_format.deserialize_aws_json_1_1(
            data["Format"]
        )
    if "Scope" in data:
        import aws_sdk_fsx.types.report_scope

        out["scope"] = aws_sdk_fsx.types.report_scope.deserialize_aws_json_1_1(
            data["Scope"]
        )
    return out
