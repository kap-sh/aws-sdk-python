"""Generated from Smithy shape ``com.amazonaws.ssm#DocumentKeyValuesFilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.document_key_values_filter_value

DocumentKeyValuesFilterValues: TypeAlias = list[
    "aws_sdk_ssm.types.document_key_values_filter_value.DocumentKeyValuesFilterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentKeyValuesFilterValues) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DocumentKeyValuesFilterValues:
    return list(data)
