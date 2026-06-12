"""Generated from Smithy shape ``com.amazonaws.servicediscovery#NamespaceFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_servicediscovery.types.namespace_filter

NamespaceFilters: TypeAlias = list[
    "aws_sdk_servicediscovery.types.namespace_filter.NamespaceFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NamespaceFilters) -> list:
    import aws_sdk_servicediscovery.types.namespace_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_servicediscovery.types.namespace_filter.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> NamespaceFilters:
    import aws_sdk_servicediscovery.types.namespace_filter

    out: NamespaceFilters = []
    for item in data:
        out.append(
            aws_sdk_servicediscovery.types.namespace_filter.deserialize_aws_json_1_1(
                item
            )
        )
    return out
