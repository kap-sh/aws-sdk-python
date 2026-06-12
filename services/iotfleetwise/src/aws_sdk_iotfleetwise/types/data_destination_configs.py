"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#DataDestinationConfigs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.data_destination_config

DataDestinationConfigs: TypeAlias = list[
    "aws_sdk_iotfleetwise.types.data_destination_config.DataDestinationConfig"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DataDestinationConfigs) -> list:
    import aws_sdk_iotfleetwise.types.data_destination_config

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iotfleetwise.types.data_destination_config.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> DataDestinationConfigs:
    import aws_sdk_iotfleetwise.types.data_destination_config

    out: DataDestinationConfigs = []
    for item in data:
        out.append(
            aws_sdk_iotfleetwise.types.data_destination_config.deserialize_aws_json_1_0(
                item
            )
        )
    return out
