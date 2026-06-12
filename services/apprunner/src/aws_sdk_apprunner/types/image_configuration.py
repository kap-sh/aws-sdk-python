"""Generated from Smithy shape ``com.amazonaws.apprunner#ImageConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.runtime_environment_secrets
    import aws_sdk_apprunner.types.runtime_environment_variables
    import aws_sdk_apprunner.types.start_command
    import aws_sdk_apprunner.types.string


class ImageConfiguration(TypedDict):
    runtime_environment_variables: NotRequired[
        "aws_sdk_apprunner.types.runtime_environment_variables.RuntimeEnvironmentVariables"
    ]
    """<p>Environment variables that are available to your running App Runner service. An array of key-value pairs.</p>"""
    start_command: NotRequired["aws_sdk_apprunner.types.start_command.StartCommand"]
    """<p>An optional command that App Runner runs to start the application in the source image. If specified, this command overrides the Docker image’s default start command.</p>"""
    port: NotRequired["aws_sdk_apprunner.types.string.String"]
    """<p>The port that your application listens to in the container.</p> <p>Default: <code>8080</code> </p>"""
    runtime_environment_secrets: NotRequired[
        "aws_sdk_apprunner.types.runtime_environment_secrets.RuntimeEnvironmentSecrets"
    ]
    """<p>An array of key-value pairs representing the secrets and parameters that get referenced to your service as an environment variable. The supported values are either the full Amazon Resource Name (ARN) of the Secrets Manager secret or the full ARN of the parameter in the Amazon Web Services Systems Manager Parameter Store.</p> <note> <ul> <li> <p> If the Amazon Web Services Systems Manager Parameter Store parameter exists in the same Amazon Web Services Region as the service that you're launching, you can use either the full ARN or name of the secret. If the parameter exists in a different Region, then the full ARN must be specified. </p> </li> <li> <p> Currently, cross account referencing of Amazon Web Services Systems Manager Parameter Store parameter is not supported. </p> </li> </ul> </note>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ImageConfiguration) -> dict:
    out: dict = {}
    if "runtime_environment_variables" in value:
        import aws_sdk_apprunner.types.runtime_environment_variables

        out["RuntimeEnvironmentVariables"] = (
            aws_sdk_apprunner.types.runtime_environment_variables.serialize_aws_json_1_0(
                value["runtime_environment_variables"]
            )
        )
    if "start_command" in value:
        out["StartCommand"] = value["start_command"]
    if "port" in value:
        out["Port"] = value["port"]
    if "runtime_environment_secrets" in value:
        import aws_sdk_apprunner.types.runtime_environment_secrets

        out["RuntimeEnvironmentSecrets"] = (
            aws_sdk_apprunner.types.runtime_environment_secrets.serialize_aws_json_1_0(
                value["runtime_environment_secrets"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ImageConfiguration:
    out: ImageConfiguration = {}  # type: ignore[typeddict-item]
    if "RuntimeEnvironmentVariables" in data:
        import aws_sdk_apprunner.types.runtime_environment_variables

        out["runtime_environment_variables"] = (
            aws_sdk_apprunner.types.runtime_environment_variables.deserialize_aws_json_1_0(
                data["RuntimeEnvironmentVariables"]
            )
        )
    if "StartCommand" in data:
        out["start_command"] = data["StartCommand"]
    if "Port" in data:
        out["port"] = data["Port"]
    if "RuntimeEnvironmentSecrets" in data:
        import aws_sdk_apprunner.types.runtime_environment_secrets

        out["runtime_environment_secrets"] = (
            aws_sdk_apprunner.types.runtime_environment_secrets.deserialize_aws_json_1_0(
                data["RuntimeEnvironmentSecrets"]
            )
        )
    return out
