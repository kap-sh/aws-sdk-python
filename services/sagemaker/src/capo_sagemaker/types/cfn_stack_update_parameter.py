"""Generated from Smithy shape ``com.amazonaws.sagemaker#CfnStackUpdateParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cfn_stack_parameter_key
    import capo_sagemaker.types.cfn_stack_parameter_value


class CfnStackUpdateParameter(TypedDict, closed=True):
    key: NotRequired[
        "capo_sagemaker.types.cfn_stack_parameter_key.CfnStackParameterKey"
    ]
    """<p> The name of the CloudFormation parameter. </p>"""
    value: NotRequired[
        "capo_sagemaker.types.cfn_stack_parameter_value.CfnStackParameterValue"
    ]
    """<p> The value of the CloudFormation parameter. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CfnStackUpdateParameter) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CfnStackUpdateParameter:
    out: CfnStackUpdateParameter = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
