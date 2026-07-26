"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#WorkloadIdentityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.workload_identity_type

WorkloadIdentityList: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.workload_identity_type.WorkloadIdentityType"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkloadIdentityList) -> list:
    import capo_bedrock_agentcore_control.types.workload_identity_type

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.workload_identity_type.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> WorkloadIdentityList:
    import capo_bedrock_agentcore_control.types.workload_identity_type

    out: WorkloadIdentityList = []
    for item in data:
        out.append(
            capo_bedrock_agentcore_control.types.workload_identity_type.deserialize_json(
                item
            )
        )
    return out
