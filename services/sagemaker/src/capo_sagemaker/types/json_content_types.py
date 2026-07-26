"""Generated from Smithy shape ``com.amazonaws.sagemaker#JsonContentTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.json_content_type

JsonContentTypes: TypeAlias = list[
    "capo_sagemaker.types.json_content_type.JsonContentType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JsonContentTypes) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> JsonContentTypes:
    return list(data)
