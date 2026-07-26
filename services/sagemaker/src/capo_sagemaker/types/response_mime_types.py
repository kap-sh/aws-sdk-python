"""Generated from Smithy shape ``com.amazonaws.sagemaker#ResponseMIMETypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.response_mime_type

ResponseMIMETypes: TypeAlias = list[
    "capo_sagemaker.types.response_mime_type.ResponseMIMEType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResponseMIMETypes) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ResponseMIMETypes:
    return list(data)
