"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#ProfilingGroupDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codeguruprofiler.types.agent_orchestration_config
    import aws_sdk_codeguruprofiler.types.compute_platform
    import aws_sdk_codeguruprofiler.types.profiling_group_arn
    import aws_sdk_codeguruprofiler.types.profiling_group_name
    import aws_sdk_codeguruprofiler.types.profiling_status
    import aws_sdk_codeguruprofiler.types.tags_map
    import aws_sdk_codeguruprofiler.types.timestamp


class ProfilingGroupDescription(TypedDict):
    name: NotRequired[
        "aws_sdk_codeguruprofiler.types.profiling_group_name.ProfilingGroupName"
    ]
    """<p>The name of the profiling group.</p>"""
    agent_orchestration_config: NotRequired[
        "aws_sdk_codeguruprofiler.types.agent_orchestration_config.AgentOrchestrationConfig"
    ]
    """<p> An <a href=\"https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_AgentOrchestrationConfig.html\"> <code>AgentOrchestrationConfig</code> </a> object that indicates if the profiling group is enabled for profiled or not. </p>"""
    arn: NotRequired[
        "aws_sdk_codeguruprofiler.types.profiling_group_arn.ProfilingGroupArn"
    ]
    """<p>The Amazon Resource Name (ARN) identifying the profiling group resource.</p>"""
    created_at: NotRequired["aws_sdk_codeguruprofiler.types.timestamp.Timestamp"]
    """<p>The time when the profiling group was created. Specify using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC. </p>"""
    updated_at: NotRequired["aws_sdk_codeguruprofiler.types.timestamp.Timestamp"]
    """<p> The date and time when the profiling group was last updated. Specify using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC. </p>"""
    profiling_status: NotRequired[
        "aws_sdk_codeguruprofiler.types.profiling_status.ProfilingStatus"
    ]
    """<p> A <a href=\"https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ProfilingStatus.html\"> <code>ProfilingStatus</code> </a> object that includes information about the last time a profile agent pinged back, the last time a profile was received, and the aggregation period and start time for the most recent aggregated profile. </p>"""
    compute_platform: NotRequired[
        "aws_sdk_codeguruprofiler.types.compute_platform.ComputePlatform"
    ]
    """<p> The compute platform of the profiling group. If it is set to <code>AWSLambda</code>, then the profiled application runs on AWS Lambda. If it is set to <code>Default</code>, then the profiled application runs on a compute platform that is not AWS Lambda, such an Amazon EC2 instance, an on-premises server, or a different platform. The default is <code>Default</code>. </p>"""
    tags: NotRequired["aws_sdk_codeguruprofiler.types.tags_map.TagsMap"]
    """<p> A list of the tags that belong to this profiling group. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProfilingGroupDescription) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "agent_orchestration_config" in value:
        import aws_sdk_codeguruprofiler.types.agent_orchestration_config

        out["agentOrchestrationConfig"] = (
            aws_sdk_codeguruprofiler.types.agent_orchestration_config.serialize_json(
                value["agent_orchestration_config"]
            )
        )
    if "arn" in value:
        out["arn"] = value["arn"]
    if "created_at" in value:
        import aws_sdk_codeguruprofiler.types.timestamp

        out["createdAt"] = aws_sdk_codeguruprofiler.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import aws_sdk_codeguruprofiler.types.timestamp

        out["updatedAt"] = aws_sdk_codeguruprofiler.types.timestamp.serialize_json(
            value["updated_at"]
        )
    if "profiling_status" in value:
        import aws_sdk_codeguruprofiler.types.profiling_status

        out["profilingStatus"] = (
            aws_sdk_codeguruprofiler.types.profiling_status.serialize_json(
                value["profiling_status"]
            )
        )
    if "compute_platform" in value:
        out["computePlatform"] = value["compute_platform"]
    if "tags" in value:
        import aws_sdk_codeguruprofiler.types.tags_map

        out["tags"] = aws_sdk_codeguruprofiler.types.tags_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> ProfilingGroupDescription:
    out: ProfilingGroupDescription = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "agentOrchestrationConfig" in data:
        import aws_sdk_codeguruprofiler.types.agent_orchestration_config

        out["agent_orchestration_config"] = (
            aws_sdk_codeguruprofiler.types.agent_orchestration_config.deserialize_json(
                data["agentOrchestrationConfig"]
            )
        )
    if "arn" in data:
        out["arn"] = data["arn"]
    if "createdAt" in data:
        import aws_sdk_codeguruprofiler.types.timestamp

        out["created_at"] = aws_sdk_codeguruprofiler.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "updatedAt" in data:
        import aws_sdk_codeguruprofiler.types.timestamp

        out["updated_at"] = aws_sdk_codeguruprofiler.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    if "profilingStatus" in data:
        import aws_sdk_codeguruprofiler.types.profiling_status

        out["profiling_status"] = (
            aws_sdk_codeguruprofiler.types.profiling_status.deserialize_json(
                data["profilingStatus"]
            )
        )
    if "computePlatform" in data:
        out["compute_platform"] = data["computePlatform"]
    if "tags" in data:
        import aws_sdk_codeguruprofiler.types.tags_map

        out["tags"] = aws_sdk_codeguruprofiler.types.tags_map.deserialize_json(
            data["tags"]
        )
    return out
