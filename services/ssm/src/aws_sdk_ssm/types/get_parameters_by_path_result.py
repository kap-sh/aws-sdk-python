"""Generated from Smithy shape ``com.amazonaws.ssm#GetParametersByPathResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.next_token
    import aws_sdk_ssm.types.parameter_list


class GetParametersByPathResult(TypedDict):
    parameters: NotRequired["aws_sdk_ssm.types.parameter_list.ParameterList"]
    """<p>A list of parameters found in the specified hierarchy.</p>"""
    next_token: NotRequired["aws_sdk_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. Use this token to get the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetParametersByPathResult) -> dict:
    out: dict = {}
    if "parameters" in value:
        import aws_sdk_ssm.types.parameter_list

        out["Parameters"] = aws_sdk_ssm.types.parameter_list.serialize_aws_json_1_1(
            value["parameters"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetParametersByPathResult:
    out: GetParametersByPathResult = {}  # type: ignore[typeddict-item]
    if "Parameters" in data:
        import aws_sdk_ssm.types.parameter_list

        out["parameters"] = aws_sdk_ssm.types.parameter_list.deserialize_aws_json_1_1(
            data["Parameters"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
