"""Generated from Smithy shape ``com.amazonaws.inspector#AgentPreviewList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector.types.agent_preview

AgentPreviewList: TypeAlias = list["capo_inspector.types.agent_preview.AgentPreview"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AgentPreviewList) -> list:
    import capo_inspector.types.agent_preview

    out: list = []
    for item in value:
        out.append(capo_inspector.types.agent_preview.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AgentPreviewList:
    import capo_inspector.types.agent_preview

    out: AgentPreviewList = []
    for item in data:
        out.append(capo_inspector.types.agent_preview.deserialize_aws_json_1_1(item))
    return out
