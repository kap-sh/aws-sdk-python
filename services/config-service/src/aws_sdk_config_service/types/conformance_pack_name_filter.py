"""Generated from Smithy shape ``com.amazonaws.configservice#ConformancePackNameFilter``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_config_service.types.conformance_pack_name

ConformancePackNameFilter: TypeAlias = list[
    "aws_sdk_config_service.types.conformance_pack_name.ConformancePackName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConformancePackNameFilter) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ConformancePackNameFilter:
    return list(data)
