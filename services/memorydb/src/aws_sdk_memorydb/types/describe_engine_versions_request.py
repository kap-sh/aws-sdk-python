"""Generated from Smithy shape ``com.amazonaws.memorydb#DescribeEngineVersionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.boolean
    import aws_sdk_memorydb.types.integer_optional
    import aws_sdk_memorydb.types.string


class DescribeEngineVersionsRequest(TypedDict):
    engine: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The name of the engine for which to list available versions.</p>"""
    engine_version: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The Redis OSS engine version</p>"""
    parameter_group_family: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The name of a specific parameter group family to return details for.</p>"""
    max_results: NotRequired["aws_sdk_memorydb.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of records to include in the response. If more records exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.</p>"""
    next_token: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>"""
    default_only: "aws_sdk_memorydb.types.boolean.Boolean"
    """<p>If true, specifies that only the default version of the specified engine or engine and major version combination is to be returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEngineVersionsRequest) -> dict:
    out: dict = {}
    if "engine" in value:
        out["Engine"] = value["engine"]
    if "engine_version" in value:
        out["EngineVersion"] = value["engine_version"]
    if "parameter_group_family" in value:
        out["ParameterGroupFamily"] = value["parameter_group_family"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    out["DefaultOnly"] = value.get("default_only", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEngineVersionsRequest:
    out: DescribeEngineVersionsRequest = {}  # type: ignore[typeddict-item]
    if "Engine" in data:
        out["engine"] = data["Engine"]
    if "EngineVersion" in data:
        out["engine_version"] = data["EngineVersion"]
    if "ParameterGroupFamily" in data:
        out["parameter_group_family"] = data["ParameterGroupFamily"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "DefaultOnly" in data:
        out["default_only"] = data["DefaultOnly"]
    else:
        out["default_only"] = False
    return out
