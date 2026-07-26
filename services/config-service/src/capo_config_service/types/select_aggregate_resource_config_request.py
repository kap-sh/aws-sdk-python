"""Generated from Smithy shape ``com.amazonaws.configservice#SelectAggregateResourceConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_config_service.types.configuration_aggregator_name
    import capo_config_service.types.expression
    import capo_config_service.types.limit
    import capo_config_service.types.next_token


class SelectAggregateResourceConfigRequest(TypedDict, closed=True):
    expression: "capo_config_service.types.expression.Expression"
    """<p>The SQL query SELECT command. </p>"""
    configuration_aggregator_name: "capo_config_service.types.configuration_aggregator_name.ConfigurationAggregatorName"
    """<p>The name of the configuration aggregator.</p>"""
    limit: "capo_config_service.types.limit.Limit"
    """<p>The maximum number of query results returned on each page. </p>"""
    max_results: "capo_config_service.types.limit.Limit"
    """<p>The maximum number of query results returned on each page. Config also allows the Limit request parameter.</p>"""
    next_token: NotRequired["capo_config_service.types.next_token.NextToken"]
    """<p>The nextToken string returned in a previous request that you use to request the next page of results in a paginated response. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SelectAggregateResourceConfigRequest) -> dict:
    out: dict = {}
    out["Expression"] = value["expression"]
    out["ConfigurationAggregatorName"] = value["configuration_aggregator_name"]
    out["Limit"] = value.get("limit", 0)
    out["MaxResults"] = value.get("max_results", 0)
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SelectAggregateResourceConfigRequest:
    out: SelectAggregateResourceConfigRequest = {}  # type: ignore[typeddict-item]
    if "Expression" in data:
        out["expression"] = data["Expression"]
    else:
        raise DeserializationError(
            "SelectAggregateResourceConfigRequest.expression required"
        )
    if "ConfigurationAggregatorName" in data:
        out["configuration_aggregator_name"] = data["ConfigurationAggregatorName"]
    else:
        raise DeserializationError(
            "SelectAggregateResourceConfigRequest.configuration_aggregator_name required"
        )
    if "Limit" in data:
        out["limit"] = data["Limit"]
    else:
        out["limit"] = 0
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    else:
        out["max_results"] = 0
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
