"""Generated from Smithy shape ``com.amazonaws.apprunner#CodeConfigurationValues``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.build_command
    import aws_sdk_apprunner.types.runtime
    import aws_sdk_apprunner.types.runtime_environment_secrets
    import aws_sdk_apprunner.types.runtime_environment_variables
    import aws_sdk_apprunner.types.start_command
    import aws_sdk_apprunner.types.string


class CodeConfigurationValues(TypedDict):
    runtime: "aws_sdk_apprunner.types.runtime.Runtime"
    """<p>A runtime environment type for building and running an App Runner service. It represents a programming language runtime.</p>"""
    build_command: NotRequired["aws_sdk_apprunner.types.build_command.BuildCommand"]
    """<p>The command App Runner runs to build your application.</p>"""
    start_command: NotRequired["aws_sdk_apprunner.types.start_command.StartCommand"]
    """<p>The command App Runner runs to start your application.</p>"""
    port: NotRequired["aws_sdk_apprunner.types.string.String"]
    """<p>The port that your application listens to in the container.</p> <p>Default: <code>8080</code> </p>"""
    runtime_environment_variables: NotRequired[
        "aws_sdk_apprunner.types.runtime_environment_variables.RuntimeEnvironmentVariables"
    ]
    """<p>The environment variables that are available to your running App Runner service. An array of key-value pairs.</p>"""
    runtime_environment_secrets: NotRequired[
        "aws_sdk_apprunner.types.runtime_environment_secrets.RuntimeEnvironmentSecrets"
    ]
    """<p>An array of key-value pairs representing the secrets and parameters that get referenced to your service as an environment variable. The supported values are either the full Amazon Resource Name (ARN) of the Secrets Manager secret or the full ARN of the parameter in the Amazon Web Services Systems Manager Parameter Store.</p> <note> <ul> <li> <p> If the Amazon Web Services Systems Manager Parameter Store parameter exists in the same Amazon Web Services Region as the service that you're launching, you can use either the full ARN or name of the secret. If the parameter exists in a different Region, then the full ARN must be specified. </p> </li> <li> <p> Currently, cross account referencing of Amazon Web Services Systems Manager Parameter Store parameter is not supported. </p> </li> </ul> </note>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CodeConfigurationValues) -> dict:
    out: dict = {}
    import aws_sdk_apprunner.types.runtime

    out["Runtime"] = aws_sdk_apprunner.types.runtime.serialize_aws_json_1_0(
        value["runtime"]
    )
    if "build_command" in value:
        out["BuildCommand"] = value["build_command"]
    if "start_command" in value:
        out["StartCommand"] = value["start_command"]
    if "port" in value:
        out["Port"] = value["port"]
    if "runtime_environment_variables" in value:
        import aws_sdk_apprunner.types.runtime_environment_variables

        out["RuntimeEnvironmentVariables"] = (
            aws_sdk_apprunner.types.runtime_environment_variables.serialize_aws_json_1_0(
                value["runtime_environment_variables"]
            )
        )
    if "runtime_environment_secrets" in value:
        import aws_sdk_apprunner.types.runtime_environment_secrets

        out["RuntimeEnvironmentSecrets"] = (
            aws_sdk_apprunner.types.runtime_environment_secrets.serialize_aws_json_1_0(
                value["runtime_environment_secrets"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CodeConfigurationValues:
    out: CodeConfigurationValues = {}  # type: ignore[typeddict-item]
    if "Runtime" in data:
        import aws_sdk_apprunner.types.runtime

        out["runtime"] = aws_sdk_apprunner.types.runtime.deserialize_aws_json_1_0(
            data["Runtime"]
        )
    else:
        raise DeserializationError("CodeConfigurationValues.runtime required")
    if "BuildCommand" in data:
        out["build_command"] = data["BuildCommand"]
    if "StartCommand" in data:
        out["start_command"] = data["StartCommand"]
    if "Port" in data:
        out["port"] = data["Port"]
    if "RuntimeEnvironmentVariables" in data:
        import aws_sdk_apprunner.types.runtime_environment_variables

        out["runtime_environment_variables"] = (
            aws_sdk_apprunner.types.runtime_environment_variables.deserialize_aws_json_1_0(
                data["RuntimeEnvironmentVariables"]
            )
        )
    if "RuntimeEnvironmentSecrets" in data:
        import aws_sdk_apprunner.types.runtime_environment_secrets

        out["runtime_environment_secrets"] = (
            aws_sdk_apprunner.types.runtime_environment_secrets.deserialize_aws_json_1_0(
                data["RuntimeEnvironmentSecrets"]
            )
        )
    return out
