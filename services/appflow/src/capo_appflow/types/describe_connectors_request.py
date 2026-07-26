"""Generated from Smithy shape ``com.amazonaws.appflow#DescribeConnectorsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.connector_type_list
    import capo_appflow.types.max_results
    import capo_appflow.types.next_token


class DescribeConnectorsRequest(TypedDict, closed=True):
    connector_types: NotRequired[
        "capo_appflow.types.connector_type_list.ConnectorTypeList"
    ]
    """<p> The type of connector, such as Salesforce, Amplitude, and so on. </p>"""
    max_results: NotRequired["capo_appflow.types.max_results.MaxResults"]
    """<p>The maximum number of items that should be returned in the result set. The default is 20.</p>"""
    next_token: NotRequired["capo_appflow.types.next_token.NextToken"]
    """<p> The pagination token for the next page of data. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeConnectorsRequest) -> dict:
    out: dict = {}
    if "connector_types" in value:
        import capo_appflow.types.connector_type_list

        out["connectorTypes"] = capo_appflow.types.connector_type_list.serialize_json(
            value["connector_types"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeConnectorsRequest:
    out: DescribeConnectorsRequest = {}  # type: ignore[typeddict-item]
    if "connectorTypes" in data:
        import capo_appflow.types.connector_type_list

        out["connector_types"] = (
            capo_appflow.types.connector_type_list.deserialize_json(
                data["connectorTypes"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
