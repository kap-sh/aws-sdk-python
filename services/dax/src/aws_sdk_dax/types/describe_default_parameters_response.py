"""Generated from Smithy shape ``com.amazonaws.dax#DescribeDefaultParametersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dax.types.parameter_list
    import aws_sdk_dax.types.string


class DescribeDefaultParametersResponse(TypedDict):
    next_token: NotRequired["aws_sdk_dax.types.string.String"]
    """<p>Provides an identifier to allow retrieval of paginated results.</p>"""
    parameters: NotRequired["aws_sdk_dax.types.parameter_list.ParameterList"]
    """<p>A list of parameters. Each element in the list represents one parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDefaultParametersResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "parameters" in value:
        import aws_sdk_dax.types.parameter_list

        out["Parameters"] = aws_sdk_dax.types.parameter_list.serialize_aws_json_1_1(
            value["parameters"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDefaultParametersResponse:
    out: DescribeDefaultParametersResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Parameters" in data:
        import aws_sdk_dax.types.parameter_list

        out["parameters"] = aws_sdk_dax.types.parameter_list.deserialize_aws_json_1_1(
            data["Parameters"]
        )
    return out
