"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeParametersResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.next_token
    import capo_ssm.types.parameter_metadata_list


class DescribeParametersResult(TypedDict, closed=True):
    parameters: NotRequired[
        "capo_ssm.types.parameter_metadata_list.ParameterMetadataList"
    ]
    """<p>Parameters returned by the request.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token to use when requesting the next set of items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeParametersResult) -> dict:
    out: dict = {}
    if "parameters" in value:
        import capo_ssm.types.parameter_metadata_list

        out["Parameters"] = (
            capo_ssm.types.parameter_metadata_list.serialize_aws_json_1_1(
                value["parameters"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeParametersResult:
    out: DescribeParametersResult = {}  # type: ignore[typeddict-item]
    if data.get("Parameters") is not None:
        import capo_ssm.types.parameter_metadata_list

        out["parameters"] = (
            capo_ssm.types.parameter_metadata_list.deserialize_aws_json_1_1(
                data["Parameters"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
