"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityResultDescriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.data_quality_result_description

DataQualityResultDescriptionList: TypeAlias = list[
    "aws_sdk_glue.types.data_quality_result_description.DataQualityResultDescription"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityResultDescriptionList) -> list:
    import aws_sdk_glue.types.data_quality_result_description

    out: list = []
    for item in value:
        out.append(
            aws_sdk_glue.types.data_quality_result_description.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DataQualityResultDescriptionList:
    import aws_sdk_glue.types.data_quality_result_description

    out: DataQualityResultDescriptionList = []
    for item in data:
        out.append(
            aws_sdk_glue.types.data_quality_result_description.deserialize_aws_json_1_1(
                item
            )
        )
    return out
