"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#ImportTaskList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.import_task

ImportTaskList: TypeAlias = list[
    "aws_sdk_application_discovery_service.types.import_task.ImportTask"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportTaskList) -> list:
    import aws_sdk_application_discovery_service.types.import_task

    out: list = []
    for item in value:
        out.append(
            aws_sdk_application_discovery_service.types.import_task.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ImportTaskList:
    import aws_sdk_application_discovery_service.types.import_task

    out: ImportTaskList = []
    for item in data:
        out.append(
            aws_sdk_application_discovery_service.types.import_task.deserialize_aws_json_1_1(
                item
            )
        )
    return out
