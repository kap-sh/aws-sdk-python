"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DescribePackagesFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.describe_packages_filter

DescribePackagesFilterList: TypeAlias = list[
    "capo_elasticsearch_service.types.describe_packages_filter.DescribePackagesFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: DescribePackagesFilterList) -> list:
    import capo_elasticsearch_service.types.describe_packages_filter

    out: list = []
    for item in value:
        out.append(
            capo_elasticsearch_service.types.describe_packages_filter.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DescribePackagesFilterList:
    import capo_elasticsearch_service.types.describe_packages_filter

    out: DescribePackagesFilterList = []
    for item in data:
        out.append(
            capo_elasticsearch_service.types.describe_packages_filter.deserialize_json(
                item
            )
        )
    return out
