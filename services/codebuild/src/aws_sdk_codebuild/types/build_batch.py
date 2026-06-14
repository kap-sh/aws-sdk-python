"""Generated from Smithy shape ``com.amazonaws.codebuild#BuildBatch``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.boolean
    import aws_sdk_codebuild.types.build_artifacts
    import aws_sdk_codebuild.types.build_artifacts_list
    import aws_sdk_codebuild.types.build_batch_phases
    import aws_sdk_codebuild.types.build_groups
    import aws_sdk_codebuild.types.build_report_arns
    import aws_sdk_codebuild.types.logs_config
    import aws_sdk_codebuild.types.non_empty_string
    import aws_sdk_codebuild.types.project_build_batch_config
    import aws_sdk_codebuild.types.project_cache
    import aws_sdk_codebuild.types.project_environment
    import aws_sdk_codebuild.types.project_file_system_locations
    import aws_sdk_codebuild.types.project_secondary_source_versions
    import aws_sdk_codebuild.types.project_source
    import aws_sdk_codebuild.types.project_sources
    import aws_sdk_codebuild.types.status_type
    import aws_sdk_codebuild.types.string
    import aws_sdk_codebuild.types.timestamp
    import aws_sdk_codebuild.types.vpc_config
    import aws_sdk_codebuild.types.wrapper_boolean
    import aws_sdk_codebuild.types.wrapper_int
    import aws_sdk_codebuild.types.wrapper_long


class BuildBatch(TypedDict):
    id: NotRequired["aws_sdk_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the batch build.</p>"""
    arn: NotRequired["aws_sdk_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the batch build.</p>"""
    start_time: NotRequired["aws_sdk_codebuild.types.timestamp.Timestamp"]
    """<p>The date and time that the batch build started.</p>"""
    end_time: NotRequired["aws_sdk_codebuild.types.timestamp.Timestamp"]
    """<p>The date and time that the batch build ended.</p>"""
    current_phase: NotRequired["aws_sdk_codebuild.types.string.String"]
    """<p>The current phase of the batch build.</p>"""
    build_batch_status: NotRequired["aws_sdk_codebuild.types.status_type.StatusType"]
    """<p>The status of the batch build.</p>"""
    source_version: NotRequired[
        "aws_sdk_codebuild.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier of the version of the source code to be built.</p>"""
    resolved_source_version: NotRequired[
        "aws_sdk_codebuild.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier of the resolved version of this batch build's source code.</p> <ul> <li> <p>For CodeCommit, GitHub, GitHub Enterprise, and BitBucket, the commit ID.</p> </li> <li> <p>For CodePipeline, the source revision provided by CodePipeline.</p> </li> <li> <p>For Amazon S3, this does not apply.</p> </li> </ul>"""
    project_name: NotRequired["aws_sdk_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The name of the batch build project.</p>"""
    phases: NotRequired["aws_sdk_codebuild.types.build_batch_phases.BuildBatchPhases"]
    """<p>An array of <code>BuildBatchPhase</code> objects the specify the phases of the batch build.</p>"""
    source: NotRequired["aws_sdk_codebuild.types.project_source.ProjectSource"]
    secondary_sources: NotRequired[
        "aws_sdk_codebuild.types.project_sources.ProjectSources"
    ]
    """<p>An array of <code>ProjectSource</code> objects that define the sources for the batch build.</p>"""
    secondary_source_versions: NotRequired[
        "aws_sdk_codebuild.types.project_secondary_source_versions.ProjectSecondarySourceVersions"
    ]
    """<p>An array of <code>ProjectSourceVersion</code> objects. Each <code>ProjectSourceVersion</code> must be one of: </p> <ul> <li> <p>For CodeCommit: the commit ID, branch, or Git tag to use.</p> </li> <li> <p>For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format <code>pr/pull-request-ID</code> (for example, <code>pr/25</code>). If a branch name is specified, the branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit ID is used.</p> </li> <li> <p>For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit ID is used.</p> </li> <li> <p>For Amazon S3: the version ID of the object that represents the build input ZIP file to use.</p> </li> </ul>"""
    artifacts: NotRequired["aws_sdk_codebuild.types.build_artifacts.BuildArtifacts"]
    """<p>A <code>BuildArtifacts</code> object the defines the build artifacts for this batch build.</p>"""
    secondary_artifacts: NotRequired[
        "aws_sdk_codebuild.types.build_artifacts_list.BuildArtifactsList"
    ]
    """<p>An array of <code>BuildArtifacts</code> objects the define the build artifacts for this batch build.</p>"""
    cache: NotRequired["aws_sdk_codebuild.types.project_cache.ProjectCache"]
    environment: NotRequired[
        "aws_sdk_codebuild.types.project_environment.ProjectEnvironment"
    ]
    service_role: NotRequired["aws_sdk_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The name of a service role used for builds in the batch.</p>"""
    log_config: NotRequired["aws_sdk_codebuild.types.logs_config.LogsConfig"]
    build_timeout_in_minutes: NotRequired[
        "aws_sdk_codebuild.types.wrapper_int.WrapperInt"
    ]
    """<p>Specifies the maximum amount of time, in minutes, that the build in a batch must be completed in.</p>"""
    queued_timeout_in_minutes: NotRequired[
        "aws_sdk_codebuild.types.wrapper_int.WrapperInt"
    ]
    """<p>Specifies the amount of time, in minutes, that the batch build is allowed to be queued before it times out.</p>"""
    complete: "aws_sdk_codebuild.types.boolean.Boolean"
    """<p>Indicates if the batch build is complete.</p>"""
    initiator: NotRequired["aws_sdk_codebuild.types.string.String"]
    """<p>The entity that started the batch build. Valid values include:</p> <ul> <li> <p>If CodePipeline started the build, the pipeline's name (for example, <code>codepipeline/my-demo-pipeline</code>).</p> </li> <li> <p>If a user started the build, the user's name.</p> </li> <li> <p>If the Jenkins plugin for CodeBuild started the build, the string <code>CodeBuild-Jenkins-Plugin</code>.</p> </li> </ul>"""
    vpc_config: NotRequired["aws_sdk_codebuild.types.vpc_config.VpcConfig"]
    encryption_key: NotRequired[
        "aws_sdk_codebuild.types.non_empty_string.NonEmptyString"
    ]
    """<p>The Key Management Service customer master key (CMK) to be used for encrypting the batch build output artifacts.</p> <note> <p>You can use a cross-account KMS key to encrypt the build output artifacts if your service role has permission to that key. </p> </note> <p>You can specify either the Amazon Resource Name (ARN) of the CMK or, if available, the CMK's alias (using the format <code>alias/<alias-name></code>).</p>"""
    build_batch_number: NotRequired["aws_sdk_codebuild.types.wrapper_long.WrapperLong"]
    """<p>The number of the batch build. For each project, the <code>buildBatchNumber</code> of its first batch build is <code>1</code>. The <code>buildBatchNumber</code> of each subsequent batch build is incremented by <code>1</code>. If a batch build is deleted, the <code>buildBatchNumber</code> of other batch builds does not change.</p>"""
    file_system_locations: NotRequired[
        "aws_sdk_codebuild.types.project_file_system_locations.ProjectFileSystemLocations"
    ]
    """<p>An array of <code>ProjectFileSystemLocation</code> objects for the batch build project. A <code>ProjectFileSystemLocation</code> object specifies the <code>identifier</code>, <code>location</code>, <code>mountOptions</code>, <code>mountPoint</code>, and <code>type</code> of a file system created using Amazon Elastic File System. </p>"""
    build_batch_config: NotRequired[
        "aws_sdk_codebuild.types.project_build_batch_config.ProjectBuildBatchConfig"
    ]
    build_groups: NotRequired["aws_sdk_codebuild.types.build_groups.BuildGroups"]
    """<p>An array of <code>BuildGroup</code> objects that define the build groups for the batch build.</p>"""
    debug_session_enabled: NotRequired[
        "aws_sdk_codebuild.types.wrapper_boolean.WrapperBoolean"
    ]
    r"""<p>Specifies if session debugging is enabled for this batch build. For more information, see <a href=\"https://docs.aws.amazon.com/codebuild/latest/userguide/session-manager.html\">Viewing a running build in Session Manager</a>. Batch session debugging is not supported for matrix batch builds.</p>"""
    report_arns: NotRequired[
        "aws_sdk_codebuild.types.build_report_arns.BuildReportArns"
    ]
    """<p>An array that contains the ARNs of reports created by merging reports from builds associated with this batch build.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BuildBatch) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
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
    if "current_phase" in value:
        out["currentPhase"] = value["current_phase"]
    if "build_batch_status" in value:
        import aws_sdk_codebuild.types.status_type

        out["buildBatchStatus"] = (
            aws_sdk_codebuild.types.status_type.serialize_aws_json_1_1(
                value["build_batch_status"]
            )
        )
    if "source_version" in value:
        out["sourceVersion"] = value["source_version"]
    if "resolved_source_version" in value:
        out["resolvedSourceVersion"] = value["resolved_source_version"]
    if "project_name" in value:
        out["projectName"] = value["project_name"]
    if "phases" in value:
        import aws_sdk_codebuild.types.build_batch_phases

        out["phases"] = (
            aws_sdk_codebuild.types.build_batch_phases.serialize_aws_json_1_1(
                value["phases"]
            )
        )
    if "source" in value:
        import aws_sdk_codebuild.types.project_source

        out["source"] = aws_sdk_codebuild.types.project_source.serialize_aws_json_1_1(
            value["source"]
        )
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
    if "artifacts" in value:
        import aws_sdk_codebuild.types.build_artifacts

        out["artifacts"] = (
            aws_sdk_codebuild.types.build_artifacts.serialize_aws_json_1_1(
                value["artifacts"]
            )
        )
    if "secondary_artifacts" in value:
        import aws_sdk_codebuild.types.build_artifacts_list

        out["secondaryArtifacts"] = (
            aws_sdk_codebuild.types.build_artifacts_list.serialize_aws_json_1_1(
                value["secondary_artifacts"]
            )
        )
    if "cache" in value:
        import aws_sdk_codebuild.types.project_cache

        out["cache"] = aws_sdk_codebuild.types.project_cache.serialize_aws_json_1_1(
            value["cache"]
        )
    if "environment" in value:
        import aws_sdk_codebuild.types.project_environment

        out["environment"] = (
            aws_sdk_codebuild.types.project_environment.serialize_aws_json_1_1(
                value["environment"]
            )
        )
    if "service_role" in value:
        out["serviceRole"] = value["service_role"]
    if "log_config" in value:
        import aws_sdk_codebuild.types.logs_config

        out["logConfig"] = aws_sdk_codebuild.types.logs_config.serialize_aws_json_1_1(
            value["log_config"]
        )
    if "build_timeout_in_minutes" in value:
        out["buildTimeoutInMinutes"] = value["build_timeout_in_minutes"]
    if "queued_timeout_in_minutes" in value:
        out["queuedTimeoutInMinutes"] = value["queued_timeout_in_minutes"]
    out["complete"] = value.get("complete", False)
    if "initiator" in value:
        out["initiator"] = value["initiator"]
    if "vpc_config" in value:
        import aws_sdk_codebuild.types.vpc_config

        out["vpcConfig"] = aws_sdk_codebuild.types.vpc_config.serialize_aws_json_1_1(
            value["vpc_config"]
        )
    if "encryption_key" in value:
        out["encryptionKey"] = value["encryption_key"]
    if "build_batch_number" in value:
        out["buildBatchNumber"] = value["build_batch_number"]
    if "file_system_locations" in value:
        import aws_sdk_codebuild.types.project_file_system_locations

        out["fileSystemLocations"] = (
            aws_sdk_codebuild.types.project_file_system_locations.serialize_aws_json_1_1(
                value["file_system_locations"]
            )
        )
    if "build_batch_config" in value:
        import aws_sdk_codebuild.types.project_build_batch_config

        out["buildBatchConfig"] = (
            aws_sdk_codebuild.types.project_build_batch_config.serialize_aws_json_1_1(
                value["build_batch_config"]
            )
        )
    if "build_groups" in value:
        import aws_sdk_codebuild.types.build_groups

        out["buildGroups"] = (
            aws_sdk_codebuild.types.build_groups.serialize_aws_json_1_1(
                value["build_groups"]
            )
        )
    if "debug_session_enabled" in value:
        out["debugSessionEnabled"] = value["debug_session_enabled"]
    if "report_arns" in value:
        import aws_sdk_codebuild.types.build_report_arns

        out["reportArns"] = (
            aws_sdk_codebuild.types.build_report_arns.serialize_aws_json_1_1(
                value["report_arns"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BuildBatch:
    out: BuildBatch = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
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
    if "currentPhase" in data:
        out["current_phase"] = data["currentPhase"]
    if "buildBatchStatus" in data:
        import aws_sdk_codebuild.types.status_type

        out["build_batch_status"] = (
            aws_sdk_codebuild.types.status_type.deserialize_aws_json_1_1(
                data["buildBatchStatus"]
            )
        )
    if "sourceVersion" in data:
        out["source_version"] = data["sourceVersion"]
    if "resolvedSourceVersion" in data:
        out["resolved_source_version"] = data["resolvedSourceVersion"]
    if "projectName" in data:
        out["project_name"] = data["projectName"]
    if "phases" in data:
        import aws_sdk_codebuild.types.build_batch_phases

        out["phases"] = (
            aws_sdk_codebuild.types.build_batch_phases.deserialize_aws_json_1_1(
                data["phases"]
            )
        )
    if "source" in data:
        import aws_sdk_codebuild.types.project_source

        out["source"] = aws_sdk_codebuild.types.project_source.deserialize_aws_json_1_1(
            data["source"]
        )
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
    if "artifacts" in data:
        import aws_sdk_codebuild.types.build_artifacts

        out["artifacts"] = (
            aws_sdk_codebuild.types.build_artifacts.deserialize_aws_json_1_1(
                data["artifacts"]
            )
        )
    if "secondaryArtifacts" in data:
        import aws_sdk_codebuild.types.build_artifacts_list

        out["secondary_artifacts"] = (
            aws_sdk_codebuild.types.build_artifacts_list.deserialize_aws_json_1_1(
                data["secondaryArtifacts"]
            )
        )
    if "cache" in data:
        import aws_sdk_codebuild.types.project_cache

        out["cache"] = aws_sdk_codebuild.types.project_cache.deserialize_aws_json_1_1(
            data["cache"]
        )
    if "environment" in data:
        import aws_sdk_codebuild.types.project_environment

        out["environment"] = (
            aws_sdk_codebuild.types.project_environment.deserialize_aws_json_1_1(
                data["environment"]
            )
        )
    if "serviceRole" in data:
        out["service_role"] = data["serviceRole"]
    if "logConfig" in data:
        import aws_sdk_codebuild.types.logs_config

        out["log_config"] = (
            aws_sdk_codebuild.types.logs_config.deserialize_aws_json_1_1(
                data["logConfig"]
            )
        )
    if "buildTimeoutInMinutes" in data:
        out["build_timeout_in_minutes"] = data["buildTimeoutInMinutes"]
    if "queuedTimeoutInMinutes" in data:
        out["queued_timeout_in_minutes"] = data["queuedTimeoutInMinutes"]
    if "complete" in data:
        out["complete"] = data["complete"]
    else:
        out["complete"] = False
    if "initiator" in data:
        out["initiator"] = data["initiator"]
    if "vpcConfig" in data:
        import aws_sdk_codebuild.types.vpc_config

        out["vpc_config"] = aws_sdk_codebuild.types.vpc_config.deserialize_aws_json_1_1(
            data["vpcConfig"]
        )
    if "encryptionKey" in data:
        out["encryption_key"] = data["encryptionKey"]
    if "buildBatchNumber" in data:
        out["build_batch_number"] = data["buildBatchNumber"]
    if "fileSystemLocations" in data:
        import aws_sdk_codebuild.types.project_file_system_locations

        out["file_system_locations"] = (
            aws_sdk_codebuild.types.project_file_system_locations.deserialize_aws_json_1_1(
                data["fileSystemLocations"]
            )
        )
    if "buildBatchConfig" in data:
        import aws_sdk_codebuild.types.project_build_batch_config

        out["build_batch_config"] = (
            aws_sdk_codebuild.types.project_build_batch_config.deserialize_aws_json_1_1(
                data["buildBatchConfig"]
            )
        )
    if "buildGroups" in data:
        import aws_sdk_codebuild.types.build_groups

        out["build_groups"] = (
            aws_sdk_codebuild.types.build_groups.deserialize_aws_json_1_1(
                data["buildGroups"]
            )
        )
    if "debugSessionEnabled" in data:
        out["debug_session_enabled"] = data["debugSessionEnabled"]
    if "reportArns" in data:
        import aws_sdk_codebuild.types.build_report_arns

        out["report_arns"] = (
            aws_sdk_codebuild.types.build_report_arns.deserialize_aws_json_1_1(
                data["reportArns"]
            )
        )
    return out
