"""Generated from Smithy shape ``com.amazonaws.configservice#ConformancePackNamesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.conformance_pack_name

ConformancePackNamesList: TypeAlias = list[
    "capo_config_service.types.conformance_pack_name.ConformancePackName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConformancePackNamesList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ConformancePackNamesList:
    return list(data)
