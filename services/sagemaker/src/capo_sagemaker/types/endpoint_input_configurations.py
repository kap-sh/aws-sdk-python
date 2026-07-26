"""Generated from Smithy shape ``com.amazonaws.sagemaker#EndpointInputConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.endpoint_input_configuration

EndpointInputConfigurations: TypeAlias = list[
    "capo_sagemaker.types.endpoint_input_configuration.EndpointInputConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndpointInputConfigurations) -> list:
    import capo_sagemaker.types.endpoint_input_configuration

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.endpoint_input_configuration.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EndpointInputConfigurations:
    import capo_sagemaker.types.endpoint_input_configuration

    out: EndpointInputConfigurations = []
    for item in data:
        out.append(
            capo_sagemaker.types.endpoint_input_configuration.deserialize_aws_json_1_1(
                item
            )
        )
    return out
