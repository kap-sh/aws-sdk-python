"""Generated from Smithy shape ``com.amazonaws.elasticache#DescribeServerlessCachesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.integer_optional
    import aws_sdk_elasticache.types.string


class DescribeServerlessCachesRequest(TypedDict, closed=True):
    serverless_cache_name: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The identifier for the serverless cache. If this parameter is specified, only information about that specific serverless cache is returned. Default: NULL</p>"""
    max_results: NotRequired[
        "aws_sdk_elasticache.types.integer_optional.IntegerOptional"
    ]
    """<p>The maximum number of records in the response. If more records exist than the specified max-records value, the next token is included in the response so that remaining results can be retrieved. The default is 50.</p>"""
    next_token: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>An optional marker returned from a prior request to support pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxResults.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeServerlessCachesRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "serverless_cache_name" in value:
        pairs.append(
            (f"{prefix}.ServerlessCacheName", str(value["serverless_cache_name"]))
        )
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> DescribeServerlessCachesRequest:
    out: DescribeServerlessCachesRequest = {}  # type: ignore[typeddict-item]
    child_serverless_cache_name = el.find("ServerlessCacheName")
    if child_serverless_cache_name is not None:
        out["serverless_cache_name"] = str(child_serverless_cache_name.text or "")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
