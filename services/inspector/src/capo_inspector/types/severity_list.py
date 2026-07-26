"""Generated from Smithy shape ``com.amazonaws.inspector#SeverityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector.types.severity

SeverityList: TypeAlias = list["capo_inspector.types.severity.Severity"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SeverityList) -> list:
    import capo_inspector.types.severity

    out: list = []
    for item in value:
        out.append(capo_inspector.types.severity.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SeverityList:
    import capo_inspector.types.severity

    out: SeverityList = []
    for item in data:
        out.append(capo_inspector.types.severity.deserialize_aws_json_1_1(item))
    return out
