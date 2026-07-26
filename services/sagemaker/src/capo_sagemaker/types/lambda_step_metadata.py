"""Generated from Smithy shape ``com.amazonaws.sagemaker#LambdaStepMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.output_parameter_list
    import capo_sagemaker.types.string256


class LambdaStepMetadata(TypedDict, closed=True):
    arn: NotRequired["capo_sagemaker.types.string256.String256"]
    """<p>The Amazon Resource Name (ARN) of the Lambda function that was run by this step execution.</p>"""
    output_parameters: NotRequired[
        "capo_sagemaker.types.output_parameter_list.OutputParameterList"
    ]
    """<p>A list of the output parameters of the Lambda step.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LambdaStepMetadata) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "output_parameters" in value:
        import capo_sagemaker.types.output_parameter_list

        out["OutputParameters"] = (
            capo_sagemaker.types.output_parameter_list.serialize_aws_json_1_1(
                value["output_parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LambdaStepMetadata:
    out: LambdaStepMetadata = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "OutputParameters" in data:
        import capo_sagemaker.types.output_parameter_list

        out["output_parameters"] = (
            capo_sagemaker.types.output_parameter_list.deserialize_aws_json_1_1(
                data["OutputParameters"]
            )
        )
    return out
