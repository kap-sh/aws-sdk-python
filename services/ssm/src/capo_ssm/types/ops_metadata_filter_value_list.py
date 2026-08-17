"""Generated from Smithy shape ``com.amazonaws.ssm#OpsMetadataFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.ops_metadata_filter_value

OpsMetadataFilterValueList: TypeAlias = list[
    "capo_ssm.types.ops_metadata_filter_value.OpsMetadataFilterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsMetadataFilterValueList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> OpsMetadataFilterValueList:
    return [item for item in data if item is not None]
