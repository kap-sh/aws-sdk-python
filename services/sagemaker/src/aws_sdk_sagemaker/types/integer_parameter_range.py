"""Generated from Smithy shape ``com.amazonaws.sagemaker#IntegerParameterRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.hyper_parameter_scaling_type
    import aws_sdk_sagemaker.types.parameter_key
    import aws_sdk_sagemaker.types.parameter_value


class IntegerParameterRange(TypedDict, closed=True):
    name: NotRequired["aws_sdk_sagemaker.types.parameter_key.ParameterKey"]
    """<p>The name of the hyperparameter to search.</p>"""
    min_value: NotRequired["aws_sdk_sagemaker.types.parameter_value.ParameterValue"]
    """<p>The minimum value of the hyperparameter to search.</p>"""
    max_value: NotRequired["aws_sdk_sagemaker.types.parameter_value.ParameterValue"]
    """<p>The maximum value of the hyperparameter to search.</p>"""
    scaling_type: NotRequired[
        "aws_sdk_sagemaker.types.hyper_parameter_scaling_type.HyperParameterScalingType"
    ]
    r"""<p>The scale that hyperparameter tuning uses to search the hyperparameter range. For information about choosing a hyperparameter scale, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-ranges.html#scaling-type\">Hyperparameter Scaling</a>. One of the following values:</p> <dl> <dt>Auto</dt> <dd> <p>SageMaker hyperparameter tuning chooses the best scale for the hyperparameter.</p> </dd> <dt>Linear</dt> <dd> <p>Hyperparameter tuning searches the values in the hyperparameter range by using a linear scale.</p> </dd> <dt>Logarithmic</dt> <dd> <p>Hyperparameter tuning searches the values in the hyperparameter range by using a logarithmic scale.</p> <p>Logarithmic scaling works only for ranges that have only values greater than 0.</p> </dd> </dl>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IntegerParameterRange) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "min_value" in value:
        out["MinValue"] = value["min_value"]
    if "max_value" in value:
        out["MaxValue"] = value["max_value"]
    if "scaling_type" in value:
        import aws_sdk_sagemaker.types.hyper_parameter_scaling_type

        out["ScalingType"] = (
            aws_sdk_sagemaker.types.hyper_parameter_scaling_type.serialize_aws_json_1_1(
                value["scaling_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> IntegerParameterRange:
    out: IntegerParameterRange = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "MinValue" in data:
        out["min_value"] = data["MinValue"]
    if "MaxValue" in data:
        out["max_value"] = data["MaxValue"]
    if "ScalingType" in data:
        import aws_sdk_sagemaker.types.hyper_parameter_scaling_type

        out["scaling_type"] = (
            aws_sdk_sagemaker.types.hyper_parameter_scaling_type.deserialize_aws_json_1_1(
                data["ScalingType"]
            )
        )
    return out
