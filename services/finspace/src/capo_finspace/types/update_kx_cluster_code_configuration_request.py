"""Generated from Smithy shape ``com.amazonaws.finspace#UpdateKxClusterCodeConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_finspace.errors import DeserializationError

if TYPE_CHECKING:
    import capo_finspace.types.client_token_string
    import capo_finspace.types.code_configuration
    import capo_finspace.types.initialization_script_file_path
    import capo_finspace.types.kx_cluster_code_deployment_configuration
    import capo_finspace.types.kx_cluster_name
    import capo_finspace.types.kx_command_line_arguments
    import capo_finspace.types.kx_environment_id


class UpdateKxClusterCodeConfigurationRequest(TypedDict, closed=True):
    environment_id: "capo_finspace.types.kx_environment_id.KxEnvironmentId"
    """<p> A unique identifier of the kdb environment. </p>"""
    cluster_name: "capo_finspace.types.kx_cluster_name.KxClusterName"
    """<p>The name of the cluster.</p>"""
    client_token: NotRequired[
        "capo_finspace.types.client_token_string.ClientTokenString"
    ]
    """<p>A token that ensures idempotency. This token expires in 10 minutes.</p>"""
    code: "capo_finspace.types.code_configuration.CodeConfiguration"
    initialization_script: NotRequired[
        "capo_finspace.types.initialization_script_file_path.InitializationScriptFilePath"
    ]
    """<p>Specifies a Q program that will be run at launch of a cluster. It is a relative path within <i>.zip</i> file that contains the custom code, which will be loaded on the cluster. It must include the file name itself. For example, <code>somedir/init.q</code>.</p> <p>You cannot update this parameter for a <code>NO_RESTART</code> deployment.</p>"""
    command_line_arguments: NotRequired[
        "capo_finspace.types.kx_command_line_arguments.KxCommandLineArguments"
    ]
    """<p>Specifies the key-value pairs to make them available inside the cluster.</p> <p>You cannot update this parameter for a <code>NO_RESTART</code> deployment.</p>"""
    deployment_configuration: NotRequired[
        "capo_finspace.types.kx_cluster_code_deployment_configuration.KxClusterCodeDeploymentConfiguration"
    ]
    """<p> The configuration that allows you to choose how you want to update the code on a cluster. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateKxClusterCodeConfigurationRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    import capo_finspace.types.code_configuration

    out["code"] = capo_finspace.types.code_configuration.serialize_json(value["code"])
    if "initialization_script" in value:
        out["initializationScript"] = value["initialization_script"]
    if "command_line_arguments" in value:
        import capo_finspace.types.kx_command_line_arguments

        out["commandLineArguments"] = (
            capo_finspace.types.kx_command_line_arguments.serialize_json(
                value["command_line_arguments"]
            )
        )
    if "deployment_configuration" in value:
        import capo_finspace.types.kx_cluster_code_deployment_configuration

        out["deploymentConfiguration"] = (
            capo_finspace.types.kx_cluster_code_deployment_configuration.serialize_json(
                value["deployment_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateKxClusterCodeConfigurationRequest:
    out: UpdateKxClusterCodeConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "code" in data:
        import capo_finspace.types.code_configuration

        out["code"] = capo_finspace.types.code_configuration.deserialize_json(
            data["code"]
        )
    else:
        raise DeserializationError(
            "UpdateKxClusterCodeConfigurationRequest.code required"
        )
    if "initializationScript" in data:
        out["initialization_script"] = data["initializationScript"]
    if "commandLineArguments" in data:
        import capo_finspace.types.kx_command_line_arguments

        out["command_line_arguments"] = (
            capo_finspace.types.kx_command_line_arguments.deserialize_json(
                data["commandLineArguments"]
            )
        )
    if "deploymentConfiguration" in data:
        import capo_finspace.types.kx_cluster_code_deployment_configuration

        out["deployment_configuration"] = (
            capo_finspace.types.kx_cluster_code_deployment_configuration.deserialize_json(
                data["deploymentConfiguration"]
            )
        )
    return out
