"""Generated from Smithy shape ``com.amazonaws.sagemaker#EndpointPerformances``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.endpoint_performance

EndpointPerformances: TypeAlias = list[
    "aws_sdk_sagemaker.types.endpoint_performance.EndpointPerformance"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndpointPerformances) -> list:
    import aws_sdk_sagemaker.types.endpoint_performance

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.endpoint_performance.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EndpointPerformances:
    import aws_sdk_sagemaker.types.endpoint_performance

    out: EndpointPerformances = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.endpoint_performance.deserialize_aws_json_1_1(item)
        )
    return out
