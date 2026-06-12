"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ExcludeManagementEventSources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.string

ExcludeManagementEventSources: TypeAlias = list[
    "aws_sdk_cloudtrail.types.string.String"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExcludeManagementEventSources) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ExcludeManagementEventSources:
    return list(data)
