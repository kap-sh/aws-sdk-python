"""Generated from Smithy shape ``com.amazonaws.sagemaker#Endpoints``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.endpoint_info

Endpoints: TypeAlias = list["capo_sagemaker.types.endpoint_info.EndpointInfo"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Endpoints) -> list:
    import capo_sagemaker.types.endpoint_info

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.endpoint_info.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Endpoints:
    import capo_sagemaker.types.endpoint_info

    out: Endpoints = []
    for item in data:
        out.append(capo_sagemaker.types.endpoint_info.deserialize_aws_json_1_1(item))
    return out
