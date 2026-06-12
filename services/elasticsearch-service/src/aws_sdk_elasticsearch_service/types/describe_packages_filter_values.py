"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DescribePackagesFilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.describe_packages_filter_value

DescribePackagesFilterValues: TypeAlias = list[
    "aws_sdk_elasticsearch_service.types.describe_packages_filter_value.DescribePackagesFilterValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: DescribePackagesFilterValues) -> list:
    return list(value)


def deserialize_json(data: list) -> DescribePackagesFilterValues:
    return list(data)
