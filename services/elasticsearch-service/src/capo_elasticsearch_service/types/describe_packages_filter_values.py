"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DescribePackagesFilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.describe_packages_filter_value

DescribePackagesFilterValues: TypeAlias = list[
    "capo_elasticsearch_service.types.describe_packages_filter_value.DescribePackagesFilterValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: DescribePackagesFilterValues) -> list:
    return list(value)


def deserialize_json(data: list) -> DescribePackagesFilterValues:
    return list(data)
