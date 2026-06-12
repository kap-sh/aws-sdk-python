"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeParametersResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.next_token
    import aws_sdk_ssm.types.parameter_metadata_list


class DescribeParametersResult(TypedDict):
    parameters: NotRequired[
        "aws_sdk_ssm.types.parameter_metadata_list.ParameterMetadataList"
    ]
    """<p>Parameters returned by the request.</p>"""
    next_token: NotRequired["aws_sdk_ssm.types.next_token.NextToken"]
    """<p>The token to use when requesting the next set of items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeParametersResult) -> dict:
    out: dict = {}
    if "parameters" in value:
        import aws_sdk_ssm.types.parameter_metadata_list

        out["Parameters"] = (
            aws_sdk_ssm.types.parameter_metadata_list.serialize_aws_json_1_1(
                value["parameters"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeParametersResult:
    out: DescribeParametersResult = {}  # type: ignore[typeddict-item]
    if "Parameters" in data:
        import aws_sdk_ssm.types.parameter_metadata_list

        out["parameters"] = (
            aws_sdk_ssm.types.parameter_metadata_list.deserialize_aws_json_1_1(
                data["Parameters"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
