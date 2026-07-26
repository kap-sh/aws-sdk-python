"""Generated from Smithy shape ``com.amazonaws.swf#DecisionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_swf.types.decision

DecisionList: TypeAlias = list["capo_swf.types.decision.Decision"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DecisionList) -> list:
    import capo_swf.types.decision

    out: list = []
    for item in value:
        out.append(capo_swf.types.decision.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> DecisionList:
    import capo_swf.types.decision

    out: DecisionList = []
    for item in data:
        out.append(capo_swf.types.decision.deserialize_aws_json_1_0(item))
    return out
