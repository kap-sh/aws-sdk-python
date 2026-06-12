"""Generated from Smithy shape ``com.amazonaws.codebuild#Sandbox``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.logs_config
    import aws_sdk_codebuild.types.non_empty_string
    import aws_sdk_codebuild.types.project_environment
    import aws_sdk_codebuild.types.project_file_system_locations
    import aws_sdk_codebuild.types.project_secondary_source_versions
    import aws_sdk_codebuild.types.project_source
    import aws_sdk_codebuild.types.project_sources
    import aws_sdk_codebuild.types.sandbox_session
    import aws_sdk_codebuild.types.string
    import aws_sdk_codebuild.types.timestamp
    import aws_sdk_codebuild.types.vpc_config
    import aws_sdk_codebuild.types.wrapper_int


class Sandbox(TypedDict):
    id: NotRequired["aws_sdk_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The ID of the sandbox.</p>"""
    arn: NotRequired["aws_sdk_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the sandbox.</p>"""
    project_name: NotRequired["aws_sdk_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The CodeBuild project name.</p>"""
    request_time: NotRequired["aws_sdk_codebuild.types.timestamp.Timestamp"]
    """<p>When the sandbox process was initially requested, expressed in Unix time format.</p>"""
    start_time: NotRequired["aws_sdk_codebuild.types.timestamp.Timestamp"]
    """<p>When the sandbox process started, expressed in Unix time format.</p>"""
    end_time: NotRequired["aws_sdk_codebuild.types.timestamp.Timestamp"]
    """<p>When the sandbox process ended, expressed in Unix time format.</p>"""
    status: NotRequired["aws_sdk_codebuild.types.string.String"]
    """<p>The status of the sandbox.</p>"""
    source: NotRequired["aws_sdk_codebuild.types.project_source.ProjectSource"]
    source_version: NotRequired[
        "aws_sdk_codebuild.types.non_empty_string.NonEmptyString"
    ]
    """<p>Any version identifier for the version of the sandbox to be built.</p>"""
    secondary_sources: NotRequired[
        "aws_sdk_codebuild.types.project_sources.ProjectSources"
    ]
    """<p> An array of <code>ProjectSource</code> objects. </p>"""
    secondary_source_versions: NotRequired[
        "aws_sdk_codebuild.types.project_secondary_source_versions.ProjectSecondarySourceVersions"
    ]
    """<p> An array of <code>ProjectSourceVersion</code> objects.</p>"""
    environment: NotRequired[
        "aws_sdk_codebuild.types.project_environment.ProjectEnvironment"
    ]
    file_system_locations: NotRequired[
        "aws_sdk_codebuild.types.project_file_system_locations.ProjectFileSystemLocations"
    ]
    """<p> An array of <code>ProjectFileSystemLocation</code> objects for a CodeBuild build project. A <code>ProjectFileSystemLocation</code> object specifies the <code>identifier</code>, <code>location</code>, <code>mountOptions</code>, <code>mountPoint</code>, and <code>type</code> of a file system created using Amazon Elastic File System. </p>"""
    timeout_in_minutes: NotRequired["aws_sdk_codebuild.types.wrapper_int.WrapperInt"]
    """<p>How long, in minutes, from 5 to 2160 (36 hours), for CodeBuild to wait before timing out this sandbox if it does not get marked as completed.</p>"""
    queued_timeout_in_minutes: NotRequired[
        "aws_sdk_codebuild.types.wrapper_int.WrapperInt"
    ]
    """<p>The number of minutes a sandbox is allowed to be queued before it times out. </p>"""
    vpc_config: NotRequired["aws_sdk_codebuild.types.vpc_config.VpcConfig"]
    log_config: NotRequired["aws_sdk_codebuild.types.logs_config.LogsConfig"]
    encryption_key: NotRequired[
        "aws_sdk_codebuild.types.non_empty_string.NonEmptyString"
    ]
    """<p>The Key Management Service customer master key (CMK) to be used for encrypting the sandbox output artifacts.</p>"""
    service_role: NotRequired["aws_sdk_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The name of a service role used for this sandbox.</p>"""
    current_session: NotRequired[
        "aws_sdk_codebuild.types.sandbox_session.SandboxSession"
    ]
    """<p>The current session for the sandbox.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Sandbox) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "project_name" in value:
        out["projectName"] = value["project_name"]
    if "request_time" in value:
        import aws_sdk_codebuild.types.timestamp

        out["requestTime"] = aws_sdk_codebuild.types.timestamp.serialize_aws_json_1_1(
            value["request_time"]
        )
    if "start_time" in value:
        import aws_sdk_codebuild.types.timestamp

        out["startTime"] = aws_sdk_codebuild.types.timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_codebuild.types.timestamp

        out["endTime"] = aws_sdk_codebuild.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "status" in value:
        out["status"] = value["status"]
    if "source" in value:
        import aws_sdk_codebuild.types.project_source

        out["source"] = aws_sdk_codebuild.types.project_source.serialize_aws_json_1_1(
            value["source"]
        )
    if "source_version" in value:
        out["sourceVersion"] = value["source_version"]
    if "secondary_sources" in value:
        import aws_sdk_codebuild.types.project_sources

        out["secondarySources"] = (
            aws_sdk_codebuild.types.project_sources.serialize_aws_json_1_1(
                value["secondary_sources"]
            )
        )
    if "secondary_source_versions" in value:
        import aws_sdk_codebuild.types.project_secondary_source_versions

        out["secondarySourceVersions"] = (
            aws_sdk_codebuild.types.project_secondary_source_versions.serialize_aws_json_1_1(
                value["secondary_source_versions"]
            )
        )
    if "environment" in value:
        import aws_sdk_codebuild.types.project_environment

        out["environment"] = (
            aws_sdk_codebuild.types.project_environment.serialize_aws_json_1_1(
                value["environment"]
            )
        )
    if "file_system_locations" in value:
        import aws_sdk_codebuild.types.project_file_system_locations

        out["fileSystemLocations"] = (
            aws_sdk_codebuild.types.project_file_system_locations.serialize_aws_json_1_1(
                value["file_system_locations"]
            )
        )
    if "timeout_in_minutes" in value:
        out["timeoutInMinutes"] = value["timeout_in_minutes"]
    if "queued_timeout_in_minutes" in value:
        out["queuedTimeoutInMinutes"] = value["queued_timeout_in_minutes"]
    if "vpc_config" in value:
        import aws_sdk_codebuild.types.vpc_config

        out["vpcConfig"] = aws_sdk_codebuild.types.vpc_config.serialize_aws_json_1_1(
            value["vpc_config"]
        )
    if "log_config" in value:
        import aws_sdk_codebuild.types.logs_config

        out["logConfig"] = aws_sdk_codebuild.types.logs_config.serialize_aws_json_1_1(
            value["log_config"]
        )
    if "encryption_key" in value:
        out["encryptionKey"] = value["encryption_key"]
    if "service_role" in value:
        out["serviceRole"] = value["service_role"]
    if "current_session" in value:
        import aws_sdk_codebuild.types.sandbox_session

        out["currentSession"] = (
            aws_sdk_codebuild.types.sandbox_session.serialize_aws_json_1_1(
                value["current_session"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Sandbox:
    out: Sandbox = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "projectName" in data:
        out["project_name"] = data["projectName"]
    if "requestTime" in data:
        import aws_sdk_codebuild.types.timestamp

        out["request_time"] = (
            aws_sdk_codebuild.types.timestamp.deserialize_aws_json_1_1(
                data["requestTime"]
            )
        )
    if "startTime" in data:
        import aws_sdk_codebuild.types.timestamp

        out["start_time"] = aws_sdk_codebuild.types.timestamp.deserialize_aws_json_1_1(
            data["startTime"]
        )
    if "endTime" in data:
        import aws_sdk_codebuild.types.timestamp

        out["end_time"] = aws_sdk_codebuild.types.timestamp.deserialize_aws_json_1_1(
            data["endTime"]
        )
    if "status" in data:
        out["status"] = data["status"]
    if "source" in data:
        import aws_sdk_codebuild.types.project_source

        out["source"] = aws_sdk_codebuild.types.project_source.deserialize_aws_json_1_1(
            data["source"]
        )
    if "sourceVersion" in data:
        out["source_version"] = data["sourceVersion"]
    if "secondarySources" in data:
        import aws_sdk_codebuild.types.project_sources

        out["secondary_sources"] = (
            aws_sdk_codebuild.types.project_sources.deserialize_aws_json_1_1(
                data["secondarySources"]
            )
        )
    if "secondarySourceVersions" in data:
        import aws_sdk_codebuild.types.project_secondary_source_versions

        out["secondary_source_versions"] = (
            aws_sdk_codebuild.types.project_secondary_source_versions.deserialize_aws_json_1_1(
                data["secondarySourceVersions"]
            )
        )
    if "environment" in data:
        import aws_sdk_codebuild.types.project_environment

        out["environment"] = (
            aws_sdk_codebuild.types.project_environment.deserialize_aws_json_1_1(
                data["environment"]
            )
        )
    if "fileSystemLocations" in data:
        import aws_sdk_codebuild.types.project_file_system_locations

        out["file_system_locations"] = (
            aws_sdk_codebuild.types.project_file_system_locations.deserialize_aws_json_1_1(
                data["fileSystemLocations"]
            )
        )
    if "timeoutInMinutes" in data:
        out["timeout_in_minutes"] = data["timeoutInMinutes"]
    if "queuedTimeoutInMinutes" in data:
        out["queued_timeout_in_minutes"] = data["queuedTimeoutInMinutes"]
    if "vpcConfig" in data:
        import aws_sdk_codebuild.types.vpc_config

        out["vpc_config"] = aws_sdk_codebuild.types.vpc_config.deserialize_aws_json_1_1(
            data["vpcConfig"]
        )
    if "logConfig" in data:
        import aws_sdk_codebuild.types.logs_config

        out["log_config"] = (
            aws_sdk_codebuild.types.logs_config.deserialize_aws_json_1_1(
                data["logConfig"]
            )
        )
    if "encryptionKey" in data:
        out["encryption_key"] = data["encryptionKey"]
    if "serviceRole" in data:
        out["service_role"] = data["serviceRole"]
    if "currentSession" in data:
        import aws_sdk_codebuild.types.sandbox_session

        out["current_session"] = (
            aws_sdk_codebuild.types.sandbox_session.deserialize_aws_json_1_1(
                data["currentSession"]
            )
        )
    return out
