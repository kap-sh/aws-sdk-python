"""Generated from Smithy shape ``com.amazonaws.firehose#DestinationDescriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_firehose.types.destination_description

DestinationDescriptionList: TypeAlias = list[
    "aws_sdk_firehose.types.destination_description.DestinationDescription"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DestinationDescriptionList) -> list:
    import aws_sdk_firehose.types.destination_description

    out: list = []
    for item in value:
        out.append(
            aws_sdk_firehose.types.destination_description.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DestinationDescriptionList:
    import aws_sdk_firehose.types.destination_description

    out: DestinationDescriptionList = []
    for item in data:
        out.append(
            aws_sdk_firehose.types.destination_description.deserialize_aws_json_1_1(
                item
            )
        )
    return out
