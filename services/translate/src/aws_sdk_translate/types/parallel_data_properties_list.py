"""Generated from Smithy shape ``com.amazonaws.translate#ParallelDataPropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_translate.types.parallel_data_properties

ParallelDataPropertiesList: TypeAlias = list[
    "aws_sdk_translate.types.parallel_data_properties.ParallelDataProperties"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParallelDataPropertiesList) -> list:
    import aws_sdk_translate.types.parallel_data_properties

    out: list = []
    for item in value:
        out.append(
            aws_sdk_translate.types.parallel_data_properties.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ParallelDataPropertiesList:
    import aws_sdk_translate.types.parallel_data_properties

    out: ParallelDataPropertiesList = []
    for item in data:
        out.append(
            aws_sdk_translate.types.parallel_data_properties.deserialize_aws_json_1_1(
                item
            )
        )
    return out
