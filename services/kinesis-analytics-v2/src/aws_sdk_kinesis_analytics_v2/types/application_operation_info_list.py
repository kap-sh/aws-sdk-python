"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ApplicationOperationInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.application_operation_info

ApplicationOperationInfoList: TypeAlias = list[
    "aws_sdk_kinesis_analytics_v2.types.application_operation_info.ApplicationOperationInfo"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationOperationInfoList) -> list:
    import aws_sdk_kinesis_analytics_v2.types.application_operation_info

    out: list = []
    for item in value:
        out.append(
            aws_sdk_kinesis_analytics_v2.types.application_operation_info.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ApplicationOperationInfoList:
    import aws_sdk_kinesis_analytics_v2.types.application_operation_info

    out: ApplicationOperationInfoList = []
    for item in data:
        out.append(
            aws_sdk_kinesis_analytics_v2.types.application_operation_info.deserialize_aws_json_1_1(
                item
            )
        )
    return out
