"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCodeBuildProjectDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_code_build_project_artifacts_list
    import capo_securityhub.types.aws_code_build_project_environment
    import capo_securityhub.types.aws_code_build_project_logs_config_details
    import capo_securityhub.types.aws_code_build_project_source
    import capo_securityhub.types.aws_code_build_project_vpc_config
    import capo_securityhub.types.non_empty_string


class AwsCodeBuildProjectDetails(TypedDict, closed=True):
    encryption_key: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The KMS key used to encrypt the build output artifacts.</p> <p>You can specify either the ARN of the KMS key or, if available, the KMS key alias (using the format alias/alias-name). </p>"""
    artifacts: NotRequired[
        "capo_securityhub.types.aws_code_build_project_artifacts_list.AwsCodeBuildProjectArtifactsList"
    ]
    """<p>Information about the build artifacts for the CodeBuild project.</p>"""
    environment: NotRequired[
        "capo_securityhub.types.aws_code_build_project_environment.AwsCodeBuildProjectEnvironment"
    ]
    """<p>Information about the build environment for this build project.</p>"""
    name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the build project.</p>"""
    source: NotRequired[
        "capo_securityhub.types.aws_code_build_project_source.AwsCodeBuildProjectSource"
    ]
    """<p>Information about the build input source code for this build project.</p>"""
    service_role: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the IAM role that enables CodeBuild to interact with dependent Amazon Web Services services on behalf of the Amazon Web Services account.</p>"""
    logs_config: NotRequired[
        "capo_securityhub.types.aws_code_build_project_logs_config_details.AwsCodeBuildProjectLogsConfigDetails"
    ]
    """<p>Information about logs for the build project.</p>"""
    vpc_config: NotRequired[
        "capo_securityhub.types.aws_code_build_project_vpc_config.AwsCodeBuildProjectVpcConfig"
    ]
    """<p>Information about the VPC configuration that CodeBuild accesses.</p>"""
    secondary_artifacts: NotRequired[
        "capo_securityhub.types.aws_code_build_project_artifacts_list.AwsCodeBuildProjectArtifactsList"
    ]
    """<p>Information about the secondary artifacts for the CodeBuild project.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsCodeBuildProjectDetails) -> dict:
    out: dict = {}
    if "encryption_key" in value:
        out["EncryptionKey"] = value["encryption_key"]
    if "artifacts" in value:
        import capo_securityhub.types.aws_code_build_project_artifacts_list

        out["Artifacts"] = (
            capo_securityhub.types.aws_code_build_project_artifacts_list.serialize_json(
                value["artifacts"]
            )
        )
    if "environment" in value:
        import capo_securityhub.types.aws_code_build_project_environment

        out["Environment"] = (
            capo_securityhub.types.aws_code_build_project_environment.serialize_json(
                value["environment"]
            )
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "source" in value:
        import capo_securityhub.types.aws_code_build_project_source

        out["Source"] = (
            capo_securityhub.types.aws_code_build_project_source.serialize_json(
                value["source"]
            )
        )
    if "service_role" in value:
        out["ServiceRole"] = value["service_role"]
    if "logs_config" in value:
        import capo_securityhub.types.aws_code_build_project_logs_config_details

        out["LogsConfig"] = (
            capo_securityhub.types.aws_code_build_project_logs_config_details.serialize_json(
                value["logs_config"]
            )
        )
    if "vpc_config" in value:
        import capo_securityhub.types.aws_code_build_project_vpc_config

        out["VpcConfig"] = (
            capo_securityhub.types.aws_code_build_project_vpc_config.serialize_json(
                value["vpc_config"]
            )
        )
    if "secondary_artifacts" in value:
        import capo_securityhub.types.aws_code_build_project_artifacts_list

        out["SecondaryArtifacts"] = (
            capo_securityhub.types.aws_code_build_project_artifacts_list.serialize_json(
                value["secondary_artifacts"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsCodeBuildProjectDetails:
    out: AwsCodeBuildProjectDetails = {}  # type: ignore[typeddict-item]
    if "EncryptionKey" in data:
        out["encryption_key"] = data["EncryptionKey"]
    if "Artifacts" in data:
        import capo_securityhub.types.aws_code_build_project_artifacts_list

        out["artifacts"] = (
            capo_securityhub.types.aws_code_build_project_artifacts_list.deserialize_json(
                data["Artifacts"]
            )
        )
    if "Environment" in data:
        import capo_securityhub.types.aws_code_build_project_environment

        out["environment"] = (
            capo_securityhub.types.aws_code_build_project_environment.deserialize_json(
                data["Environment"]
            )
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "Source" in data:
        import capo_securityhub.types.aws_code_build_project_source

        out["source"] = (
            capo_securityhub.types.aws_code_build_project_source.deserialize_json(
                data["Source"]
            )
        )
    if "ServiceRole" in data:
        out["service_role"] = data["ServiceRole"]
    if "LogsConfig" in data:
        import capo_securityhub.types.aws_code_build_project_logs_config_details

        out["logs_config"] = (
            capo_securityhub.types.aws_code_build_project_logs_config_details.deserialize_json(
                data["LogsConfig"]
            )
        )
    if "VpcConfig" in data:
        import capo_securityhub.types.aws_code_build_project_vpc_config

        out["vpc_config"] = (
            capo_securityhub.types.aws_code_build_project_vpc_config.deserialize_json(
                data["VpcConfig"]
            )
        )
    if "SecondaryArtifacts" in data:
        import capo_securityhub.types.aws_code_build_project_artifacts_list

        out["secondary_artifacts"] = (
            capo_securityhub.types.aws_code_build_project_artifacts_list.deserialize_json(
                data["SecondaryArtifacts"]
            )
        )
    return out
