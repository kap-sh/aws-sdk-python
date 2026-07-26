"""Generated from Smithy shape ``com.amazonaws.sagemaker#CsvContentTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.csv_content_type

CsvContentTypes: TypeAlias = list[
    "capo_sagemaker.types.csv_content_type.CsvContentType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CsvContentTypes) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> CsvContentTypes:
    return list(data)
