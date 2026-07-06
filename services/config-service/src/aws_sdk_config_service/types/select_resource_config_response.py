"""Generated from Smithy shape ``com.amazonaws.configservice#SelectResourceConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_config_service.types.next_token
    import aws_sdk_config_service.types.query_info
    import aws_sdk_config_service.types.results


class SelectResourceConfigResponse(TypedDict, closed=True):
    results: NotRequired["aws_sdk_config_service.types.results.Results"]
    """<p>Returns the results for the SQL query.</p>"""
    query_info: NotRequired["aws_sdk_config_service.types.query_info.QueryInfo"]
    """<p>Returns the <code>QueryInfo</code> object.</p>"""
    next_token: NotRequired["aws_sdk_config_service.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> string returned in a previous request that you use to request the next page of results in a paginated response. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SelectResourceConfigResponse) -> dict:
    out: dict = {}
    if "results" in value:
        import aws_sdk_config_service.types.results

        out["Results"] = aws_sdk_config_service.types.results.serialize_aws_json_1_1(
            value["results"]
        )
    if "query_info" in value:
        import aws_sdk_config_service.types.query_info

        out["QueryInfo"] = (
            aws_sdk_config_service.types.query_info.serialize_aws_json_1_1(
                value["query_info"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SelectResourceConfigResponse:
    out: SelectResourceConfigResponse = {}  # type: ignore[typeddict-item]
    if "Results" in data:
        import aws_sdk_config_service.types.results

        out["results"] = aws_sdk_config_service.types.results.deserialize_aws_json_1_1(
            data["Results"]
        )
    if "QueryInfo" in data:
        import aws_sdk_config_service.types.query_info

        out["query_info"] = (
            aws_sdk_config_service.types.query_info.deserialize_aws_json_1_1(
                data["QueryInfo"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
