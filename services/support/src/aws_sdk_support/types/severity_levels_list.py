"""Generated from Smithy shape ``com.amazonaws.support#SeverityLevelsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_support.types.severity_level

SeverityLevelsList: TypeAlias = list[
    "aws_sdk_support.types.severity_level.SeverityLevel"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SeverityLevelsList) -> list:
    import aws_sdk_support.types.severity_level

    out: list = []
    for item in value:
        out.append(aws_sdk_support.types.severity_level.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SeverityLevelsList:
    import aws_sdk_support.types.severity_level

    out: SeverityLevelsList = []
    for item in data:
        out.append(aws_sdk_support.types.severity_level.deserialize_aws_json_1_1(item))
    return out
