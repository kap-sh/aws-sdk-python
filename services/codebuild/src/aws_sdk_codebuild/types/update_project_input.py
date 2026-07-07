"""Generated from Smithy shape ``com.amazonaws.codebuild#UpdateProjectInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codebuild.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.build_time_out
    import aws_sdk_codebuild.types.logs_config
    import aws_sdk_codebuild.types.non_empty_string
    import aws_sdk_codebuild.types.project_artifacts
    import aws_sdk_codebuild.types.project_artifacts_list
    import aws_sdk_codebuild.types.project_build_batch_config
    import aws_sdk_codebuild.types.project_cache
    import aws_sdk_codebuild.types.project_description
    import aws_sdk_codebuild.types.project_environment
    import aws_sdk_codebuild.types.project_file_system_locations
    import aws_sdk_codebuild.types.project_secondary_source_versions
    import aws_sdk_codebuild.types.project_source
    import aws_sdk_codebuild.types.project_sources
    import aws_sdk_codebuild.types.string
    import aws_sdk_codebuild.types.tag_list
    import aws_sdk_codebuild.types.time_out
    import aws_sdk_codebuild.types.vpc_config
    import aws_sdk_codebuild.types.wrapper_boolean
    import aws_sdk_codebuild.types.wrapper_int


class UpdateProjectInput(TypedDict, closed=True):
    name: "aws_sdk_codebuild.types.non_empty_string.NonEmptyString"
    """<p>The name of the build project.</p> <note> <p>You cannot change a build project's name.</p> </note>"""
    description: NotRequired[
        "aws_sdk_codebuild.types.project_description.ProjectDescription"
    ]
    """<p>A new or replacement description of the build project.</p>"""
    source: NotRequired["aws_sdk_codebuild.types.project_source.ProjectSource"]
    """<p>Information to be changed about the build input source code for the build project.</p>"""
    secondary_sources: NotRequired[
        "aws_sdk_codebuild.types.project_sources.ProjectSources"
    ]
    """<p> An array of <code>ProjectSource</code> objects. </p>"""
    source_version: NotRequired["aws_sdk_codebuild.types.string.String"]
    r"""<p> A version of the build input to be built for this project. If not specified, the latest version is used. If specified, it must be one of: </p> <ul> <li> <p>For CodeCommit: the commit ID, branch, or Git tag to use.</p> </li> <li> <p>For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format <code>pr/pull-request-ID</code> (for example <code>pr/25</code>). If a branch name is specified, the branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit ID is used.</p> </li> <li> <p>For GitLab: the commit ID, branch, or Git tag to use.</p> </li> <li> <p>For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit ID is used.</p> </li> <li> <p>For Amazon S3: the version ID of the object that represents the build input ZIP file to use.</p> </li> </ul> <p> If <code>sourceVersion</code> is specified at the build level, then that version takes precedence over this <code>sourceVersion</code> (at the project level). </p> <p> For more information, see <a href=\"https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html\">Source Version Sample with CodeBuild</a> in the <i>CodeBuild User Guide</i>. </p>"""
    secondary_source_versions: NotRequired[
        "aws_sdk_codebuild.types.project_secondary_source_versions.ProjectSecondarySourceVersions"
    ]
    """<p> An array of <code>ProjectSourceVersion</code> objects. If <code>secondarySourceVersions</code> is specified at the build level, then they take over these <code>secondarySourceVersions</code> (at the project level). </p>"""
    artifacts: NotRequired["aws_sdk_codebuild.types.project_artifacts.ProjectArtifacts"]
    """<p>Information to be changed about the build output artifacts for the build project.</p>"""
    secondary_artifacts: NotRequired[
        "aws_sdk_codebuild.types.project_artifacts_list.ProjectArtifactsList"
    ]
    """<p> An array of <code>ProjectArtifact</code> objects. </p>"""
    cache: NotRequired["aws_sdk_codebuild.types.project_cache.ProjectCache"]
    """<p>Stores recently used information so that it can be quickly accessed at a later time.</p>"""
    environment: NotRequired[
        "aws_sdk_codebuild.types.project_environment.ProjectEnvironment"
    ]
    """<p>Information to be changed about the build environment for the build project.</p>"""
    service_role: NotRequired["aws_sdk_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The replacement ARN of the IAM role that enables CodeBuild to interact with dependent Amazon Web Services services on behalf of the Amazon Web Services account.</p>"""
    timeout_in_minutes: NotRequired[
        "aws_sdk_codebuild.types.build_time_out.BuildTimeOut"
    ]
    """<p>The replacement value in minutes, from 5 to 2160 (36 hours), for CodeBuild to wait before timing out any related build that did not get marked as completed.</p>"""
    queued_timeout_in_minutes: NotRequired["aws_sdk_codebuild.types.time_out.TimeOut"]
    """<p> The number of minutes a build is allowed to be queued before it times out. </p>"""
    encryption_key: NotRequired[
        "aws_sdk_codebuild.types.non_empty_string.NonEmptyString"
    ]
    """<p>The Key Management Service customer master key (CMK) to be used for encrypting the build output artifacts.</p> <note> <p> You can use a cross-account KMS key to encrypt the build output artifacts if your service role has permission to that key. </p> </note> <p>You can specify either the Amazon Resource Name (ARN) of the CMK or, if available, the CMK's alias (using the format <code>alias/<alias-name></code>). </p>"""
    tags: NotRequired["aws_sdk_codebuild.types.tag_list.TagList"]
    """<p>An updated list of tag key and value pairs associated with this build project.</p> <p>These tags are available for use by Amazon Web Services services that support CodeBuild build project tags.</p>"""
    vpc_config: NotRequired["aws_sdk_codebuild.types.vpc_config.VpcConfig"]
    """<p>VpcConfig enables CodeBuild to access resources in an Amazon VPC.</p>"""
    badge_enabled: NotRequired["aws_sdk_codebuild.types.wrapper_boolean.WrapperBoolean"]
    """<p>Set this to true to generate a publicly accessible URL for your project's build badge.</p>"""
    logs_config: NotRequired["aws_sdk_codebuild.types.logs_config.LogsConfig"]
    """<p> Information about logs for the build project. A project can create logs in CloudWatch Logs, logs in an S3 bucket, or both. </p>"""
    file_system_locations: NotRequired[
        "aws_sdk_codebuild.types.project_file_system_locations.ProjectFileSystemLocations"
    ]
    """<p> An array of <code>ProjectFileSystemLocation</code> objects for a CodeBuild build project. A <code>ProjectFileSystemLocation</code> object specifies the <code>identifier</code>, <code>location</code>, <code>mountOptions</code>, <code>mountPoint</code>, and <code>type</code> of a file system created using Amazon Elastic File System. </p>"""
    build_batch_config: NotRequired[
        "aws_sdk_codebuild.types.project_build_batch_config.ProjectBuildBatchConfig"
    ]
    concurrent_build_limit: NotRequired[
        "aws_sdk_codebuild.types.wrapper_int.WrapperInt"
    ]
    """<p>The maximum number of concurrent builds that are allowed for this project.</p> <p>New builds are only started if the current number of builds is less than or equal to this limit. If the current build count meets this limit, new builds are throttled and are not run.</p> <p>To remove this limit, set this value to -1.</p>"""
    auto_retry_limit: NotRequired["aws_sdk_codebuild.types.wrapper_int.WrapperInt"]
    """<p>The maximum number of additional automatic retries after a failed build. For example, if the auto-retry limit is set to 2, CodeBuild will call the <code>RetryBuild</code> API to automatically retry your build for up to 2 additional times.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateProjectInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
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
    if "source_version" in value:
        out["sourceVersion"] = value["source_version"]
    if "secondary_source_versions" in value:
        import aws_sdk_codebuild.types.project_secondary_source_versions

        out["secondarySourceVersions"] = (
            aws_sdk_codebuild.types.project_secondary_source_versions.serialize_aws_json_1_1(
                value["secondary_source_versions"]
            )
        )
    if "artifacts" in value:
        import aws_sdk_codebuild.types.project_artifacts

        out["artifacts"] = (
            aws_sdk_codebuild.types.project_artifacts.serialize_aws_json_1_1(
                value["artifacts"]
            )
        )
    if "secondary_artifacts" in value:
        import aws_sdk_codebuild.types.project_artifacts_list

        out["secondaryArtifacts"] = (
            aws_sdk_codebuild.types.project_artifacts_list.serialize_aws_json_1_1(
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
    if "timeout_in_minutes" in value:
        out["timeoutInMinutes"] = value["timeout_in_minutes"]
    if "queued_timeout_in_minutes" in value:
        out["queuedTimeoutInMinutes"] = value["queued_timeout_in_minutes"]
    if "encryption_key" in value:
        out["encryptionKey"] = value["encryption_key"]
    if "tags" in value:
        import aws_sdk_codebuild.types.tag_list

        out["tags"] = aws_sdk_codebuild.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "vpc_config" in value:
        import aws_sdk_codebuild.types.vpc_config

        out["vpcConfig"] = aws_sdk_codebuild.types.vpc_config.serialize_aws_json_1_1(
            value["vpc_config"]
        )
    if "badge_enabled" in value:
        out["badgeEnabled"] = value["badge_enabled"]
    if "logs_config" in value:
        import aws_sdk_codebuild.types.logs_config

        out["logsConfig"] = aws_sdk_codebuild.types.logs_config.serialize_aws_json_1_1(
            value["logs_config"]
        )
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
    if "concurrent_build_limit" in value:
        out["concurrentBuildLimit"] = value["concurrent_build_limit"]
    if "auto_retry_limit" in value:
        out["autoRetryLimit"] = value["auto_retry_limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateProjectInput:
    out: UpdateProjectInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateProjectInput.name required")
    if "description" in data:
        out["description"] = data["description"]
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
    if "sourceVersion" in data:
        out["source_version"] = data["sourceVersion"]
    if "secondarySourceVersions" in data:
        import aws_sdk_codebuild.types.project_secondary_source_versions

        out["secondary_source_versions"] = (
            aws_sdk_codebuild.types.project_secondary_source_versions.deserialize_aws_json_1_1(
                data["secondarySourceVersions"]
            )
        )
    if "artifacts" in data:
        import aws_sdk_codebuild.types.project_artifacts

        out["artifacts"] = (
            aws_sdk_codebuild.types.project_artifacts.deserialize_aws_json_1_1(
                data["artifacts"]
            )
        )
    if "secondaryArtifacts" in data:
        import aws_sdk_codebuild.types.project_artifacts_list

        out["secondary_artifacts"] = (
            aws_sdk_codebuild.types.project_artifacts_list.deserialize_aws_json_1_1(
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
    if "timeoutInMinutes" in data:
        out["timeout_in_minutes"] = data["timeoutInMinutes"]
    if "queuedTimeoutInMinutes" in data:
        out["queued_timeout_in_minutes"] = data["queuedTimeoutInMinutes"]
    if "encryptionKey" in data:
        out["encryption_key"] = data["encryptionKey"]
    if "tags" in data:
        import aws_sdk_codebuild.types.tag_list

        out["tags"] = aws_sdk_codebuild.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    if "vpcConfig" in data:
        import aws_sdk_codebuild.types.vpc_config

        out["vpc_config"] = aws_sdk_codebuild.types.vpc_config.deserialize_aws_json_1_1(
            data["vpcConfig"]
        )
    if "badgeEnabled" in data:
        out["badge_enabled"] = data["badgeEnabled"]
    if "logsConfig" in data:
        import aws_sdk_codebuild.types.logs_config

        out["logs_config"] = (
            aws_sdk_codebuild.types.logs_config.deserialize_aws_json_1_1(
                data["logsConfig"]
            )
        )
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
    if "concurrentBuildLimit" in data:
        out["concurrent_build_limit"] = data["concurrentBuildLimit"]
    if "autoRetryLimit" in data:
        out["auto_retry_limit"] = data["autoRetryLimit"]
    return out
