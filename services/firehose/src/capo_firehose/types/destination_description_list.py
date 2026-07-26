"""Generated from Smithy shape ``com.amazonaws.firehose#DestinationDescriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_firehose.types.destination_description

DestinationDescriptionList: TypeAlias = list[
    "capo_firehose.types.destination_description.DestinationDescription"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DestinationDescriptionList) -> list:
    import capo_firehose.types.destination_description

    out: list = []
    for item in value:
        out.append(
            capo_firehose.types.destination_description.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DestinationDescriptionList:
    import capo_firehose.types.destination_description

    out: DestinationDescriptionList = []
    for item in data:
        out.append(
            capo_firehose.types.destination_description.deserialize_aws_json_1_1(item)
        )
    return out
