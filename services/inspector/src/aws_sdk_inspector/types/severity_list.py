"""Generated from Smithy shape ``com.amazonaws.inspector#SeverityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector.types.severity

SeverityList: TypeAlias = list["aws_sdk_inspector.types.severity.Severity"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SeverityList) -> list:
    import aws_sdk_inspector.types.severity

    out: list = []
    for item in value:
        out.append(aws_sdk_inspector.types.severity.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SeverityList:
    import aws_sdk_inspector.types.severity

    out: SeverityList = []
    for item in data:
        out.append(aws_sdk_inspector.types.severity.deserialize_aws_json_1_1(item))
    return out
