"""Generated from Smithy shape ``com.amazonaws.ecs#ContainerDependency``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.container_condition
    import aws_sdk_ecs.types.string


class ContainerDependency(TypedDict):
    container_name: "aws_sdk_ecs.types.string.String"
    """<p>The name of a container.</p>"""
    condition: "aws_sdk_ecs.types.container_condition.ContainerCondition"
    """<p>The dependency condition of the container. The following are the available conditions and their behavior:</p> <ul> <li> <p> <code>START</code> - This condition emulates the behavior of links and volumes today. It validates that a dependent container is started before permitting other containers to start.</p> </li> <li> <p> <code>COMPLETE</code> - This condition validates that a dependent container runs to completion (exits) before permitting other containers to start. This can be useful for nonessential containers that run a script and then exit. This condition can't be set on an essential container.</p> </li> <li> <p> <code>SUCCESS</code> - This condition is the same as <code>COMPLETE</code>, but it also requires that the container exits with a <code>zero</code> status. This condition can't be set on an essential container.</p> </li> <li> <p> <code>HEALTHY</code> - This condition validates that the dependent container passes its Docker health check before permitting other containers to start. This requires that the dependent container has health checks configured. This condition is confirmed only at task startup.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerDependency) -> dict:
    out: dict = {}
    out["containerName"] = value["container_name"]
    import aws_sdk_ecs.types.container_condition

    out["condition"] = aws_sdk_ecs.types.container_condition.serialize_aws_json_1_1(
        value["condition"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ContainerDependency:
    out: ContainerDependency = {}  # type: ignore[typeddict-item]
    if "containerName" in data:
        out["container_name"] = data["containerName"]
    else:
        raise DeserializationError("ContainerDependency.container_name required")
    if "condition" in data:
        import aws_sdk_ecs.types.container_condition

        out["condition"] = (
            aws_sdk_ecs.types.container_condition.deserialize_aws_json_1_1(
                data["condition"]
            )
        )
    else:
        raise DeserializationError("ContainerDependency.condition required")
    return out
