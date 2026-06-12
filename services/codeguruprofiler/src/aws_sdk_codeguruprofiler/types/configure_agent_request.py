"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#ConfigureAgentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codeguruprofiler.types.fleet_instance_id
    import aws_sdk_codeguruprofiler.types.metadata
    import aws_sdk_codeguruprofiler.types.profiling_group_name


class ConfigureAgentRequest(TypedDict):
    profiling_group_name: (
        "aws_sdk_codeguruprofiler.types.profiling_group_name.ProfilingGroupName"
    )
    """<p> The name of the profiling group for which the configured agent is collecting profiling data. </p>"""
    fleet_instance_id: NotRequired[
        "aws_sdk_codeguruprofiler.types.fleet_instance_id.FleetInstanceId"
    ]
    """<p> A universally unique identifier (UUID) for a profiling instance. For example, if the profiling instance is an Amazon EC2 instance, it is the instance ID. If it is an AWS Fargate container, it is the container's task ID. </p>"""
    metadata: NotRequired["aws_sdk_codeguruprofiler.types.metadata.Metadata"]
    """<p> Metadata captured about the compute platform the agent is running on. It includes information about sampling and reporting. The valid fields are:</p> <ul> <li> <p> <code>COMPUTE_PLATFORM</code> - The compute platform on which the agent is running </p> </li> <li> <p> <code>AGENT_ID</code> - The ID for an agent instance. </p> </li> <li> <p> <code>AWS_REQUEST_ID</code> - The AWS request ID of a Lambda invocation. </p> </li> <li> <p> <code>EXECUTION_ENVIRONMENT</code> - The execution environment a Lambda function is running on. </p> </li> <li> <p> <code>LAMBDA_FUNCTION_ARN</code> - The Amazon Resource Name (ARN) that is used to invoke a Lambda function. </p> </li> <li> <p> <code>LAMBDA_MEMORY_LIMIT_IN_MB</code> - The memory allocated to a Lambda function. </p> </li> <li> <p> <code>LAMBDA_REMAINING_TIME_IN_MILLISECONDS</code> - The time in milliseconds before execution of a Lambda function times out. </p> </li> <li> <p> <code>LAMBDA_TIME_GAP_BETWEEN_INVOKES_IN_MILLISECONDS</code> - The time in milliseconds between two invocations of a Lambda function. </p> </li> <li> <p> <code>LAMBDA_PREVIOUS_EXECUTION_TIME_IN_MILLISECONDS</code> - The time in milliseconds for the previous Lambda invocation. </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigureAgentRequest) -> dict:
    out: dict = {}
    if "fleet_instance_id" in value:
        out["fleetInstanceId"] = value["fleet_instance_id"]
    if "metadata" in value:
        import aws_sdk_codeguruprofiler.types.metadata

        out["metadata"] = aws_sdk_codeguruprofiler.types.metadata.serialize_json(
            value["metadata"]
        )
    return out


def deserialize_json(data: dict) -> ConfigureAgentRequest:
    out: ConfigureAgentRequest = {}  # type: ignore[typeddict-item]
    if "fleetInstanceId" in data:
        out["fleet_instance_id"] = data["fleetInstanceId"]
    if "metadata" in data:
        import aws_sdk_codeguruprofiler.types.metadata

        out["metadata"] = aws_sdk_codeguruprofiler.types.metadata.deserialize_json(
            data["metadata"]
        )
    return out
