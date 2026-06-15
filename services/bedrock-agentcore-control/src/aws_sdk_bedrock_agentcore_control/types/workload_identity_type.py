"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#WorkloadIdentityType``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.workload_identity_arn_type
    import aws_sdk_bedrock_agentcore_control.types.workload_identity_name_type


class WorkloadIdentityType(TypedDict):
    name: "aws_sdk_bedrock_agentcore_control.types.workload_identity_name_type.WorkloadIdentityNameType"
    """<p>The name of the workload identity.</p>"""
    workload_identity_arn: "aws_sdk_bedrock_agentcore_control.types.workload_identity_arn_type.WorkloadIdentityArnType"
    """<p>The Amazon Resource Name (ARN) of the workload identity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkloadIdentityType) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["workloadIdentityArn"] = value["workload_identity_arn"]
    return out


def deserialize_json(data: dict) -> WorkloadIdentityType:
    out: WorkloadIdentityType = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("WorkloadIdentityType.name required")
    if "workloadIdentityArn" in data:
        out["workload_identity_arn"] = data["workloadIdentityArn"]
    else:
        raise DeserializationError(
            "WorkloadIdentityType.workload_identity_arn required"
        )
    return out
