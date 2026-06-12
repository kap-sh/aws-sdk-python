"""Generated from Smithy shape ``com.amazonaws.firehose#DestinationTableConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_firehose.types.destination_table_configuration

DestinationTableConfigurationList: TypeAlias = list[
    "aws_sdk_firehose.types.destination_table_configuration.DestinationTableConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DestinationTableConfigurationList) -> list:
    import aws_sdk_firehose.types.destination_table_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_firehose.types.destination_table_configuration.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DestinationTableConfigurationList:
    import aws_sdk_firehose.types.destination_table_configuration

    out: DestinationTableConfigurationList = []
    for item in data:
        out.append(
            aws_sdk_firehose.types.destination_table_configuration.deserialize_aws_json_1_1(
                item
            )
        )
    return out
