"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelDashboardEndpoints``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.model_dashboard_endpoint

ModelDashboardEndpoints: TypeAlias = list[
    "aws_sdk_sagemaker.types.model_dashboard_endpoint.ModelDashboardEndpoint"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelDashboardEndpoints) -> list:
    import aws_sdk_sagemaker.types.model_dashboard_endpoint

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.model_dashboard_endpoint.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ModelDashboardEndpoints:
    import aws_sdk_sagemaker.types.model_dashboard_endpoint

    out: ModelDashboardEndpoints = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.model_dashboard_endpoint.deserialize_aws_json_1_1(
                item
            )
        )
    return out
