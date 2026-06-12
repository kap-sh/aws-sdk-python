"""Generated from Smithy shape ``com.amazonaws.elasticache#DescribeServerlessCachesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.serverless_cache_list
    import aws_sdk_elasticache.types.string


class DescribeServerlessCachesResponse(TypedDict):
    next_token: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>An optional marker returned from a prior request to support pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxResults.</p>"""
    serverless_caches: NotRequired[
        "aws_sdk_elasticache.types.serverless_cache_list.ServerlessCacheList"
    ]
    """<p>The serverless caches associated with a given description request.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeServerlessCachesResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "serverless_caches" in value:
        import aws_sdk_elasticache.types.serverless_cache_list

        aws_sdk_elasticache.types.serverless_cache_list.serialize_query(
            value["serverless_caches"], pairs, f"{prefix}.ServerlessCaches"
        )


def deserialize_query(el: Element) -> DescribeServerlessCachesResponse:
    out: DescribeServerlessCachesResponse = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_serverless_caches = el.find("ServerlessCaches")
    if child_serverless_caches is not None:
        import aws_sdk_elasticache.types.serverless_cache_list

        out["serverless_caches"] = (
            aws_sdk_elasticache.types.serverless_cache_list.deserialize_query(
                child_serverless_caches
            )
        )
    return out
