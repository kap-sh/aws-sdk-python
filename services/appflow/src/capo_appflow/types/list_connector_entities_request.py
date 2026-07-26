"""Generated from Smithy shape ``com.amazonaws.appflow#ListConnectorEntitiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.api_version
    import capo_appflow.types.connector_profile_name
    import capo_appflow.types.connector_type
    import capo_appflow.types.entities_path
    import capo_appflow.types.list_entities_max_results
    import capo_appflow.types.next_token


class ListConnectorEntitiesRequest(TypedDict, closed=True):
    connector_profile_name: NotRequired[
        "capo_appflow.types.connector_profile_name.ConnectorProfileName"
    ]
    """<p> The name of the connector profile. The name is unique for each <code>ConnectorProfile</code> in the Amazon Web Services account, and is used to query the downstream connector. </p>"""
    connector_type: NotRequired["capo_appflow.types.connector_type.ConnectorType"]
    """<p> The type of connector, such as Salesforce, Amplitude, and so on. </p>"""
    entities_path: NotRequired["capo_appflow.types.entities_path.EntitiesPath"]
    """<p> This optional parameter is specific to connector implementation. Some connectors support multiple levels or categories of entities. You can find out the list of roots for such providers by sending a request without the <code>entitiesPath</code> parameter. If the connector supports entities at different roots, this initial request returns the list of roots. Otherwise, this request returns all entities supported by the provider. </p>"""
    api_version: NotRequired["capo_appflow.types.api_version.ApiVersion"]
    """<p>The version of the API that's used by the connector.</p>"""
    max_results: NotRequired[
        "capo_appflow.types.list_entities_max_results.ListEntitiesMaxResults"
    ]
    """<p>The maximum number of items that the operation returns in the response.</p>"""
    next_token: NotRequired["capo_appflow.types.next_token.NextToken"]
    """<p>A token that was provided by your prior <code>ListConnectorEntities</code> operation if the response was too big for the page size. You specify this token to get the next page of results in paginated response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConnectorEntitiesRequest) -> dict:
    out: dict = {}
    if "connector_profile_name" in value:
        out["connectorProfileName"] = value["connector_profile_name"]
    if "connector_type" in value:
        import capo_appflow.types.connector_type

        out["connectorType"] = capo_appflow.types.connector_type.serialize_json(
            value["connector_type"]
        )
    if "entities_path" in value:
        out["entitiesPath"] = value["entities_path"]
    if "api_version" in value:
        out["apiVersion"] = value["api_version"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListConnectorEntitiesRequest:
    out: ListConnectorEntitiesRequest = {}  # type: ignore[typeddict-item]
    if "connectorProfileName" in data:
        out["connector_profile_name"] = data["connectorProfileName"]
    if "connectorType" in data:
        import capo_appflow.types.connector_type

        out["connector_type"] = capo_appflow.types.connector_type.deserialize_json(
            data["connectorType"]
        )
    if "entitiesPath" in data:
        out["entities_path"] = data["entitiesPath"]
    if "apiVersion" in data:
        out["api_version"] = data["apiVersion"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
