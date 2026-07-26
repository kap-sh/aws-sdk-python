"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#DescribeImportTasksFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_discovery_service.types.import_task_filter

DescribeImportTasksFilterList: TypeAlias = list[
    "capo_application_discovery_service.types.import_task_filter.ImportTaskFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeImportTasksFilterList) -> list:
    import capo_application_discovery_service.types.import_task_filter

    out: list = []
    for item in value:
        out.append(
            capo_application_discovery_service.types.import_task_filter.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DescribeImportTasksFilterList:
    import capo_application_discovery_service.types.import_task_filter

    out: DescribeImportTasksFilterList = []
    for item in data:
        out.append(
            capo_application_discovery_service.types.import_task_filter.deserialize_aws_json_1_1(
                item
            )
        )
    return out
