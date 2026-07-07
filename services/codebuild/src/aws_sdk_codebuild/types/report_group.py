"""Generated from Smithy shape ``com.amazonaws.codebuild#ReportGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.non_empty_string
    import aws_sdk_codebuild.types.report_export_config
    import aws_sdk_codebuild.types.report_group_name
    import aws_sdk_codebuild.types.report_group_status_type
    import aws_sdk_codebuild.types.report_type
    import aws_sdk_codebuild.types.tag_list
    import aws_sdk_codebuild.types.timestamp


class ReportGroup(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the <code>ReportGroup</code>. </p>"""
    name: NotRequired["aws_sdk_codebuild.types.report_group_name.ReportGroupName"]
    """<p>The name of the <code>ReportGroup</code>. </p>"""
    type: NotRequired["aws_sdk_codebuild.types.report_type.ReportType"]
    """<p>The type of the <code>ReportGroup</code>. This can be one of the following values:</p> <dl> <dt>CODE_COVERAGE</dt> <dd> <p>The report group contains code coverage reports.</p> </dd> <dt>TEST</dt> <dd> <p>The report group contains test reports.</p> </dd> </dl>"""
    export_config: NotRequired[
        "aws_sdk_codebuild.types.report_export_config.ReportExportConfig"
    ]
    """<p>Information about the destination where the raw data of this <code>ReportGroup</code> is exported. </p>"""
    created: NotRequired["aws_sdk_codebuild.types.timestamp.Timestamp"]
    """<p>The date and time this <code>ReportGroup</code> was created. </p>"""
    last_modified: NotRequired["aws_sdk_codebuild.types.timestamp.Timestamp"]
    """<p>The date and time this <code>ReportGroup</code> was last modified. </p>"""
    tags: NotRequired["aws_sdk_codebuild.types.tag_list.TagList"]
    """<p>A list of tag key and value pairs associated with this report group. </p> <p>These tags are available for use by Amazon Web Services services that support CodeBuild report group tags.</p>"""
    status: NotRequired[
        "aws_sdk_codebuild.types.report_group_status_type.ReportGroupStatusType"
    ]
    """<p>The status of the report group. This property is read-only.</p> <p>This can be one of the following values:</p> <dl> <dt>ACTIVE</dt> <dd> <p>The report group is active.</p> </dd> <dt>DELETING</dt> <dd> <p>The report group is in the process of being deleted.</p> </dd> </dl>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportGroup) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "type" in value:
        import aws_sdk_codebuild.types.report_type

        out["type"] = aws_sdk_codebuild.types.report_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "export_config" in value:
        import aws_sdk_codebuild.types.report_export_config

        out["exportConfig"] = (
            aws_sdk_codebuild.types.report_export_config.serialize_aws_json_1_1(
                value["export_config"]
            )
        )
    if "created" in value:
        import aws_sdk_codebuild.types.timestamp

        out["created"] = aws_sdk_codebuild.types.timestamp.serialize_aws_json_1_1(
            value["created"]
        )
    if "last_modified" in value:
        import aws_sdk_codebuild.types.timestamp

        out["lastModified"] = aws_sdk_codebuild.types.timestamp.serialize_aws_json_1_1(
            value["last_modified"]
        )
    if "tags" in value:
        import aws_sdk_codebuild.types.tag_list

        out["tags"] = aws_sdk_codebuild.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "status" in value:
        import aws_sdk_codebuild.types.report_group_status_type

        out["status"] = (
            aws_sdk_codebuild.types.report_group_status_type.serialize_aws_json_1_1(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReportGroup:
    out: ReportGroup = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "name" in data:
        out["name"] = data["name"]
    if "type" in data:
        import aws_sdk_codebuild.types.report_type

        out["type"] = aws_sdk_codebuild.types.report_type.deserialize_aws_json_1_1(
            data["type"]
        )
    if "exportConfig" in data:
        import aws_sdk_codebuild.types.report_export_config

        out["export_config"] = (
            aws_sdk_codebuild.types.report_export_config.deserialize_aws_json_1_1(
                data["exportConfig"]
            )
        )
    if "created" in data:
        import aws_sdk_codebuild.types.timestamp

        out["created"] = aws_sdk_codebuild.types.timestamp.deserialize_aws_json_1_1(
            data["created"]
        )
    if "lastModified" in data:
        import aws_sdk_codebuild.types.timestamp

        out["last_modified"] = (
            aws_sdk_codebuild.types.timestamp.deserialize_aws_json_1_1(
                data["lastModified"]
            )
        )
    if "tags" in data:
        import aws_sdk_codebuild.types.tag_list

        out["tags"] = aws_sdk_codebuild.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    if "status" in data:
        import aws_sdk_codebuild.types.report_group_status_type

        out["status"] = (
            aws_sdk_codebuild.types.report_group_status_type.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    return out
