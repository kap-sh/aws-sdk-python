"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCodeBuildProjectDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_code_build_project_artifacts_list
    import aws_sdk_securityhub.types.aws_code_build_project_environment
    import aws_sdk_securityhub.types.aws_code_build_project_logs_config_details
    import aws_sdk_securityhub.types.aws_code_build_project_source
    import aws_sdk_securityhub.types.aws_code_build_project_vpc_config
    import aws_sdk_securityhub.types.non_empty_string


class AwsCodeBuildProjectDetails(TypedDict, closed=True):
    encryption_key: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The KMS key used to encrypt the build output artifacts.</p> <p>You can specify either the ARN of the KMS key or, if available, the KMS key alias (using the format alias/alias-name). </p>"""
    artifacts: NotRequired[
        "aws_sdk_securityhub.types.aws_code_build_project_artifacts_list.AwsCodeBuildProjectArtifactsList"
    ]
    """<p>Information about the build artifacts for the CodeBuild project.</p>"""
    environment: NotRequired[
        "aws_sdk_securityhub.types.aws_code_build_project_environment.AwsCodeBuildProjectEnvironment"
    ]
    """<p>Information about the build environment for this build project.</p>"""
    name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the build project.</p>"""
    source: NotRequired[
        "aws_sdk_securityhub.types.aws_code_build_project_source.AwsCodeBuildProjectSource"
    ]
    """<p>Information about the build input source code for this build project.</p>"""
    service_role: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the IAM role that enables CodeBuild to interact with dependent Amazon Web Services services on behalf of the Amazon Web Services account.</p>"""
    logs_config: NotRequired[
        "aws_sdk_securityhub.types.aws_code_build_project_logs_config_details.AwsCodeBuildProjectLogsConfigDetails"
    ]
    """<p>Information about logs for the build project.</p>"""
    vpc_config: NotRequired[
        "aws_sdk_securityhub.types.aws_code_build_project_vpc_config.AwsCodeBuildProjectVpcConfig"
    ]
    """<p>Information about the VPC configuration that CodeBuild accesses.</p>"""
    secondary_artifacts: NotRequired[
        "aws_sdk_securityhub.types.aws_code_build_project_artifacts_list.AwsCodeBuildProjectArtifactsList"
    ]
    """<p>Information about the secondary artifacts for the CodeBuild project.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsCodeBuildProjectDetails) -> dict:
    out: dict = {}
    if "encryption_key" in value:
        out["EncryptionKey"] = value["encryption_key"]
    if "artifacts" in value:
        import aws_sdk_securityhub.types.aws_code_build_project_artifacts_list

        out["Artifacts"] = (
            aws_sdk_securityhub.types.aws_code_build_project_artifacts_list.serialize_json(
                value["artifacts"]
            )
        )
    if "environment" in value:
        import aws_sdk_securityhub.types.aws_code_build_project_environment

        out["Environment"] = (
            aws_sdk_securityhub.types.aws_code_build_project_environment.serialize_json(
                value["environment"]
            )
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "source" in value:
        import aws_sdk_securityhub.types.aws_code_build_project_source

        out["Source"] = (
            aws_sdk_securityhub.types.aws_code_build_project_source.serialize_json(
                value["source"]
            )
        )
    if "service_role" in value:
        out["ServiceRole"] = value["service_role"]
    if "logs_config" in value:
        import aws_sdk_securityhub.types.aws_code_build_project_logs_config_details

        out["LogsConfig"] = (
            aws_sdk_securityhub.types.aws_code_build_project_logs_config_details.serialize_json(
                value["logs_config"]
            )
        )
    if "vpc_config" in value:
        import aws_sdk_securityhub.types.aws_code_build_project_vpc_config

        out["VpcConfig"] = (
            aws_sdk_securityhub.types.aws_code_build_project_vpc_config.serialize_json(
                value["vpc_config"]
            )
        )
    if "secondary_artifacts" in value:
        import aws_sdk_securityhub.types.aws_code_build_project_artifacts_list

        out["SecondaryArtifacts"] = (
            aws_sdk_securityhub.types.aws_code_build_project_artifacts_list.serialize_json(
                value["secondary_artifacts"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsCodeBuildProjectDetails:
    out: AwsCodeBuildProjectDetails = {}  # type: ignore[typeddict-item]
    if "EncryptionKey" in data:
        out["encryption_key"] = data["EncryptionKey"]
    if "Artifacts" in data:
        import aws_sdk_securityhub.types.aws_code_build_project_artifacts_list

        out["artifacts"] = (
            aws_sdk_securityhub.types.aws_code_build_project_artifacts_list.deserialize_json(
                data["Artifacts"]
            )
        )
    if "Environment" in data:
        import aws_sdk_securityhub.types.aws_code_build_project_environment

        out["environment"] = (
            aws_sdk_securityhub.types.aws_code_build_project_environment.deserialize_json(
                data["Environment"]
            )
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "Source" in data:
        import aws_sdk_securityhub.types.aws_code_build_project_source

        out["source"] = (
            aws_sdk_securityhub.types.aws_code_build_project_source.deserialize_json(
                data["Source"]
            )
        )
    if "ServiceRole" in data:
        out["service_role"] = data["ServiceRole"]
    if "LogsConfig" in data:
        import aws_sdk_securityhub.types.aws_code_build_project_logs_config_details

        out["logs_config"] = (
            aws_sdk_securityhub.types.aws_code_build_project_logs_config_details.deserialize_json(
                data["LogsConfig"]
            )
        )
    if "VpcConfig" in data:
        import aws_sdk_securityhub.types.aws_code_build_project_vpc_config

        out["vpc_config"] = (
            aws_sdk_securityhub.types.aws_code_build_project_vpc_config.deserialize_json(
                data["VpcConfig"]
            )
        )
    if "SecondaryArtifacts" in data:
        import aws_sdk_securityhub.types.aws_code_build_project_artifacts_list

        out["secondary_artifacts"] = (
            aws_sdk_securityhub.types.aws_code_build_project_artifacts_list.deserialize_json(
                data["SecondaryArtifacts"]
            )
        )
    return out
