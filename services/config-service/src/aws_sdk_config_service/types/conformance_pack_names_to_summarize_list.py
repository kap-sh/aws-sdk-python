"""Generated from Smithy shape ``com.amazonaws.configservice#ConformancePackNamesToSummarizeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_config_service.types.conformance_pack_name

ConformancePackNamesToSummarizeList: TypeAlias = list[
    "aws_sdk_config_service.types.conformance_pack_name.ConformancePackName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConformancePackNamesToSummarizeList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ConformancePackNamesToSummarizeList:
    return list(data)
