"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#WorkloadIdentityDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.workload_identity_arn


class WorkloadIdentityDetails(TypedDict, closed=True):
    workload_identity_arn: "aws_sdk_bedrock_agentcore_control.types.workload_identity_arn.WorkloadIdentityArn"
    """<p>The ARN associated with the workload identity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkloadIdentityDetails) -> dict:
    out: dict = {}
    out["workloadIdentityArn"] = value["workload_identity_arn"]
    return out


def deserialize_json(data: dict) -> WorkloadIdentityDetails:
    out: WorkloadIdentityDetails = {}  # type: ignore[typeddict-item]
    if "workloadIdentityArn" in data:
        out["workload_identity_arn"] = data["workloadIdentityArn"]
    else:
        raise DeserializationError(
            "WorkloadIdentityDetails.workload_identity_arn required"
        )
    return out
