"""Generated from Smithy shape ``com.amazonaws.ssm#GetParametersResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.parameter_list
    import aws_sdk_ssm.types.parameter_name_list


class GetParametersResult(TypedDict):
    parameters: NotRequired["aws_sdk_ssm.types.parameter_list.ParameterList"]
    """<p>A list of details for a parameter.</p>"""
    invalid_parameters: NotRequired[
        "aws_sdk_ssm.types.parameter_name_list.ParameterNameList"
    ]
    """<p>A list of parameters that aren't formatted correctly or don't run during an execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetParametersResult) -> dict:
    out: dict = {}
    if "parameters" in value:
        import aws_sdk_ssm.types.parameter_list

        out["Parameters"] = aws_sdk_ssm.types.parameter_list.serialize_aws_json_1_1(
            value["parameters"]
        )
    if "invalid_parameters" in value:
        import aws_sdk_ssm.types.parameter_name_list

        out["InvalidParameters"] = (
            aws_sdk_ssm.types.parameter_name_list.serialize_aws_json_1_1(
                value["invalid_parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetParametersResult:
    out: GetParametersResult = {}  # type: ignore[typeddict-item]
    if "Parameters" in data:
        import aws_sdk_ssm.types.parameter_list

        out["parameters"] = aws_sdk_ssm.types.parameter_list.deserialize_aws_json_1_1(
            data["Parameters"]
        )
    if "InvalidParameters" in data:
        import aws_sdk_ssm.types.parameter_name_list

        out["invalid_parameters"] = (
            aws_sdk_ssm.types.parameter_name_list.deserialize_aws_json_1_1(
                data["InvalidParameters"]
            )
        )
    return out
