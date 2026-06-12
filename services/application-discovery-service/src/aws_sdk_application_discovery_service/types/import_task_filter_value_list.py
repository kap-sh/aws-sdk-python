"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#ImportTaskFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.import_task_filter_value

ImportTaskFilterValueList: TypeAlias = list[
    "aws_sdk_application_discovery_service.types.import_task_filter_value.ImportTaskFilterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportTaskFilterValueList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ImportTaskFilterValueList:
    return list(data)
