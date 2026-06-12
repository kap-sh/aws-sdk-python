"""Generated from Smithy shape ``com.amazonaws.finspace#UpdateKxClusterCodeConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_finspace.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_finspace.types.client_token_string
    import aws_sdk_finspace.types.code_configuration
    import aws_sdk_finspace.types.initialization_script_file_path
    import aws_sdk_finspace.types.kx_cluster_code_deployment_configuration
    import aws_sdk_finspace.types.kx_cluster_name
    import aws_sdk_finspace.types.kx_command_line_arguments
    import aws_sdk_finspace.types.kx_environment_id


class UpdateKxClusterCodeConfigurationRequest(TypedDict):
    environment_id: "aws_sdk_finspace.types.kx_environment_id.KxEnvironmentId"
    """<p> A unique identifier of the kdb environment. </p>"""
    cluster_name: "aws_sdk_finspace.types.kx_cluster_name.KxClusterName"
    """<p>The name of the cluster.</p>"""
    client_token: NotRequired[
        "aws_sdk_finspace.types.client_token_string.ClientTokenString"
    ]
    """<p>A token that ensures idempotency. This token expires in 10 minutes.</p>"""
    code: "aws_sdk_finspace.types.code_configuration.CodeConfiguration"
    initialization_script: NotRequired[
        "aws_sdk_finspace.types.initialization_script_file_path.InitializationScriptFilePath"
    ]
    """<p>Specifies a Q program that will be run at launch of a cluster. It is a relative path within <i>.zip</i> file that contains the custom code, which will be loaded on the cluster. It must include the file name itself. For example, <code>somedir/init.q</code>.</p> <p>You cannot update this parameter for a <code>NO_RESTART</code> deployment.</p>"""
    command_line_arguments: NotRequired[
        "aws_sdk_finspace.types.kx_command_line_arguments.KxCommandLineArguments"
    ]
    """<p>Specifies the key-value pairs to make them available inside the cluster.</p> <p>You cannot update this parameter for a <code>NO_RESTART</code> deployment.</p>"""
    deployment_configuration: NotRequired[
        "aws_sdk_finspace.types.kx_cluster_code_deployment_configuration.KxClusterCodeDeploymentConfiguration"
    ]
    """<p> The configuration that allows you to choose how you want to update the code on a cluster. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateKxClusterCodeConfigurationRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    import aws_sdk_finspace.types.code_configuration

    out["code"] = aws_sdk_finspace.types.code_configuration.serialize_json(
        value["code"]
    )
    if "initialization_script" in value:
        out["initializationScript"] = value["initialization_script"]
    if "command_line_arguments" in value:
        import aws_sdk_finspace.types.kx_command_line_arguments

        out["commandLineArguments"] = (
            aws_sdk_finspace.types.kx_command_line_arguments.serialize_json(
                value["command_line_arguments"]
            )
        )
    if "deployment_configuration" in value:
        import aws_sdk_finspace.types.kx_cluster_code_deployment_configuration

        out["deploymentConfiguration"] = (
            aws_sdk_finspace.types.kx_cluster_code_deployment_configuration.serialize_json(
                value["deployment_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateKxClusterCodeConfigurationRequest:
    out: UpdateKxClusterCodeConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "code" in data:
        import aws_sdk_finspace.types.code_configuration

        out["code"] = aws_sdk_finspace.types.code_configuration.deserialize_json(
            data["code"]
        )
    else:
        raise DeserializationError(
            "UpdateKxClusterCodeConfigurationRequest.code required"
        )
    if "initializationScript" in data:
        out["initialization_script"] = data["initializationScript"]
    if "commandLineArguments" in data:
        import aws_sdk_finspace.types.kx_command_line_arguments

        out["command_line_arguments"] = (
            aws_sdk_finspace.types.kx_command_line_arguments.deserialize_json(
                data["commandLineArguments"]
            )
        )
    if "deploymentConfiguration" in data:
        import aws_sdk_finspace.types.kx_cluster_code_deployment_configuration

        out["deployment_configuration"] = (
            aws_sdk_finspace.types.kx_cluster_code_deployment_configuration.deserialize_json(
                data["deploymentConfiguration"]
            )
        )
    return out
