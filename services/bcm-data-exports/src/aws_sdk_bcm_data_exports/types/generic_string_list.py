"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#GenericStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bcm_data_exports.types.generic_string

GenericStringList: TypeAlias = list[
    "aws_sdk_bcm_data_exports.types.generic_string.GenericString"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GenericStringList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> GenericStringList:
    return list(data)
