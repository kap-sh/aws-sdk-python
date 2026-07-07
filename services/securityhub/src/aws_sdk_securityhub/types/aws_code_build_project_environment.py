"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCodeBuildProjectEnvironment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_code_build_project_environment_environment_variables_list
    import aws_sdk_securityhub.types.aws_code_build_project_environment_registry_credential
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.non_empty_string


class AwsCodeBuildProjectEnvironment(TypedDict, closed=True):
    certificate: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The certificate to use with this build project.</p>"""
    environment_variables: NotRequired[
        "aws_sdk_securityhub.types.aws_code_build_project_environment_environment_variables_list.AwsCodeBuildProjectEnvironmentEnvironmentVariablesList"
    ]
    """<p>A set of environment variables to make available to builds for the build project.</p>"""
    privileged_mode: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Whether to allow the Docker daemon to run inside a Docker container. Set to <code>true</code> if the build project is used to build Docker images.</p>"""
    image_pull_credentials_type: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The type of credentials CodeBuild uses to pull images in your build.</p> <p>Valid values:</p> <ul> <li> <p> <code>CODEBUILD</code> specifies that CodeBuild uses its own credentials. This requires that you modify your ECR repository policy to trust the CodeBuild service principal.</p> </li> <li> <p> <code>SERVICE_ROLE</code> specifies that CodeBuild uses your build project's service role.</p> </li> </ul> <p>When you use a cross-account or private registry image, you must use <code>SERVICE_ROLE</code> credentials. When you use an CodeBuild curated image, you must use <code>CODEBUILD</code> credentials.</p>"""
    registry_credential: NotRequired[
        "aws_sdk_securityhub.types.aws_code_build_project_environment_registry_credential.AwsCodeBuildProjectEnvironmentRegistryCredential"
    ]
    """<p>The credentials for access to a private registry.</p>"""
    type: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The type of build environment to use for related builds.</p> <p>The environment type <code>ARM_CONTAINER</code> is available only in Regions US East (N. Virginia), US East (Ohio), US West (Oregon), Europe (Ireland), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Sydney), and Europe (Frankfurt).</p> <p>The environment type <code>LINUX_CONTAINER</code> with compute type build.general1.2xlarge is available only in Regions US East (N. Virginia), US East (N. Virginia), US West (Oregon), Canada (Central), Europe (Ireland), Europe (London), Europe (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), China (Beijing), and China (Ningxia).</p> <p>The environment type <code>LINUX_GPU_CONTAINER</code> is available only in Regions US East (N. Virginia), US East (N. Virginia), US West (Oregon), Canada (Central), Europe (Ireland), Europe (London), Europe (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), China (Beijing), and China (Ningxia).</p> <p>Valid values: <code>WINDOWS_CONTAINER</code> | <code>LINUX_CONTAINER</code> | <code>LINUX_GPU_CONTAINER</code> | <code>ARM_CONTAINER</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsCodeBuildProjectEnvironment) -> dict:
    out: dict = {}
    if "certificate" in value:
        out["Certificate"] = value["certificate"]
    if "environment_variables" in value:
        import aws_sdk_securityhub.types.aws_code_build_project_environment_environment_variables_list

        out["EnvironmentVariables"] = (
            aws_sdk_securityhub.types.aws_code_build_project_environment_environment_variables_list.serialize_json(
                value["environment_variables"]
            )
        )
    if "privileged_mode" in value:
        out["PrivilegedMode"] = value["privileged_mode"]
    if "image_pull_credentials_type" in value:
        out["ImagePullCredentialsType"] = value["image_pull_credentials_type"]
    if "registry_credential" in value:
        import aws_sdk_securityhub.types.aws_code_build_project_environment_registry_credential

        out["RegistryCredential"] = (
            aws_sdk_securityhub.types.aws_code_build_project_environment_registry_credential.serialize_json(
                value["registry_credential"]
            )
        )
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_json(data: dict) -> AwsCodeBuildProjectEnvironment:
    out: AwsCodeBuildProjectEnvironment = {}  # type: ignore[typeddict-item]
    if "Certificate" in data:
        out["certificate"] = data["Certificate"]
    if "EnvironmentVariables" in data:
        import aws_sdk_securityhub.types.aws_code_build_project_environment_environment_variables_list

        out["environment_variables"] = (
            aws_sdk_securityhub.types.aws_code_build_project_environment_environment_variables_list.deserialize_json(
                data["EnvironmentVariables"]
            )
        )
    if "PrivilegedMode" in data:
        out["privileged_mode"] = data["PrivilegedMode"]
    if "ImagePullCredentialsType" in data:
        out["image_pull_credentials_type"] = data["ImagePullCredentialsType"]
    if "RegistryCredential" in data:
        import aws_sdk_securityhub.types.aws_code_build_project_environment_registry_credential

        out["registry_credential"] = (
            aws_sdk_securityhub.types.aws_code_build_project_environment_registry_credential.deserialize_json(
                data["RegistryCredential"]
            )
        )
    if "Type" in data:
        out["type"] = data["Type"]
    return out
