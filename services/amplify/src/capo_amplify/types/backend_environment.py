"""Generated from Smithy shape ``com.amazonaws.amplify#BackendEnvironment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_amplify.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amplify.types.backend_environment_arn
    import capo_amplify.types.create_time
    import capo_amplify.types.deployment_artifacts
    import capo_amplify.types.environment_name
    import capo_amplify.types.stack_name
    import capo_amplify.types.update_time


class BackendEnvironment(TypedDict, closed=True):
    backend_environment_arn: (
        "capo_amplify.types.backend_environment_arn.BackendEnvironmentArn"
    )
    """<p>The Amazon Resource Name (ARN) for a backend environment that is part of an Amplify app. </p>"""
    environment_name: "capo_amplify.types.environment_name.EnvironmentName"
    """<p>The name for a backend environment that is part of an Amplify app. </p>"""
    stack_name: NotRequired["capo_amplify.types.stack_name.StackName"]
    """<p>The AWS CloudFormation stack name of a backend environment. </p>"""
    deployment_artifacts: NotRequired[
        "capo_amplify.types.deployment_artifacts.DeploymentArtifacts"
    ]
    """<p>The name of deployment artifacts. </p>"""
    create_time: "capo_amplify.types.create_time.CreateTime"
    """<p>The creation date and time for a backend environment that is part of an Amplify app. </p>"""
    update_time: "capo_amplify.types.update_time.UpdateTime"
    """<p>The last updated date and time for a backend environment that is part of an Amplify app. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BackendEnvironment) -> dict:
    out: dict = {}
    out["backendEnvironmentArn"] = value["backend_environment_arn"]
    out["environmentName"] = value["environment_name"]
    if "stack_name" in value:
        out["stackName"] = value["stack_name"]
    if "deployment_artifacts" in value:
        out["deploymentArtifacts"] = value["deployment_artifacts"]
    import capo_amplify.types.create_time

    out["createTime"] = capo_amplify.types.create_time.serialize_json(
        value["create_time"]
    )
    import capo_amplify.types.update_time

    out["updateTime"] = capo_amplify.types.update_time.serialize_json(
        value["update_time"]
    )
    return out


def deserialize_json(data: dict) -> BackendEnvironment:
    out: BackendEnvironment = {}  # type: ignore[typeddict-item]
    if "backendEnvironmentArn" in data:
        out["backend_environment_arn"] = data["backendEnvironmentArn"]
    else:
        raise DeserializationError(
            "BackendEnvironment.backend_environment_arn required"
        )
    if "environmentName" in data:
        out["environment_name"] = data["environmentName"]
    else:
        raise DeserializationError("BackendEnvironment.environment_name required")
    if "stackName" in data:
        out["stack_name"] = data["stackName"]
    if "deploymentArtifacts" in data:
        out["deployment_artifacts"] = data["deploymentArtifacts"]
    if "createTime" in data:
        import capo_amplify.types.create_time

        out["create_time"] = capo_amplify.types.create_time.deserialize_json(
            data["createTime"]
        )
    else:
        raise DeserializationError("BackendEnvironment.create_time required")
    if "updateTime" in data:
        import capo_amplify.types.update_time

        out["update_time"] = capo_amplify.types.update_time.deserialize_json(
            data["updateTime"]
        )
    else:
        raise DeserializationError("BackendEnvironment.update_time required")
    return out
