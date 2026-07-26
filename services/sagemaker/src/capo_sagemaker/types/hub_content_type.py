"""Generated from Smithy shape ``com.amazonaws.sagemaker#HubContentType``."""

from typing import Literal, TypeAlias, cast

HubContentType: TypeAlias = Literal[
    "Model",
    "Notebook",
    "ModelReference",
    "DataSet",
    "JsonDoc",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HubContentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HubContentType:
    return cast(HubContentType, data)
