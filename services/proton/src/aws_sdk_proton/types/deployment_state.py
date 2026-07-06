"""Generated from Smithy shape ``com.amazonaws.proton#DeploymentState``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_proton.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.component_state
    import aws_sdk_proton.types.environment_state
    import aws_sdk_proton.types.service_instance_state
    import aws_sdk_proton.types.service_pipeline_state


class _DeploymentState_serviceInstance(TypedDict, closed=True):
    serviceInstance: "aws_sdk_proton.types.service_instance_state.ServiceInstanceState"


class _DeploymentState_environment(TypedDict, closed=True):
    environment: "aws_sdk_proton.types.environment_state.EnvironmentState"


class _DeploymentState_servicePipeline(TypedDict, closed=True):
    servicePipeline: "aws_sdk_proton.types.service_pipeline_state.ServicePipelineState"


class _DeploymentState_component(TypedDict, closed=True):
    component: "aws_sdk_proton.types.component_state.ComponentState"


DeploymentState: TypeAlias = (
    _DeploymentState_serviceInstance
    | _DeploymentState_environment
    | _DeploymentState_servicePipeline
    | _DeploymentState_component
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeploymentState) -> dict:
    if "serviceInstance" in value:
        import aws_sdk_proton.types.service_instance_state

        return {
            "serviceInstance": aws_sdk_proton.types.service_instance_state.serialize_aws_json_1_0(
                value["serviceInstance"]
            )
        }
    elif "environment" in value:
        import aws_sdk_proton.types.environment_state

        return {
            "environment": aws_sdk_proton.types.environment_state.serialize_aws_json_1_0(
                value["environment"]
            )
        }
    elif "servicePipeline" in value:
        import aws_sdk_proton.types.service_pipeline_state

        return {
            "servicePipeline": aws_sdk_proton.types.service_pipeline_state.serialize_aws_json_1_0(
                value["servicePipeline"]
            )
        }
    elif "component" in value:
        import aws_sdk_proton.types.component_state

        return {
            "component": aws_sdk_proton.types.component_state.serialize_aws_json_1_0(
                value["component"]
            )
        }
    else:
        raise SerializationError("DeploymentState: no variant present")


def deserialize_aws_json_1_0(data: dict) -> DeploymentState:
    if "serviceInstance" in data:
        import aws_sdk_proton.types.service_instance_state

        return {
            "serviceInstance": aws_sdk_proton.types.service_instance_state.deserialize_aws_json_1_0(
                data["serviceInstance"]
            )
        }
    elif "environment" in data:
        import aws_sdk_proton.types.environment_state

        return {
            "environment": aws_sdk_proton.types.environment_state.deserialize_aws_json_1_0(
                data["environment"]
            )
        }
    elif "servicePipeline" in data:
        import aws_sdk_proton.types.service_pipeline_state

        return {
            "servicePipeline": aws_sdk_proton.types.service_pipeline_state.deserialize_aws_json_1_0(
                data["servicePipeline"]
            )
        }
    elif "component" in data:
        import aws_sdk_proton.types.component_state

        return {
            "component": aws_sdk_proton.types.component_state.deserialize_aws_json_1_0(
                data["component"]
            )
        }
    else:
        raise DeserializationError("DeploymentState: no recognized variant key")
