"""Generated from Smithy shape ``com.amazonaws.sagemaker#MetricSpecification``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_sagemaker.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.customized_metric_specification
    import aws_sdk_sagemaker.types.predefined_metric_specification


class _MetricSpecification_Predefined(TypedDict):
    Predefined: "aws_sdk_sagemaker.types.predefined_metric_specification.PredefinedMetricSpecification"


class _MetricSpecification_Customized(TypedDict):
    Customized: "aws_sdk_sagemaker.types.customized_metric_specification.CustomizedMetricSpecification"


MetricSpecification: TypeAlias = (
    _MetricSpecification_Predefined | _MetricSpecification_Customized
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricSpecification) -> dict:
    if "Predefined" in value:
        import aws_sdk_sagemaker.types.predefined_metric_specification

        return {
            "Predefined": aws_sdk_sagemaker.types.predefined_metric_specification.serialize_aws_json_1_1(
                value["Predefined"]
            )
        }
    elif "Customized" in value:
        import aws_sdk_sagemaker.types.customized_metric_specification

        return {
            "Customized": aws_sdk_sagemaker.types.customized_metric_specification.serialize_aws_json_1_1(
                value["Customized"]
            )
        }
    else:
        raise SerializationError("MetricSpecification: no variant present")


def deserialize_aws_json_1_1(data: dict) -> MetricSpecification:
    if "Predefined" in data:
        import aws_sdk_sagemaker.types.predefined_metric_specification

        return {
            "Predefined": aws_sdk_sagemaker.types.predefined_metric_specification.deserialize_aws_json_1_1(
                data["Predefined"]
            )
        }
    elif "Customized" in data:
        import aws_sdk_sagemaker.types.customized_metric_specification

        return {
            "Customized": aws_sdk_sagemaker.types.customized_metric_specification.deserialize_aws_json_1_1(
                data["Customized"]
            )
        }
    else:
        raise DeserializationError("MetricSpecification: no recognized variant key")
