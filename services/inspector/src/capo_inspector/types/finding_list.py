"""Generated from Smithy shape ``com.amazonaws.inspector#FindingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector.types.finding

FindingList: TypeAlias = list["capo_inspector.types.finding.Finding"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FindingList) -> list:
    import capo_inspector.types.finding

    out: list = []
    for item in value:
        out.append(capo_inspector.types.finding.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> FindingList:
    import capo_inspector.types.finding

    out: FindingList = []
    for item in data:
        out.append(capo_inspector.types.finding.deserialize_aws_json_1_1(item))
    return out
