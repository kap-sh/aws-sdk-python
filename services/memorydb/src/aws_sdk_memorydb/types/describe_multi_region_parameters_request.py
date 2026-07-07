"""Generated from Smithy shape ``com.amazonaws.memorydb#DescribeMultiRegionParametersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_memorydb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.integer_optional
    import aws_sdk_memorydb.types.string


class DescribeMultiRegionParametersRequest(TypedDict, closed=True):
    multi_region_parameter_group_name: "aws_sdk_memorydb.types.string.String"
    """<p>The name of the multi-region parameter group to return details for.</p>"""
    source: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The parameter types to return. Valid values: user | system | engine-default</p>"""
    max_results: NotRequired["aws_sdk_memorydb.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of records to include in the response. If more records exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.</p>"""
    next_token: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMultiRegionParametersRequest) -> dict:
    out: dict = {}
    out["MultiRegionParameterGroupName"] = value["multi_region_parameter_group_name"]
    if "source" in value:
        out["Source"] = value["source"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMultiRegionParametersRequest:
    out: DescribeMultiRegionParametersRequest = {}  # type: ignore[typeddict-item]
    if "MultiRegionParameterGroupName" in data:
        out["multi_region_parameter_group_name"] = data["MultiRegionParameterGroupName"]
    else:
        raise DeserializationError(
            "DescribeMultiRegionParametersRequest.multi_region_parameter_group_name required"
        )
    if "Source" in data:
        out["source"] = data["Source"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
