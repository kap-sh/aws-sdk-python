"""Generated from Smithy shape ``com.amazonaws.applicationinsights#WorkloadMetaData``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_insights.types.meta_data_key
    import aws_sdk_application_insights.types.meta_data_value

WorkloadMetaData: TypeAlias = dict[
    "aws_sdk_application_insights.types.meta_data_key.MetaDataKey",
    "aws_sdk_application_insights.types.meta_data_value.MetaDataValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: WorkloadMetaData) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> WorkloadMetaData:
    out: WorkloadMetaData = {}
    for key, value in data.items():
        out[key] = value
    return out
