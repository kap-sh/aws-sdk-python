"""Generated from Smithy shape ``com.amazonaws.sagemaker#AgentVersions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.agent_version

AgentVersions: TypeAlias = list["capo_sagemaker.types.agent_version.AgentVersion"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AgentVersions) -> list:
    import capo_sagemaker.types.agent_version

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.agent_version.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AgentVersions:
    import capo_sagemaker.types.agent_version

    out: AgentVersions = []
    for item in data:
        out.append(capo_sagemaker.types.agent_version.deserialize_aws_json_1_1(item))
    return out
