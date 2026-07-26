"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#FilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_discovery_service.types.filter_value

FilterValues: TypeAlias = list[
    "capo_application_discovery_service.types.filter_value.FilterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilterValues) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> FilterValues:
    return list(data)
