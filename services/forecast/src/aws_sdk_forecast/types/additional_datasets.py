"""Generated from Smithy shape ``com.amazonaws.forecast#AdditionalDatasets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_forecast.types.additional_dataset

AdditionalDatasets: TypeAlias = list[
    "aws_sdk_forecast.types.additional_dataset.AdditionalDataset"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdditionalDatasets) -> list:
    import aws_sdk_forecast.types.additional_dataset

    out: list = []
    for item in value:
        out.append(
            aws_sdk_forecast.types.additional_dataset.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AdditionalDatasets:
    import aws_sdk_forecast.types.additional_dataset

    out: AdditionalDatasets = []
    for item in data:
        out.append(
            aws_sdk_forecast.types.additional_dataset.deserialize_aws_json_1_1(item)
        )
    return out
