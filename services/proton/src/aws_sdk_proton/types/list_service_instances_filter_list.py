"""Generated from Smithy shape ``com.amazonaws.proton#ListServiceInstancesFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_proton.types.list_service_instances_filter

ListServiceInstancesFilterList: TypeAlias = list[
    "aws_sdk_proton.types.list_service_instances_filter.ListServiceInstancesFilter"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListServiceInstancesFilterList) -> list:
    import aws_sdk_proton.types.list_service_instances_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_proton.types.list_service_instances_filter.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ListServiceInstancesFilterList:
    import aws_sdk_proton.types.list_service_instances_filter

    out: ListServiceInstancesFilterList = []
    for item in data:
        out.append(
            aws_sdk_proton.types.list_service_instances_filter.deserialize_aws_json_1_0(
                item
            )
        )
    return out
