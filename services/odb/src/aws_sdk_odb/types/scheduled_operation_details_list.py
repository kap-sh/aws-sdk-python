"""Generated from Smithy shape ``com.amazonaws.odb#ScheduledOperationDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_odb.types.scheduled_operation_details

ScheduledOperationDetailsList: TypeAlias = list[
    "aws_sdk_odb.types.scheduled_operation_details.ScheduledOperationDetails"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ScheduledOperationDetailsList) -> list:
    import aws_sdk_odb.types.scheduled_operation_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_odb.types.scheduled_operation_details.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ScheduledOperationDetailsList:
    import aws_sdk_odb.types.scheduled_operation_details

    out: ScheduledOperationDetailsList = []
    for item in data:
        out.append(
            aws_sdk_odb.types.scheduled_operation_details.deserialize_aws_json_1_0(item)
        )
    return out
