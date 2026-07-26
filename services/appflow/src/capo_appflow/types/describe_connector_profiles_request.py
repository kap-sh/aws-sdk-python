"""Generated from Smithy shape ``com.amazonaws.appflow#DescribeConnectorProfilesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.connector_label
    import capo_appflow.types.connector_profile_name_list
    import capo_appflow.types.connector_type
    import capo_appflow.types.max_results
    import capo_appflow.types.next_token


class DescribeConnectorProfilesRequest(TypedDict, closed=True):
    connector_profile_names: NotRequired[
        "capo_appflow.types.connector_profile_name_list.ConnectorProfileNameList"
    ]
    """<p> The name of the connector profile. The name is unique for each <code>ConnectorProfile</code> in the Amazon Web Services account. </p>"""
    connector_type: NotRequired["capo_appflow.types.connector_type.ConnectorType"]
    """<p> The type of connector, such as Salesforce, Amplitude, and so on. </p>"""
    connector_label: NotRequired["capo_appflow.types.connector_label.ConnectorLabel"]
    """<p>The name of the connector. The name is unique for each <code>ConnectorRegistration</code> in your Amazon Web Services account. Only needed if calling for CUSTOMCONNECTOR connector type/.</p>"""
    max_results: NotRequired["capo_appflow.types.max_results.MaxResults"]
    """<p> Specifies the maximum number of items that should be returned in the result set. The default for <code>maxResults</code> is 20 (for all paginated API operations). </p>"""
    next_token: NotRequired["capo_appflow.types.next_token.NextToken"]
    """<p> The pagination token for the next page of data. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeConnectorProfilesRequest) -> dict:
    out: dict = {}
    if "connector_profile_names" in value:
        import capo_appflow.types.connector_profile_name_list

        out["connectorProfileNames"] = (
            capo_appflow.types.connector_profile_name_list.serialize_json(
                value["connector_profile_names"]
            )
        )
    if "connector_type" in value:
        import capo_appflow.types.connector_type

        out["connectorType"] = capo_appflow.types.connector_type.serialize_json(
            value["connector_type"]
        )
    if "connector_label" in value:
        out["connectorLabel"] = value["connector_label"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeConnectorProfilesRequest:
    out: DescribeConnectorProfilesRequest = {}  # type: ignore[typeddict-item]
    if "connectorProfileNames" in data:
        import capo_appflow.types.connector_profile_name_list

        out["connector_profile_names"] = (
            capo_appflow.types.connector_profile_name_list.deserialize_json(
                data["connectorProfileNames"]
            )
        )
    if "connectorType" in data:
        import capo_appflow.types.connector_type

        out["connector_type"] = capo_appflow.types.connector_type.deserialize_json(
            data["connectorType"]
        )
    if "connectorLabel" in data:
        out["connector_label"] = data["connectorLabel"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
