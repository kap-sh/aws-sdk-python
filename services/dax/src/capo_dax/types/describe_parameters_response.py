"""Generated from Smithy shape ``com.amazonaws.dax#DescribeParametersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dax.types.parameter_list
    import capo_dax.types.string


class DescribeParametersResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_dax.types.string.String"]
    """<p>Provides an identifier to allow retrieval of paginated results.</p>"""
    parameters: NotRequired["capo_dax.types.parameter_list.ParameterList"]
    """<p>A list of parameters within a parameter group. Each element in the list represents one parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeParametersResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "parameters" in value:
        import capo_dax.types.parameter_list

        out["Parameters"] = capo_dax.types.parameter_list.serialize_aws_json_1_1(
            value["parameters"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeParametersResponse:
    out: DescribeParametersResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Parameters" in data:
        import capo_dax.types.parameter_list

        out["parameters"] = capo_dax.types.parameter_list.deserialize_aws_json_1_1(
            data["Parameters"]
        )
    return out
